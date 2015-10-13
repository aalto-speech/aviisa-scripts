#!/usr/bin/env python3

import sys


def main(phone_map, abbreviations):
    phone_map = {v[0]: v[1].strip()
                 for v in (l.split(None, 1)
                           for l in open(phone_map, encoding='utf-8'))}
    abbr_map = {v[0]: v[1].strip().split(',')
                for v in (l.split(None, 1)
                          for l in open(abbreviations, encoding='utf-8'))} if abbreviations is not None else {}

    o = sys.stdout.buffer
    o.write(b"__(1.0) __\n")
    o.write(b"_(1.0) _\n")
    o.write(b"<s>(1.0)\n")
    o.write(b"</s>(1.0)\n")

    for word in sys.stdin.readlines():
        word = word.strip()
        transcriptions = []
        basic = [phone_map[c] for c in word if c in phone_map]
        if len(basic) > 0:
            transcriptions.append(basic)

        if word in abbr_map:
            for abbr in abbr_map[word]:
                transcriptions.append([phone_map[c] for c in abbr if c in phone_map])

        transcriptions = set(tuple(t) for t in transcriptions)
        for trans in transcriptions:
            o.write("{}({:.1f})  ".format(word, 1/len(transcriptions)).encode("utf-8"))
            rtrans = ["_"]+list(trans)+["_"]
            for i in range(1, len(trans)+1):
                o.write("{}-{}+{} ".format(rtrans[i-1],rtrans[i],rtrans[i+1]).encode("iso-8859-15"))
            o.write(b"\n")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
