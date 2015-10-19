export TRAIN_NAME='sme_F_sri_6g_m'
export TRAIN_DIR="$GROUP_DIR/p/sami/lmmodels/$TRAIN_NAME"

export SOURCE_FILES=$GROUP_DIR/p/sami/audio_files/sme_F/train.trn:$GROUP_DIR/p/sami/wikipedia.txt

export NGRAM_ORDER=6
export PRUNE_THRESHOLD=5e-9

export LA_NGRAM_ORDER=3
export LA_PRUNE_THRESHOLD=5e-8

export MORPH_TRAIN_OPTIONS=""
