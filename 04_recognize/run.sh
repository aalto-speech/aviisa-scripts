#!/bin/bash

#SBATCH --time=4:00:00 --mem-per-cpu=1000
#SBATCH -n1 -N1


module load AaltoASR sctk

if [ -z "$1" ]; then
    echo "Provide a config file"
    exit
fi

./scripts/run.sh $1
