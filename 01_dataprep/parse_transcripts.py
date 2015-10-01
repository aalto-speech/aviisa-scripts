#!/usr/bin/env python3
import itertools
import os
import re
import string
import sys


def main(txt_file, phn_file, transcript_file):

    phone_map = {v[0]: v[1].strip() for v in (l.split(None, 1) for l in open('data/phone_map', encoding='utf-8'))}
    abbr_map = {v[0]: v[1].strip() for v in (l.split(None, 1) for l in open('data/sme/abbreviations', encoding='utf-8'))}
    allowed_chars = set(phone_map.keys()) | set(string.digits)

    sentences = find_sentences(open(txt_file), allowed_chars, abbr_map)
    fdsentences = fix_digits(sentences)

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


def fix_digits(sentences):
    digit_map = {v[0]: v[1].strip() for v in (l.split(None, 1) for l in open('data/number_transcriptions', encoding='utf-8'))}

    def number_to_word(word):
        nonlocal digit_map
        if word.isdigit():
            if word in digit_map:
                return digit_map[word]
            else:
                exit("Please provide a transcription for {} in number_transcriptions".format(word))
        return word

    s = []
    for sentence in sentences:
        s.append(list(map(number_to_word, itertools.chain.from_iterable(re.split(r'(\d+)', w) for w in sentence))))
    return s


def find_sentences(f, allowed_chars, abbr_map):
    """Return sentences in 2 dimensional (sentence, word) array.
    A sentence ends on a line break or a punctuation character . ! ?
    """
    line_ends = ".!?"

    cur_word = ""
    cur_sentence = []
    sentences = []

    def finish_word():
        nonlocal cur_word, cur_sentence
        if len(cur_word) > 0:
            cur_sentence.append(cur_word)
        cur_word = ""

    def finish_sentence():
        finish_word()
        nonlocal cur_sentence, sentences
        if len(cur_sentence) > 0:
            sentences.append(cur_sentence)
        cur_sentence = []

    def put_char(c):
        nonlocal cur_word, allowed_chars
        if c.lower() in allowed_chars:
            cur_word += c.lower()

    for line in f:
        parts = line.split()
        for p in parts:
            if p in abbr_map:
                p = abbr_map[p]
            if any(c in string.digits for c in p):
                p = p.split
        for c in line:
            if c.isspace():
                finish_word()
            elif c in line_ends:
                finish_sentence()
            else:
                put_char(c)

        finish_sentence()

    return sentences

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])