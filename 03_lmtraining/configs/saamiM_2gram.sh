export TRAIN_NAME='saamiM_2gram_word'
export TRAIN_DIR="$GROUP_DIR/p/sami/lmmodels/$TRAIN_NAME"

export SOURCE_FILES=$GROUP_DIR/p/sami/uit-sme-M/train.trn:$GROUP_DIR/p/sami/wikipedia.txt

export NGRAM_ORDER=2
export PRUNE_THRESHOLD=5e-9

export LA_NGRAM_ORDER=1
export LA_PRUNE_THRESHOLD=5e-8

