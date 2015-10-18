export TRAIN_NAME='fin_F_210m'
export TRAIN_DIR="$GROUP_DIR/p/sami/models/$TRAIN_NAME"
export TRAIN_ALIGN_DIR="$TRAIN_DIR/align"

export TRAIN_IM="$GROUP_DIR/p/sami/initial_models/fin_F_14.10.2015_22"

export TRAIN_RECIPE="$TRAIN_DIR/recipe"
export TRAIN_LEX="$TRAIN_DIR/train.lex"

export TRAIN_TRN="$GROUP_DIR/p/sami/audio_data/fin_F/train_12600.trn"
export TRAIN_WAVLIST="$GROUP_DIR/p/sami/audio_data/fin_F/train_12600.scp"

export TRAIN_GAUSSIANS=30000
export TRAIN_BATCHES=5
#export TRAIN_CLUSTERS=5

export TRAIN_SCRIPTDIR="$GROUP_DIR/Modules/src/git/AaltoASR/aku/scripts"
export LANGDAT_DIR="$GROUP_DIR/p/sami/langdata/fin";
export TRAIN_BINDIR="$GROUP_DIR/Modules/src/git/AaltoASR/build/aku"
