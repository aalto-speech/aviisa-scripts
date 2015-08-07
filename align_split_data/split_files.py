#!/usr/bin/env python3

import os
import sys
import wave

def main(align_file, wav_file, wav_out_dir):
    cur_start = 0
    cur_index = 0

    in_wav = wave.open(wav_file)
    bn = os.path.splitext(os.path.basename(wav_file))[0]
    params = in_wav.getparams()
    data = in_wav.readframes(params.nframes)
    in_wav.close()

    for line in open(align_file, encoding='iso-8859-15').readlines()[1:]:
        s,e,phone = line.split(None, 2)
        if phone.strip() == "__":
            end = (int(e) + int(s)) // 2

            out_wav = wave.open(os.path.join(wav_out_dir, "{}_{:03}.wav".format(bn, cur_index)), 'w')
            out_wav.setparams(params)

            out_wav.writeframes(data[cur_start*2:end*2])
            out_wav.close()

            cur_index += 1
            cur_start = end

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])