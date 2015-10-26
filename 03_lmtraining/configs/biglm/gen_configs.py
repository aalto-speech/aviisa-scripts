#!/usr/bin/env python3

for lang in ("sme", "est", "fin"):
    for order in [4,10,20]:
        with open("{}_b60k_v_{}g_m.sh".format(lang,order), 'w') as f:
            print("export TRAIN_NAME='{}_b60k_v_{}g_m'".format(lang,order), file=f)
            print("export TRAIN_DIR=$GROUP_DIR/p/sami/lmmodels/biglm/$TRAIN_NAME", file=f)
            print(file=f)
            print("export SOURCE_FILES=$GROUP_DIR/p/sami/lmdata/{}/biglm.txt".format(lang), file=f)
            print(file=f)
            print("export NGRAM_ORDER={}".format(order), file=f)
            print("export PRUNE_THRESHOLD=5e-9", file=f)
            print(file=f)
            print("export LA_NGRAM_ORDER={}".format(order//3), file=f)
            print("export LA_PRUNE_THRESHOLD=5e-8", file=f)

            print("export MORPH_TRAIN_OPTIONS=\" --num-morph-types=60000 \"", file=f)

            print("export VARIKN_OPTIONS=\"-s --dscale=0.0025\"", file=f)
            count = 20000
            print("export VARIKN_DEVSIZE={}".format(count), file=f)


for lang in ("sme", "est", "fin"):
    for order in [4,10,20]:
        with open("{}_b60kv_v_{}g_m.sh".format(lang,order), 'w') as f:
            print("export TRAIN_NAME='{}_b60kv_v_{}g_m'".format(lang,order), file=f)
            print("export TRAIN_DIR=$GROUP_DIR/p/sami/lmmodels/biglm/$TRAIN_NAME", file=f)
            print(file=f)
            print("export SOURCE_FILES=$GROUP_DIR/p/sami/lmdata/{}/biglm.txt".format(lang), file=f)
            print(file=f)
            print("export NGRAM_ORDER={}".format(order), file=f)
            print("export PRUNE_THRESHOLD=5e-9", file=f)
            print(file=f)
            print("export LA_NGRAM_ORDER={}".format(order//3), file=f)
            print("export LA_PRUNE_THRESHOLD=5e-8", file=f)

            print("export MORPH_TRAIN_OPTIONS=\"\"", file=f)

            print("export VARIKN_OPTIONS=\"-s -f --nfirst=60000 --dscale=0.0025\"", file=f)
            count = 20000
            print("export VARIKN_DEVSIZE={}".format(count), file=f)
