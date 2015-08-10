#!/usr/bin/env python3
import glob
import os
from os import path
import random
import shutil
import sys
import wave

TRAIN_PERCENT=75
DEV_PERCENT=15


def copy_files(file_list, out_dir, scp_file):
    with open(scp_file, 'w') as scp_f:
        for f in file_list:
            shutil.copyfile(f, path.join(out_dir, path.basename(f)))
            print(path.join(out_dir, path.basename(f)), file=scp_f)


def make_trn(trn, trn_file):
    with open(trn_file, 'w') as trn_f:
        for k, v in sorted(trn.items()):
            print("{} ({})".format(v,k), file=trn_f)


def main(wav_dir, trn_dir, hours, out):

    trn = {}
    tr_files = []
    de_files = []
    ev_files = []

    tr_trn = {}
    de_trn = {}
    ev_trn = {}

    for file in glob.iglob(path.join(trn_dir, "*.trn")):
        for line in open(file, encoding="utf-8"):
            sent, key = line.strip().rsplit(None, 1)
            trn[key[1:-1]] = sent

    wav_list = sorted(glob.glob(path.join(wav_dir, "*.wav")))

    random.seed(wave.open(wav_list[0]).getnframes())

    tot_hours = 0
    for wav in wav_list:
        if tot_hours > hours:
            break

        with wave.open(wav) as wf:
            seconds = wf.getnframes() / wf.getsampwidth() / wf.getframerate()
            tot_hours += seconds / 3600


        name = path.splitext(path.basename(wav))[0]
        full_path = path.realpath(wav)

        r = random.random()
        if r < TRAIN_PERCENT/100:
            tr_files.append(full_path)
            tr_trn[name] = trn[name]
        elif r < (TRAIN_PERCENT + DEV_PERCENT)/100:
            de_files.append(full_path)
            de_trn[name] = trn[name]
        else:
            ev_files.append(full_path)
            ev_trn[name] = trn[name]

    for w in ("train", "eval", "devel"):
        if path.exists(path.join(out, w)):
            shutil.rmtree(path.join(out, w))
        os.makedirs(path.join(out,w))

    make_trn(tr_trn, path.join(out, 'train.trn'))
    make_trn(de_trn, path.join(out, 'devel.trn'))
    make_trn(ev_trn, path.join(out, 'eval.trn'))


    copy_files(tr_files, path.join(out, "train"), path.join(out, "train.scp"))
    copy_files(de_files, path.join(out, "devel"), path.join(out, "devel.scp"))
    copy_files(ev_files, path.join(out, "eval"), path.join(out, "eval.scp"))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4])