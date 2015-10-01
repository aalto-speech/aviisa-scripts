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


varigram_kn -3 -C -a -Z -n 4 -o /triton/ics/project/puhe/c/sami_speech/morf_model/varigram_discount_data_25.txt /triton/ics/project/puhe/c/sami_speech/morf_model/varigram_lm_morf_25.txt /triton/elec/work/jpleino1/saami2015_BN_dev/dev_29/models/old_vk_lm4.lm

else

INTERPOLATE=$(seq 1 $NGRAM_ORDER | sed "s/^/-interpolate/" | tr "\n" " ")
KNDISCOUNT=$(seq 1 $NGRAM_ORDER | sed "s/^/-kndiscount/" | tr "\n" " ")


cat $TRAIN_DIR/lm_source_txt | \
ngram-count \
  -order $NGRAM_ORDER \
  $INTERPOLATE \
  -text - \
  -lm $TRAIN_DIR/model.gz \
  $KNDISCOUNT \
  -write-vocab $TRAIN_DIR/vocab

fi
  
   
