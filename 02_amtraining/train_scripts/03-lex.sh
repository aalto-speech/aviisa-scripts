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

$BASE_DIR/base_scripts/vocab2lex.pl -read="$TRAIN_DIR/train.vocab" \
>>"$LEX"
