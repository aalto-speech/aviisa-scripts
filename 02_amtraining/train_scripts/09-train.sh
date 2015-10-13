#!/bin/bash -e

BASE_DIR=$(readlink -f $(dirname "$0"))/..

if [ -z "$1" ]; then
    echo "Provide a config file"
    exit
fi

source "$1"

export TRAIN_TIERULES=$LANGDAT_DIR/rules

"$BASE_DIR/base_scripts/train.pl"
