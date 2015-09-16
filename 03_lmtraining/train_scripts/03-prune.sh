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
   
$BASE_DIR/../02_amtraining/base_scripts/vocab2lex.pl -read="$TRAIN_DIR/vocab" >"$TRAIN_DIR/vocab.lex"



cat << EOF > $TRAIN_DIR/bin/convert_trn_word
cat < \&0
EOF


cat << EOF > $TRAIN_DIR/bin/convert_trn_letter

orig_file=\$(mktemp)
cat <\&0 > \$orig_file

namelist=\$(mktemp)
grep -o "(.*$" \$orig_file > \$namelist

cat \$orig_file | sed 's/(.*$//' | sed "s/ /_/g" | sed "s/\w/& /g" | paste -d" " - \$namelist | iconv -f UTF-8 -t $ONE_BYTE_ENCODING

rm \$orig_file \$namelist
EOF


