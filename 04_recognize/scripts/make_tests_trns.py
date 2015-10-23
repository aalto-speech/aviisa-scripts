#!/usr/bin/env python3

from os.path import join
import sys


def make_ler(inf, outf):
    with open(outf, 'w', encoding='utf-8') as of:
        for line in open(inf, encoding='utf-8'):
            parts = line.strip().split()
            for i in range(len(parts) - 1):
                parts[i] = " ".join(list(parts[i]))
            print(" _ ".join(parts), file=of)


def encode(inf, outf, encoding):
    with open(outf, 'w', encoding=encoding) as of:
        for line in open(inf, encoding='utf-8'):
            print(line.strip(), file=of)


def main(out_dir, ref_trn, hyp_trn, encoding):
    encode(ref_trn, join(out_dir, "ref_wer.iso.trn"), encoding)
    encode(hyp_trn, join(out_dir, "hyp_wer.iso.trn"), encoding)

    make_ler(ref_trn, join(out_dir, "ref_ler.trn"))
    make_ler(hyp_trn, join(out_dir, "hyp_ler.trn"))

    encode(join(out_dir, "ref_ler.trn"), join(out_dir, "ref_ler.iso.trn"), encoding)
    encode(join(out_dir, "hyp_ler.trn"), join(out_dir, "hyp_ler.iso.trn"), encoding)


if __name__ == "__main__":
    main(*sys.argv[1:5])
