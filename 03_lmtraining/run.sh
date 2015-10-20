#!/bin/bash

#SBATCH --time=4:00:00 --mem-per-cpu=3000
#SBATCH -n1 -N1

echo $1

module load AaltoASR morfessor python variKN srilm

if [ -z "$1" ]; then
    echo "Provide a config file"
    exit
fi

./train_scripts/01-morfessor.sh $1
./train_scripts/02-ngram_count.sh $1
./train_scripts/03-prune.sh $1