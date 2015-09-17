#!/bin/bash
export TEST_NAME="saamiM-word-dev"
export TEST_DIR="$GROUP_DIR/p/sami/recog_tests/$TEST_NAME"

export TEST_LM_SCALES=20:25:30:35:40:45

export TEST_AM="$GROUP_DIR/p/sami/models/saami_male/hmm/saami_male_11.8.2015_22"

export TEST_LM="$GROUP_DIR/p/sami/lmmodels/saamiM_2gram_word":"$GROUP_DIR/p/sami/lmmodels/saamiM_3gram_word":"$GROUP_DIR/p/sami/lmmodels/saamiM_4gram_word":"$GROUP_DIR/p/sami/lmmodels/saamiM_5gram_word":"$GROUP_DIR/p/sami/lmmodels/saamiM_6gram_word":"$GROUP_DIR/p/sami/lmmodels/saamiM_7gram_word":"$GROUP_DIR/p/sami/lmmodels/saamiM_8gram_word"


export TEST_TRN="$GROUP_DIR/p/sami/uit-sme-M/devel.trn"
export TEST_WAVLIST="$GROUP_DIR/p/sami/uit-sme-M/devel.scp"

export ONE_BYTE_ENCODING=ISO-8859-10
