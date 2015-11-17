#!/usr/bin/env python3
import os
import glob


for lang in ("sme", "est", "fin"):
    for gender in ("M", "F"):
        for order in [4,10,20]:
            with open("{}{}_b_v_{}g_m.sh".format(lang,gender,order), 'w') as f:
                print("export TEST_NAME='{}{}_b_v_{}g_m'".format(lang,gender,order), file=f)
                print("export TEST_DIR=$GROUP_DIR/p/sami/recog_tests/biglm/", file=f)
                print(file=f)
                print("export TEST_LM_SCALES=30", file=f)
                print(file=f)

                possible_ams = list(glob.glob(os.environ["GROUP_DIR"]+"/p/sami/models/{}_{}/hmm/*_22.ph".format(lang, gender)))
                am = possible_ams[0][:-3]

                print("export TEST_AM={}".format(am), file=f)
                print("export TEST_LM=$GROUP_DIR/p/sami/lmmodels/biglm/{}{}_b_v_{}g_m".format(lang,gender,order), file=f)

                print("export TEST_TRN=$GROUP_DIR/p/sami/audio_data/{}_{}/devel200.trn".format(lang, gender), file=f)
                print("export TEST_WAVLIST=$GROUP_DIR/p/sami/audio_data/{}_{}/devel200.scp".format(lang, gender), file=f)

                print("export ONE_BYTE_ENCODING=ISO-8859-10", file=f)


for lang in ("sme", "est", "fin"):
    for gender in ("M", "F"):
        for order in [4,10,20]:
            with open("{}{}_b60k_v_{}g_m.sh".format(lang, gender ,order), 'w') as f:
                print("export TEST_NAME='{}{}_b60k_v_{}g_m'".format(lang,gender,order), file=f)
                print("export TEST_DIR=$GROUP_DIR/p/sami/recog_tests/biglm/", file=f)
                print(file=f)
                print("export TEST_LM_SCALES=30", file=f)
                print(file=f)

                possible_ams = list(glob.glob(os.environ["GROUP_DIR"]+"/p/sami/models/{}_{}/hmm/*_22.ph".format(lang, gender)))
                am = possible_ams[0][:-3]

                print("export TEST_AM={}".format(am), file=f)
                print("export TEST_LM=$GROUP_DIR/p/sami/lmmodels/biglm/{}_b60k_v_{}g_m".format(lang,order), file=f)

                print("export TEST_TRN=$GROUP_DIR/p/sami/audio_data/{}_{}/devel200.trn".format(lang, gender), file=f)
                print("export TEST_WAVLIST=$GROUP_DIR/p/sami/audio_data/{}_{}/devel200.scp".format(lang, gender), file=f)

                print("export ONE_BYTE_ENCODING=ISO-8859-10", file=f)

for lang in ("sme", "est", "fin"):
    g = ("M", "F")
    if lang == "est":
        g = ("M", "F", "M2")
    for gender in g:
        for order in [4,10,20]:
            with open("{}{}_b60kv_v_{}g_m.sh".format(lang, gender ,order), 'w') as f:
                print("export TEST_NAME='{}{}_b60kv_v_{}g_m'".format(lang,gender,order), file=f)
                print("export TEST_DIR=$GROUP_DIR/p/sami/recog_tests/biglm/", file=f)
                print(file=f)
                print("export TEST_LM_SCALES=30", file=f)
                print(file=f)

                possible_ams = list(glob.glob(os.environ["GROUP_DIR"]+"/p/sami/models/{}_{}/hmm/*_22.ph".format(lang, gender)))
                am = possible_ams[0][:-3]

                print("export TEST_AM={}".format(am), file=f)
                print("export TEST_LM=$GROUP_DIR/p/sami/lmmodels/biglm/{}_b60kv_v_{}g_m".format(lang,order), file=f)

                print("export TEST_TRN=$GROUP_DIR/p/sami/audio_data/{}_{}/devel200.trn".format(lang, gender), file=f)
                print("export TEST_WAVLIST=$GROUP_DIR/p/sami/audio_data/{}_{}/devel200.scp".format(lang, gender), file=f)

                print("export ONE_BYTE_ENCODING=ISO-8859-10", file=f)


for lang in ("sme", "est", "fin"):
    g = ("M", "F")
    if lang == "est":
        g = ("M", "F", "M2")
    for gender in g:
        for order in [4,10,20]:
            with open("{}{}_s1b60k_v_{}g_m.sh".format(lang, gender ,order), 'w') as f:
                print("export TEST_NAME='{}{}_s1b60k_v_{}g_m'".format(lang,gender,order), file=f)
                print("export TEST_DIR=$GROUP_DIR/p/sami/recog_tests/biglm/", file=f)
                print(file=f)
                print("export TEST_LM_SCALES=30", file=f)
                print(file=f)

                possible_ams = list(glob.glob(os.environ["GROUP_DIR"]+"/p/sami/models/{}_{}_150m/hmm/*_22.ph".format(lang, gender)))
                am = possible_ams[0][:-3]

                print("export TEST_AM={}".format(am), file=f)
                print("export TEST_LM=$GROUP_DIR/p/sami/lmmodels/biglm/{}_b60k_v_{}g_m".format(lang,order), file=f)

                print("export TEST_TRN=$GROUP_DIR/p/sami/audio_data/{}_{}/devel200.trn".format(lang, gender), file=f)
                print("export TEST_WAVLIST=$GROUP_DIR/p/sami/audio_data/{}_{}/devel200.scp".format(lang, gender), file=f)

                print("export ONE_BYTE_ENCODING=ISO-8859-10", file=f)


