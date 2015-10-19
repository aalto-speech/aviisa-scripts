#!/bin/bash

BASE_DIR=$(readlink -f $(dirname "$0"))/..

if [ -z "$1" ]; then
    echo "Provide a config file"
    exit
fi

source "$1"

mkdir -p $TRAIN_DIR

SOURCE_FILES=(${SOURCE_FILES//:/ })
echo ${SOURCE_FILES[@]}

if [ ! -z ${MORPH_TRAIN_OPTIONS+x} ]; then

    cat ${SOURCE_FILES[@]} | \
    sed 's/(.*$//' | \
    grep -v "[0-9\.]" | \
    morfessor-train $MORPH_TRAIN_OPTIONS -d ones -s $TRAIN_DIR/morfessor.bin -
    cat $SOURCE_FILES | \
    sed 's/(.*$//' | \
    morfessor-segment -l $TRAIN_DIR/morfessor.bin --output-format "{analysis} <w> " --output-newlines - > $TRAIN_DIR/lm_source_txt

else
    cat ${SOURCE_FILES[@]} | \
    sed 's/(.*$//' \
    grep -v "[0-9\.]" | \
    > $TRAIN_DIR/lm_source_txt

fi
