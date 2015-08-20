#!/bin/bash

BASE_DIR=$(readlink -f $(dirname "$0"))/..

if [ -z "$1" ]; then
    echo "Provide a config file"
    exit
fi

source "$1"

for AMDIR in $TEST_AM; do
    for LMDIR in $TEST_LM; do
       export KEY=$(basename $AMDIR)/$(basename $LMDIR)
       export AM=$AMDIR
       export LM=$LMDIR/model_pruned
       export LOOKAHEAD_LM=$LMDIR/model_la
       export DICTIONARY=$LMDIR/vocab
       export FSA=1
       export BEAM=280
       export LM_SCALE=35
       export TOKEN_LIMIT=100000
       export AUDIO_LIST=$TEST_WAVLIST
       export RESULTS_DIR=$TEST_DIR/recognitions/${KEY}
       export RECOGNITIONS_DIR=$TEST_DIR/results/${KEY}
       export GENERATE_LATTICES=1

       mkdir -p $RESULTS_DIR
       recognize-batch.sh | tee ${RESULTS_DIR}/log
       hyp_trn=${RESULTS_DIR}/$(ls -t ${RESULTS_DIR} | grep -v log | head -n1)
       echo $hyp_trn
       ref2=$(mktemp)
       hyp2=$(mktemp)

       echo $ref2 $hyp2
       iconv -f UTF-8 -t ISO-8859-10 < $TEST_TRN > $ref2
       iconv -f UTF-8 -t ISO-8859-10 < $hyp_trn > $hyp2

       sclite -i wsj -f 0 -h $hyp2 -r $ref2 | tee ${hyp_trn}.sclite


       #rm $ref2 $hyp2



    done
done
