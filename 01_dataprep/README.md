How to use this
==============

Load AaltoASR on the path

    module load AaltoASR

and run with the source directories

    ./run.sh /teamwork/t40511_asr/c/uit-sme/16k/TTSF_alle/ /teamwork/t40511_asr/c/uit-sme/txt/TTSF_alle/
    ./run.sh /teamwork/t40511_asr/c/uit-sme/16k/TTSM_alle/ /teamwork/t40511_asr/c/uit-sme/txt/TTSM_alle/

wait a moment and you can find the resulting wav and trn files in out


You can also create a new corpus directory with a 75/15/10 split of train/dev/eval

    ./make_train_dev_eval.py out out 4 /teamwork/t40511_asr/p/sami/uit-sme-split

