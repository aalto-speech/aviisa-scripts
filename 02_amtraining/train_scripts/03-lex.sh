#!/bin/bash 

BASE_DIR=$(readlink -f $(dirname "$0"))/..

if [ -z "$1" ]; then
    echo "Provide a config file"
    exit
fi

source "$1"

mkdir -p "$TRAIN_DIR"

LEX="$TRAIN_DIR/train.lex"

sed 's/(.*$//' "$TRAIN_TRN" \
| tr ' ' '\n' \
| sort -u \
>"$TRAIN_DIR/train.vocab"

cat $LANGDAT_DIR/abbreviations > $TRAIN_DIR/extra_abbr
seq 1 9999 | $LANGDAT_DIR/number_to_words > $TRAIN_DIR/extra_nums
seq 1 9999 | paste -d" " - $TRAIN_DIR/extra_nums >> $TRAIN_DIR/extra_abbr

$BASE_DIR/base_scripts/vocab2lex.py $LANGDAT_DIR/phones $TRAIN_DIR/extra_abbr  < $TRAIN_DIR/train.vocab >"$LEX"
