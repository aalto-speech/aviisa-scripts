#!/usr/bin/env python3
import os

import sys

def main(langdat_dir, trn_file, phn_dir):
    phone_map = {v[0]: v[1].strip() for v in (l.split(None, 1) for l in open('{}/phones'.format(langdat_dir), encoding='utf-8'))}

    for line in open(trn_file):
        parts = line.split()
        sentence = parts[:-1]
        sid = parts[-1][1:-1]
        phn = open(os.path.join(phn_dir,sid+".phn"), "w", encoding="iso8859-15")


        print("0 0 __", file=phn)

        phones = '_'
        for word in sentence:
            for c in word:
                phones += phone_map[c]
            phones += '_'

        for j in range(1, len(phones)-1):
            if phones[j] == '_':
                print("0 0 _", file=phn)
                continue

            lci = j -1
            while lci > 0 and phones[lci] == '_':
                lci -= 1

            rci = j +1
            while rci < len(phones) - 1 and phones[rci] == '_':
                rci += 1

            print("0 0 {}-{}+{}".format(phones[lci], phones[j], phones[rci]), file=phn)

        print("0 0 __", file=phn)

        phn.close()



if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])