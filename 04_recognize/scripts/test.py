#!/usr/bin/env python3

from os import path
import os

def exists_and_not_empty(f):
    try:
        return path.getsize(f) > 100
    except:
        return False

def check():
    files = [path.join(os.environ['TEST_DIR'], 'recognitions', "{}--{}-fsa-b280-s30-tl100k.trn.sclite_ler".format(path.basename(os.environ['TEST_AM']),path.basename(os.environ['TEST_LM']))),
             path.join(os.environ['TEST_DIR'], 'recognitions', "{}--{}-fsa-b280-s30-tl100k.trn.sclite_wer".format(path.basename(os.environ['TEST_AM']),path.basename(os.environ['TEST_LM']))),
             path.join(os.environ['TEST_DIR'], 'recognitions', "{}--{}-fsa-b280-s30-tl100k.trn".format(path.basename(os.environ['TEST_AM']),path.basename(os.environ['TEST_LM']))),
             ]

    for f in files:
        if not exists_and_not_empty(f):
            print(os.environ['TEST_NAME'])
            exit(1)

if __name__ == "__main__":
    check()
