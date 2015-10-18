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


if [ -z "$4" ]; then
    echo "Provide a language directory as fourth argument"
    exit
fi


if [ -z "$5" ]; then
    echo "Provide a target directory as fifth argument"
    exit
fi

WAV_DIR=$1
TXT_DIR=$2

MODEL=$3

LANGDAT_DIR=$4

TARGET_DIR=$5

WD=work$RANDOM
mkdir -p $WD
mkdir -p $TARGET_DIR
RECIPE=$WD/recipe
> $RECIPE

for txt in $(ls -1 $TXT_DIR/*.txt); do
    b=`basename $txt .txt`
    ./parse_transcripts.py $txt $WD/${b}.phn $TARGET_DIR/${b}.trn $LANGDAT_DIR $6
    echo "audio=${WAV_DIR}/${b}.wav transcript=${WD}/${b}.phn alignment=${WD}/${b}.aligned" >> $RECIPE
done

for b in $(seq 1 8); do
align -B 8 -I $b -b $MODEL -c ${MODEL}.cfg -r $RECIPE --beam=10000 --sbeam=4000 --swins=2000 --phoseg -i 1 &
done
wait

for txt in $(ls -1 $TXT_DIR/*.txt); do
b=`basename $txt .txt`
./split_files.py ${WD}/${b}.aligned ${WAV_DIR}/${b}.wav $TARGET_DIR
done



