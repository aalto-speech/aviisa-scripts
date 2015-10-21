#!/usr/bin/env python3

for lang in ("sme", "est", "fin"):
    for gender in ("M", "F"):
        for order in [4,10]:
            with open("{}{}_b_v_{}g_m.sh".format(lang,gender,order), 'w') as f:
                print("export TRAIN_NAME='{}{}_b_v_{}g_m'".format(lang,gender,order), file=f)
                print("export TRAIN_DIR=$GROUP_DIR/p/sami/lmmodels/biglm/$TRAIN_NAME", file=f)
                print(file=f)
                print("export SOURCE_FILES=$GROUP_DIR/p/sami/audio_data/{}_{}/train.trn:$GROUP_DIR/p/sami/lmdata/{}/biglm.txt".format(lang, gender, lang), file=f)
                print(file=f)
                print("export NGRAM_ORDER={}".format(order), file=f)
                print("export PRUNE_THRESHOLD=5e-9", file=f)
                print(file=f)
                print("export LA_NGRAM_ORDER={}".format(order//3), file=f)
                print("export LA_PRUNE_THRESHOLD=5e-8", file=f)


                print("export MORPH_TRAIN_OPTIONS=\"\"", file=f)

                print("export VARIKN_OPTIONS=\"\"", file=f)
                count = 100000
                print("export VARIKN_DEVSIZE={}".format(count), file=f)
