#!/bin/bash 

BASE_DIR=$(readlink -f $(dirname "$0"))/..

if [ -z "$1" ]; then
    echo "Provide a config file"
    exit
fi

source "$1"



ngram -order $NGRAM_ORDER -unk -lm $TRAIN_DIR/model.gz -prune $PRUNE_THRESHOLD -write-lm $TRAIN_DIR/model_pruned
ngram -order $LA_NGRAM_ORDER -unk -lm $TRAIN_DIR/model.gz -prune $LA_PRUNE_THRESHOLD -write-lm $TRAIN_DIR/model_la

lm --arpa="$TRAIN_DIR/model_pruned" --out-bin="$TRAIN_DIR/model_pruned.fsabin"
arpa2bin < "$TRAIN_DIR/model_la" > "$TRAIN_DIR/model_la.bin"

if [ -z $MORPH_TRAIN_OPTIONS ]; then
extra_option="-morph"
fi

$BASE_DIR/../02_amtraining/base_scripts/vocab2lex.pl $extra_option -read="$TRAIN_DIR/vocab" >"$TRAIN_DIR/vocab.lex"