for lang in ("sme", "est", "fin"):
    for gender in ("M", "F"):
        for order in [4,10,20]:
            with open("{}{}_s1b60kv_v_{}g_m.sh".format(lang, gender ,order), 'w') as f:
                print("export TEST_NAME='{}{}_s1b60kv_v_{}g_m'".format(lang,gender,order), file=f)
                print("export TEST_DIR=$GROUP_DIR/p/sami/recog_tests/biglm/", file=f)
                print(file=f)
                print("export TEST_LM_SCALES=30", file=f)
                print(file=f)

                possible_ams = list(glob.glob(os.environ["GROUP_DIR"]+"/p/sami/models/{}_{}_150m/hmm/*_22.ph".format(lang, gender)))
                am = possible_ams[0][:-3]

                print("export TEST_AM={}".format(am), file=f)
                print("export TEST_LM=$GROUP_DIR/p/sami/lmmodels/biglm/{}_b60kv_v_{}g_m".format(lang,order), file=f)

                print("export TEST_TRN=$GROUP_DIR/p/sami/audio_data/{}_{}/devel200.trn".format(lang, gender), file=f)
                print("export TEST_WAVLIST=$GROUP_DIR/p/sami/audio_data/{}_{}/devel200.scp".format(lang, gender), file=f)

                print("export ONE_BYTE_ENCODING=ISO-8859-10", file=f)
lang = "sme"
for order in range(2, 21):
    for gender in ("M", "F"):
        with open("{}{}_s1b60kv_v_{}g_m.sh".format(lang, gender ,order), 'w') as f:
            print("export TEST_NAME='{}{}_s1b60kv_v_{}g_m'".format(lang,gender,order), file=f)
            print("export TEST_DIR=$GROUP_DIR/p/sami/recog_tests/biglm/", file=f)
            print(file=f)
            print("export TEST_LM_SCALES=30", file=f)
            print(file=f)

            possible_ams = list(glob.glob(os.environ["GROUP_DIR"]+"/p/sami/models/{}_{}/hmm/*_22.ph".format(lang, gender)))
            am = possible_ams[0][:-3]

            print("export TEST_AM={}".format(am), file=f)
            print("export TEST_LM=$GROUP_DIR/p/sami/lmmodels/biglm/{}_b60kv_v_{}g_m".format(lang,order), file=f)

            print("export TEST_TRN=$GROUP_DIR/p/sami/audio_data/{}_{}/devel200.trn".format(lang, gender), file=f)
            print("export TEST_WAVLIST=$GROUP_DIR/p/sami/audio_data/{}_{}/devel200.scp".format(lang, gender), file=f)

            print("export ONE_BYTE_ENCODING=ISO-8859-10", file=f)


        with open("{}{}_s1b60kv_s_{}g_m.sh".format(lang, gender ,order), 'w') as f:
            print("export TEST_NAME='{}{}_s1b60kv_s_{}g_m'".format(lang,gender,order), file=f)
            print("export TEST_DIR=$GROUP_DIR/p/sami/recog_tests/biglm/", file=f)
            print(file=f)
            print("export TEST_LM_SCALES=30", file=f)
            print(file=f)

            possible_ams = list(glob.glob(os.environ["GROUP_DIR"]+"/p/sami/models/{}_{}/hmm/*_22.ph".format(lang, gender)))
            am = possible_ams[0][:-3]

            print("export TEST_AM={}".format(am), file=f)
            print("export TEST_LM=$GROUP_DIR/p/sami/lmmodels/biglm/{}_b60kv_s_{}g_m".format(lang,order), file=f)

            print("export TEST_TRN=$GROUP_DIR/p/sami/audio_data/{}_{}/devel200.trn".format(lang, gender), file=f)
            print("export TEST_WAVLIST=$GROUP_DIR/p/sami/audio_data/{}_{}/devel200.scp".format(lang, gender), file=f)

            print("export ONE_BYTE_ENCODING=ISO-8859-10", file=f)


        with open("{}{}_s1b60kv_s_{}g_w.sh".format(lang, gender ,order), 'w') as f:
            print("export TEST_NAME='{}{}_s1b60kv_s_{}g_w'".format(lang,gender,order), file=f)
            print("export TEST_DIR=$GROUP_DIR/p/sami/recog_tests/biglm/", file=f)
            print(file=f)
            print("export TEST_LM_SCALES=30", file=f)
            print(file=f)

            possible_ams = list(glob.glob(os.environ["GROUP_DIR"]+"/p/sami/models/{}_{}/hmm/*_22.ph".format(lang, gender)))
            am = possible_ams[0][:-3]

            print("export TEST_AM={}".format(am), file=f)
            print("export TEST_LM=$GROUP_DIR/p/sami/lmmodels/biglm/{}_b60kv_s_{}g_w".format(lang,order), file=f)

            print("export TEST_TRN=$GROUP_DIR/p/sami/audio_data/{}_{}/devel200.trn".format(lang, gender), file=f)
            print("export TEST_WAVLIST=$GROUP_DIR/p/sami/audio_data/{}_{}/devel200.scp".format(lang, gender), file=f)

            print("export ONE_BYTE_ENCODING=ISO-8859-10", file=f)
