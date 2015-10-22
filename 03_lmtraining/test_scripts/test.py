#!/usr/bin/env python3

from os import path
import os

def exists_and_not_empty(f):
    try:
        return path.getsize(f) > 100
    except:
        return False

def check():
    files = [path.join(os.environ['TRAIN_DIR'], os.environ['TRAIN_NAME']),
             path.join(os.environ['TRAIN_DIR'], os.environ['TRAIN_NAME']+".fsabin"),
             path.join(os.environ['TRAIN_DIR'], "model_la"),
             path.join(os.environ['TRAIN_DIR'], "model_la.bin"),
             path.join(os.environ['TRAIN_DIR'], "vocab.lex"),
             ]

    for f in files:
        if not exists_and_not_empty(f):
            print(os.environ['TRAIN_NAME'])
            exit(1)

if __name__ == "__main__":
    check()
