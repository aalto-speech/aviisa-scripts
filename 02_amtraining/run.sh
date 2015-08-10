#!/bin/bash

if [ -z "$1" ]; then
    echo "Provide a config file"
    exit
fi

./train_scripts/03-lex.sh $1
./train_scripts/04-recipe.sh $1
./train_scripts/05-verify.sh $1
./train_scripts/07-align.sh $1
./train_scripts/08-feanorm.sh $1
./train_scripts/09-train.sh $1
