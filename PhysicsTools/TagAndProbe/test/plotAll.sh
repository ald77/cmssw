#! /bin/bash

shopt -s nullglob

./genSystText.py -n 2016_02_02_nominal -b 2016_02_05_expbkg -s 2016_02_25_param2 -m 2016_02_04_madgraph -t 2016_02_08_difftag
for file in $(ls -A eff_all_*.txt)
do
    python plotting/EGammaID_scaleFactors.py $file
done
