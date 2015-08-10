#!/bin/bash -e

BASE_DIR=$(readlink -f $(dirname "$0"))/..

if [ -z "$1" ]; then
    echo "Provide a config file"
    exit
fi

source "$1"


mkdir -p "$TRAIN_DIR/hmm"
feanorm -r "$TRAIN_RECIPE" -c "$TRAIN_IM.cfg" -M normalization -w "$TRAIN_DIR/hmm/init.cfg"
