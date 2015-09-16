#!/bin/bash

if [ -z "$1" ]; then
    echo "Provide a config file"
    exit
fi

./train_scripts/01-morfessor.sh $1
./train_scripts/02-ngram_count.sh $1
./train_scripts/03-prune.sh $1