#!/usr/bin/env python3
import os
import sys

line_ends = set('!?.')
allowed_punctuations = set(":;(),'\"")

def main(phones):
    allowed_chars = set()
    for line in open(phones):
        if len(line.strip()) == 0:
            continue
        k = line.split()[0]
        allowed_chars.update(*k)
    allowed_chars.add(" ")

    a = allowed_chars | allowed_punctuations | line_ends

    def process_line(cur_line):
        real_line = []
        for p in cur_line:
            q  = p.lower()
            if any(x not in a for x in q):
                return
            s = "".join(x for x in q if x in allowed_chars).strip()
            if len(s) > 0:
                real_line.append(s)

        #l = "".join(x for x in cur_line if x in allowed_chars).strip()
        if len(real_line) > 2:
            print(" ".join(real_line))

    for line in sys.stdin:
        parts = line.split()
        cur_line = []
        for p in parts:
            cur_line.append(p)
            if p[-1] in line_ends:
                process_line(cur_line)
                cur_line = []
        process_line(cur_line)

if __name__ == "__main__":
    main(sys.argv[1])
