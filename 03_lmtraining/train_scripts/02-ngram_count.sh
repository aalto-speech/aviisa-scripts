#!/bin/bash 

BASE_DIR=$(readlink -f $(dirname "$0"))/..

if [ -z "$1" ]; then
    echo "Provide a config file"
    exit
fi

source "$1"


if [ ! -z ${VARIKN_OPTIONS+x} ]; then

sort -R < $TRAIN_DIR/lm_source_txt > $TRAIN_DIR/lm_source_txt_rand
head -n ${VARIKN_DEVSIZE} $TRAIN_DIR/lm_source_txt_rand > $TRAIN_DIR/varikn_dev
tail -n +${VARIKN_DEVSIZE} $TRAIN_DIR/lm_source_txt_rand > $TRAIN_DIR/varikn_train


varigram_kn $VARIKN_OPTIONS -3 -C -a -Z -U $TRAIN_DIR/vocab -n $NGRAM_ORDER -o $TRAIN_DIR/varikn_dev $TRAIN_DIR/varikn_train "$TRAIN_DIR/${TRAIN_NAME}"

else

for knd in $(seq $NGRAM_ORDER -1 1); do


    INTERPOLATE=$(seq 1 $NGRAM_ORDER | sed "s/^/-interpolate/" | tr "\n" " ")
    KNDISCOUNT=$(seq 1 $knd | sed "s/^/-kndiscount/" | tr "\n" " ")
    WBDISCOUNT=""
    if [ $knd != $NGRAM_ORDER ]; then
        WBDISCOUNT=$(seq $((knd+1)) $NGRAM_ORDER | sed "s/^/-wbdiscount/" | tr "\n" " ")
    fi

    echo $KNDISCOUNT $WBDISCOUNT
    cat $TRAIN_DIR/lm_source_txt | \
    ngram-count \
      -order $NGRAM_ORDER \
      $INTERPOLATE \
      -text - \
      -lm $TRAIN_DIR/model.gz \
      $KNDISCOUNT $WBDISCOUNT \
      -write-vocab $TRAIN_DIR/vocab

    if [ $? == 0 ]; then
        break
    fi
done
fi
  
   
