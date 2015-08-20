export TRAIN_NAME='saami_male'
export TRAIN_DIR="$GROUP_DIR/p/sami/models/$TRAIN_NAME"
export TRAIN_ALIGN_DIR="$TRAIN_DIR/align"

export TRAIN_IM="$GROUP_DIR/p/saami2015/sami_ph/samiph2015a"

export TRAIN_RECIPE="$TRAIN_DIR/recipe"
export TRAIN_LEX="$TRAIN_DIR/train.lex"

export TRAIN_TRN="$GROUP_DIR/p/sami/uit-sme-M/train.trn"
export TRAIN_WAVLIST="$GROUP_DIR/p/sami/uit-sme-M/train.scp"

export TRAIN_GAUSSIANS=12000
export TRAIN_BATCHES=5
#export TRAIN_CLUSTERS=5

export TRAIN_SCRIPTDIR="$GROUP_DIR/Modules/src/git/AaltoASR/aku/scripts"
export TRAIN_TIERULES="$BASE_DIR/rules/sami.txt";
export TRAIN_BINDIR="$GROUP_DIR/Modules/src/git/AaltoASR/build/aku"
