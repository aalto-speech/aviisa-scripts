#!/usr/bin/env python3
import string
import sys
from os import path

def clean(file_prefix):
    trn = {}
    scp = {}
    for line in open(file_prefix + ".trn", encoding="utf-8"):
        sent, key = line.strip().rsplit(None, 1)
        trn[key[1:-1]] = sent

    for line in open(file_prefix + ".scp", encoding="utf-8"):
        name = path.splitext(path.basename(line.strip()))[0]
        scp[name] = line.strip()

    forbidden_chars = string.digits + "."
    forbidden = set()
    for k,v in trn.items():
        if any(c in forbidden_chars for c in v):
            forbidden.add(k)

    with open(file_prefix + ".trn", 'w', encoding="utf-8") as t:
        for k,v in trn.items():
            if k not in forbidden:
                print("{} ({})".format(v,k), file=t)

    with open(file_prefix + ".scp", 'w', encoding="utf-8") as s:
        for k,v in scp.items():
            if k not in forbidden:
                print(v, file=s)

if __name__ == "__main__":
    for f in sys.argv[1:]:
        clean(f)
