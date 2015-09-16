export TEST_NAME="first-recognition-dev"
export TEST_DIR="$GROUP_DIR/p/sami/recog_tests/$TEST_NAME"


export TEST_AM=(
"$GROUP_DIR/p/sami/models/saami_female/hmm/saami_female_11.8.2015_22"
)
export TEST_LM=(
"$GROUP_DIR/p/sami/lmmodels/saamif_3gram_word"
)

export TEST_TRN="$GROUP_DIR/p/sami/uit-sme-F/devel.trn"
export TEST_WAVLIST="$GROUP_DIR/p/sami/uit-sme-F/devel.scp"

export ONE_BYTE_ENCODING=ISO-8859-10