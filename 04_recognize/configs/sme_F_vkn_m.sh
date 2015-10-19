#!/bin/bash
export TEST_NAME="sme_F_vkn_m"
export TEST_DIR="$GROUP_DIR/p/sami/recog_tests/$TEST_NAME"


export TEST_LM_SCALES=25:30:35

export TEST_AM="$GROUP_DIR/p/sami/models/sme_F/hmm/sme_F_18.10.2015_22"

export TEST_LM="$GROUP_DIR/p/sami/lmmodels/sme_F_vkn_10g_m"


export TEST_TRN="$GROUP_DIR/p/sami/audio_data/sme_F/devel.trn"
export TEST_WAVLIST="$GROUP_DIR/p/sami/audio_data/sme_F/devel.scp"

export ONE_BYTE_ENCODING=ISO-8859-10
