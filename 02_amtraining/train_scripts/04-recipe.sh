#!/bin/bash

BASE_DIR=$(readlink -f $(dirname "$0"))/..

if [ -z "$1" ]; then
    echo "Provide a config file"
    exit
fi

source "$1"

ALIGN_DIR="$WORK_DIR/$TRAIN_NAME/align"

sed -r 's!^(.*)/([^/]*)\.(wav|FI0)$!audio=\1/\2.\3 transcript='"$ALIGN_DIR"'/\2.phn alignment='"$ALIGN_DIR"'/\2.phn hmmnet='"$ALIGN_DIR"'/\2.hmmnet utterance=\2!' \
"$TRAIN_WAVLIST" \
>"$TRAIN_RECIPE"
