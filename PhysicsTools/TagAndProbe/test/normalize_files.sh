#! /bin/bash

cp current/TnPTree_mc.root .
cp current/TnPTree_data.root .

python utilities/normalizeMCWeights.py -m TnPTree_mc.root -d TnPTree_data.root; mv *norm*.root current/TnPTree_mc_norm.root;
#python utilities/normalizeMCWeights.py -m TnPTree_mc.root -d TnPTree_data.root -n; mv *norm*.root current/TnPTree_mc_norm.root;

rm -f *.root
