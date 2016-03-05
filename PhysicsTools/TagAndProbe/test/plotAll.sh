#! /bin/bash

shopt -s nullglob

#./genSystText.py -n 2016_02_02_nominal -b 2016_02_05_expbkg -s 2016_03_02_param2b -m 2016_02_04_madgraph -t 2016_02_08_difftag &> syst_text.log
for file in $(ls -A eff_all_*.txt)
do
    python plotting/EGammaID_scaleFactors.py $file -b
done
