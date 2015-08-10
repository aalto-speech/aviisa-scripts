#!/bin/bash 

BASE_DIR=$(readlink -f $(dirname "$0"))/..

if [ -z "$1" ]; then
    echo "Provide a config file"
    exit
fi

source "$1"

verify-train-files.py "$TRAIN_RECIPE" "$TRAIN_TRN" "$TRAIN_LEX" "$TRAIN_IM.ph"
