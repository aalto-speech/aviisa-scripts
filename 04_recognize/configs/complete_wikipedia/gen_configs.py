#!/usr/bin/env python3
import os
import glob


for lang in ("sme", "est", "fin"):
    for gender in ("M", "F"):
        for tool in ("s", "v"):
            for order in range(5,10):
                for type in ("m", "w"):
                    with open("{}{}_cow_{}_{}g_{}.sh".format(lang,gender,tool,order,type), 'w') as f:
                        print("export TEST_NAME='{}{}_cow_{}_{}g_{}'".format(lang,gender,tool,order,type), file=f)
                        print("export TEST_DIR=$GROUP_DIR/p/sami/recog_tests/complete_wikipedia/", file=f)
                        print(file=f)
                        print("export TEST_LM_SCALES=30", file=f)
                        print(file=f)

                        possible_ams = list(glob.glob(os.environ["GROUP_DIR"]+"/p/sami/models/{}_{}/hmm/*_22.ph".format(lang, gender)))
                        am = possible_ams[0][:-3]

                        print("export TEST_AM={}".format(am), file=f)
                        print("export TEST_LM=$GROUP_DIR/p/sami/lmmodels/complete_wikipedia/{}{}_cow_{}_{}g_{}".format(lang,gender,tool,order,type), file=f)

                        print("export TEST_TRN=$GROUP_DIR/p/sami/audio_data/{}_{}/devel.trn".format(lang, gender), file=f)
                        print("export TEST_WAVLIST=$GROUP_DIR/p/sami/audio_data/{}_{}/devel.scp".format(lang, gender), file=f)

                        print("export ONE_BYTE_ENCODING=ISO-8859-10", file=f)
