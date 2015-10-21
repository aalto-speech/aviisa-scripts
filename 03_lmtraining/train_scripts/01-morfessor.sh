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
if [ ! -f $TRAIN_DIR/morfessor.bin ]; then
    cat ${SOURCE_FILES[@]} | \
    sed 's/(.*$//' | \
    grep -v "[0-9\.]" | \
    ${BASE_DIR}/env_morfessor/bin/morfessor-train $MORPH_TRAIN_OPTIONS -d ones -s $TRAIN_DIR/morfessor.bin -
fi
    cat ${SOURCE_FILES[@]} | \
    sed 's/(.*$//' | \
    grep -v "[0-9\.]" | \
    ${BASE_DIR}/env_morfessor/bin/morfessor-segment -l $TRAIN_DIR/morfessor.bin --output-format "{analysis} <w> " --output-newlines - | \
    sed "s#^#<s> #" | sed 's#$# </s>#' > $TRAIN_DIR/lm_source_txt

else
    cat ${SOURCE_FILES[@]} | \
    sed 's/(.*$//' | \
    grep -v "[0-9\.]" | \
    sed "s#^#<s> #" | sed 's#$# </s>#' > $TRAIN_DIR/lm_source_txt

fi
