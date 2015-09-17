#!/bin/bash
export TEST_NAME="saamiF-morph-dev"
export TEST_DIR="$GROUP_DIR/p/sami/recog_tests/$TEST_NAME"


export TEST_LM_SCALES=20:25:30:35:40:45

export TEST_AM="$GROUP_DIR/p/sami/models/saami_female/hmm/saami_female_11.8.2015_22"

export TEST_LM="$GROUP_DIR/p/sami/lmmodels/saamiF_2gram_morph":"$GROUP_DIR/p/sami/lmmodels/saamiF_3gram_morph":"$GROUP_DIR/p/sami/lmmodels/saamiF_4gram_morph":"$GROUP_DIR/p/sami/lmmodels/saamiF_5gram_morph":"$GROUP_DIR/p/sami/lmmodels/saamiF_6gram_morph":"$GROUP_DIR/p/sami/lmmodels/saamiF_7gram_morph":"$GROUP_DIR/p/sami/lmmodels/saamiF_8gram_morph"


export TEST_TRN="$GROUP_DIR/p/sami/uit-sme-F/devel.trn"
export TEST_WAVLIST="$GROUP_DIR/p/sami/uit-sme-F/devel.scp"

export ONE_BYTE_ENCODING=ISO-8859-10
