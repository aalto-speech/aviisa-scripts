export TRAIN_NAME='saami_female'
export TRAIN_DIR="$GROUP_DIR/p/sami/models/$TRAIN_NAME"

export TRAIN_IM="$GROUP_DIR/u/jpleino1/saami2015/sami_ph/samiph2015a"

export TRAIN_RECIPE="$TRAIN_DIR/recipe"
export TRAIN_LEX="$TRAIN_DIR/train.lex"

export TRAIN_TRN="$GROUP_DIR/p/sami/uit-sme-F/train.trn"
export TRAIN_WAVLIST="$GROUP_DIR/p/sami/uit-sme-F/train.scp"

export TRAIN_GAUSSIANS=12000
export TRAIN_BATCHES=50
export TRAIN_CLUSTERS=5

export TRAIN_SCRIPTDIR="$GROUP_DIR/Modules/src/git/AaltoASR/aku/scripts"
export TRAIN_TIERULES="$TRAIN_SCRIPTDIR/sami_rules.txt";
export TRAIN_BINDIR="$GROUP_DIR/Modules/src/git/AaltoASR/build/aku"
