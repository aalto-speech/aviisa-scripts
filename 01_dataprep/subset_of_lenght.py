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


def main(scp_file, trn_file, seconds, out):

    trn = {}

    for line in open(trn_file, encoding="utf-8"):
        sent, key = line.strip().rsplit(None, 1)
        trn[key[1:-1]] = sent

    wav_list = [l.strip() for l in open(scp_file, encoding="utf-8").readlines() if len(l.strip()) > 0]
    nwl = []
    ntrn = {}

    random.seed(wave.open(wav_list[0]).getnframes())

    tot_seconds = 0
    random.shuffle(wav_list)
    for wav in wav_list:
        if tot_seconds > seconds:
            break

        with wave.open(wav) as wf:
            tot_seconds += wf.getnframes() / wf.getframerate()

        name = path.splitext(path.basename(wav))[0]
        nwl.append(wav)
        ntrn[name] = trn[name]

    make_trn(ntrn, out + '.trn')
    with open(out + ".scp", 'w', encoding='utf-8') as f:
        for w in sorted(nwl):
            print(w, file=f)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4])
