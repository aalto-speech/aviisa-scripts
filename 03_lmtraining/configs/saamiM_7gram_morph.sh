export TRAIN_NAME='saamiM_7gram_morph'
export TRAIN_DIR="$GROUP_DIR/p/sami/lmmodels/$TRAIN_NAME"

export SOURCE_FILES=$GROUP_DIR/p/sami/uit-sme-M/train.trn:$GROUP_DIR/p/sami/wikipedia.txt

export NGRAM_ORDER=7
export PRUNE_THRESHOLD=5e-9

export LA_NGRAM_ORDER=3
export LA_PRUNE_THRESHOLD=5e-8

export MORPH_TRAIN_OPTIONS=""
