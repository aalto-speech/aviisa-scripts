#!/bin/bash

BASE_DIR=$(readlink -f $(dirname "$0"))/..

if [ -z "$1" ]; then
    echo "Provide a config file"
    exit
fi

. "$1"


echo $TEST_LM
echo $TEST_AM

TEST_LM=(${TEST_LM//:/ })
TEST_AM=(${TEST_AM//:/ })


function make_ler {
   cat $1 | sed "s/(.*$//" | sed "s/ /_/g" | sed "s/\w/& /g" | paste -d" " - $2 > $3
}

function encode {
    iconv -f UTF-8 -t $ONE_BYTE_ENCODING < $1 > $2
}


for AMDIR in ${TEST_AM[@]}; do
    for LMDIR in ${TEST_LM[@]}; do
        echo "AM " $AMDIR
        echo "LM " $LMDIR
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

        hyp_trn=$(grep "^Wrote" ${RESULTS_DIR}/log | sed "s/^Wrote //" | sed "s/\.$//")
#        hyp_trn=${RESULTS_DIR}/$(ls -t ${RESULTS_DIR} | grep -v log | grep -v sclite | head -n1)

        echo $hyp_trn

        mkdir -p ${RESULTS_DIR}/tmp

        grep -o "(.*$" $TEST_TRN > ${RESULTS_DIR}/tmp/namelist

        make_ler $hyp_trn ${RESULTS_DIR}/tmp/namelist ${RESULTS_DIR}/tmp/hyp_ler.trn
        make_ler $TEST_TRN ${RESULTS_DIR}/tmp/namelist ${RESULTS_DIR}/tmp/ref_ler.trn

        encode ${RESULTS_DIR}/tmp/hyp_ler.trn ${RESULTS_DIR}/tmp/hyp_ler.iso.trn
        encode ${RESULTS_DIR}/tmp/ref_ler.trn ${RESULTS_DIR}/tmp/ref_ler.iso.trn

        encode $hyp_trn ${RESULTS_DIR}/tmp/hyp_wer.iso.trn
        encode $TEST_TRN ${RESULTS_DIR}/tmp/ref_wer.iso.trn



        sclite -i wsj -f 0 -h ${RESULTS_DIR}/tmp/hyp_wer.iso.trn -r ${RESULTS_DIR}/tmp/ref_wer.iso.trn | tee ${hyp_trn}.sclite_wer
        sclite -i wsj -f 0 -h ${RESULTS_DIR}/tmp/hyp_ler.iso.trn -r ${RESULTS_DIR}/tmp/ref_ler.iso.trn | tee ${hyp_trn}.sclite_ler
    done
done
