#!/bin/bash

#SBATCH --time=24:00:00 --mem-per-cpu=12000
#SBATCH -n1 -N1

echo $1

module load AaltoASR sctk

if [ -z "$1" ]; then
    echo "Provide a config file"
    exit
fi

./scripts/run.sh $1
