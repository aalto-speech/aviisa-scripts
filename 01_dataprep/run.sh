#!/bin/bash
mkdir -p work
mkdir -p out

CUR_DIR=$(pwd)

if [ -z "$1" ]; then
    echo "Provide a directory with wav-files as first argument"
    exit
fi

if [ -z "$2" ]; then
    echo "Provide a directory with txt-files as second argument"
    exit
fi

if [ -z "$3" ]; then
    echo "Provide a model as third argument"
    exit
fi

WAV_DIR=$1
TXT_DIR=$2

MODEL=$3

LANGDAT_DIR=$4

RECIPE=work/recipe_$RANDOM
> $RECIPE

for txt in $(ls -1 $TXT_DIR/*.txt); do
    b=`basename $txt .txt`
    ./parse_transcripts.py $txt work/${b}.phn out/${b}.trn $LANGDAT_DIR
    echo "audio=${WAV_DIR}/${b}.wav transcript=work/${b}.phn alignment=work/${b}.aligned" >> $RECIPE
done

align -b $MODEL -c ${MODEL}.cfg -r $RECIPE --beam=2000 --sbeam=2000 --phoseg -i 1

for txt in $(ls -1 $TXT_DIR/*.txt); do
b=`basename $txt .txt`
./split_files.py work/${b}.aligned ${WAV_DIR}/${b}.wav out
done

mkdir realign
RECIPE=realign/recipe_$RANDOM



