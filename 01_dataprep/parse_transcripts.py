#!/usr/bin/env python3
import itertools
import os
import re
import string
from subprocess import Popen, PIPE
import sys
import collections


def main(txt_file, phn_file, transcript_file, langdat_dir, sentence_per_line):

    phone_map = {v[0]: v[1].strip() for v in (l.split(None, 1) for l in open('{}/phones'.format(langdat_dir), encoding='utf-8'))}
    abbr_map = {v[0]: v[1].strip().split() for v in (l.split(None, 1) for l in open('{}/abbreviations'.format(langdat_dir), encoding='utf-8') if len(l.strip()) > 0)}
    allowed_chars = set(phone_map.keys()) | set(string.digits)

    sentences = find_sentences(open(txt_file), allowed_chars, abbr_map, sentence_per_line)
    def get_number_trans(word):
        (trans, _) = Popen(['{}/number_to_words'.format(langdat_dir)], stdin=PIPE, stderr=PIPE, stdout=PIPE).communicate(word.encode('utf-8'))
        return [trans.decode('utf-8').strip().split(',')[0]]

    phsentences = to_phonetic_words(sentences, abbr_map, get_number_trans)

    fdsentences = phsentences

    phn = open(phn_file, "w", encoding="iso8859-15")
    tra = open(transcript_file, "w")


    index = 0
    bn = os.path.splitext(os.path.basename(txt_file))[0]

    for sentence, bssentence in zip(fdsentences, sentences):
        print("{} ({}_{:03})".format(" ".join(bssentence), bn, index), file=tra)
        print("0 0 __", file=phn)

        phones = '_'
        for word in sentence:
            for c in word:
                if c == "\n":
                    pass
                phones += phone_map[c]
            phones += '_'

        for j in range(1, len(phones)-1):
            if phones[j] == '_':
                print("0 0 _", file=phn)
                continue

            lci = j - 1
            while lci > 0 and phones[lci] == '_':
                lci -= 1

            rci = j + 1
            while rci < len(phones) - 1 and phones[rci] == '_':
                rci += 1

            print("0 0 {}-{}+{}".format(phones[lci], phones[j], phones[rci]), file=phn)
        index += 1

    print("0 0 __", file=phn)


def to_phonetic_words(sentences, abbr_map, digit_script):
    ### this always pick only one possible phone transcription

    ready_sentences = []
    for sentence in sentences:
        cur_s = []
        for word in sentence:
            if word in abbr_map:
                cur_s.extend(abbr_map[word])
            elif word.isdigit():
                cur_s.extend(digit_script(word))
            else:
                cur_s.append(word)

        ready_sentences.append(cur_s)
    return ready_sentences


def find_sentences(f, allowed_chars, abbr_map, sentence_per_line=True):
    """Return sentences in 2 dimensional (sentence, word) array.
    A sentence ends on a line break or a punctuation character . ! ?
    """
    line_ends = ".!?"

    cur_sentence = []
    sentences = []
    discards = collections.Counter()

    def finish_sentence():
        nonlocal cur_sentence, sentences
        if len(cur_sentence) > 0:
            sentences.append(cur_sentence)
        cur_sentence = []

    for line in f:
        parts = line.lower().split()
        for p in parts:
            break_sentence = False
            if p in abbr_map:
                #p = abbr_map[p]
                cur_sentence.append(p)
                continue

            p = re.split('(\d+|[\(\)\\,]+)', p)

            if len(p[-1])> 0 and p[-1][-1] in line_ends:
                break_sentence = True

            for part in p:
                part1 = "".join([c for c in part if c in allowed_chars])
                discards.update(c for c in part if c not in allowed_chars)
                if len(part1) > 0:
                    cur_sentence.append(part1)
            if break_sentence:
                finish_sentence()
        if sentence_per_line:
            finish_sentence()
    finish_sentence()
    print(discards)
    return sentences

if __name__ == "__main__":
    sentence_per_line = True
    if len(sys.argv) > 5:
        sentence_per_line = not sys.argv[5].startswith("nosplit")
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sentence_per_line)