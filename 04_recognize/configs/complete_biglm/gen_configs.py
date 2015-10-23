#!/usr/bin/env python3
import os
import glob


for lang in ("sme", "est", "fin"):
    for gender in ("M", "F"):
        for order in [4,10,20]:
            with open("{}{}_cb_v_{}g_m.sh".format(lang,gender,order), 'w') as f:
                print("export TEST_NAME='{}{}_cb_v_{}g_m'".format(lang,gender,order), file=f)
                print("export TEST_DIR=$GROUP_DIR/p/sami/recog_tests/complete_biglm/", file=f)
                print(file=f)
                print("export TEST_LM_SCALES=30", file=f)
                print(file=f)

                possible_ams = list(glob.glob(os.environ["GROUP_DIR"]+"/p/sami/models/{}_{}/hmm/*_22.ph".format(lang, gender)))
                am = possible_ams[0][:-3]

                print("export TEST_AM={}".format(am), file=f)
                print("export TEST_LM=$GROUP_DIR/p/sami/lmmodels/complete_biglm/{}{}_cb_v_{}g_m".format(lang,gender,order), file=f)

                print("export TEST_TRN=$GROUP_DIR/p/sami/audio_data/{}_{}/devel200.trn".format(lang, gender), file=f)
                print("export TEST_WAVLIST=$GROUP_DIR/p/sami/audio_data/{}_{}/devel200.scp".format(lang, gender), file=f)

                print("export ONE_BYTE_ENCODING=ISO-8859-10", file=f)
