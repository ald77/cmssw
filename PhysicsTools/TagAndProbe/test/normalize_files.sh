#! /bin/bash


cp current/TnPTree_data.root .
#cp current/TnPTree_mc.root .; python utilities/normalizeMCWeights.py -m TnPTree_mc.root -d TnPTree_data.root; mv *norm*.root current/TnPTree_mc_norm.root; rm -f TnPTree_mc*.root
cp current/TnPTree_madgraph.root .; python utilities/normalizeMCWeights.py -m TnPTree_madgraph.root -d TnPTree_data.root; mv *norm*.root current/TnPTree_madgraph_norm.root; rm -f TnPTree_madgraph*.root
cp current/TnPTree_powheg.root .; python utilities/normalizeMCWeights.py -m TnPTree_powheg.root -d TnPTree_data.root; mv *norm*.root current/TnPTree_powheg_norm.root; rm -f TnPTree_powheg*.root
cp current/TnPTree_powheg_mini.root .; python utilities/normalizeMCWeights.py -m TnPTree_powheg_mini.root -d TnPTree_data.root; mv *norm*.root current/TnPTree_powheg_mini_norm.root; rm -f TnPTree_powheg_mini*.root
cp current/TnPTree_amcatnlo.root .; python utilities/normalizeMCWeights.py -m TnPTree_amcatnlo.root -d TnPTree_data.root; mv *norm*.root current/TnPTree_amcatnlo_norm.root; rm -f TnPTree_amcatnlo*.root
rm -f *.root

cp current/TnPTree_data_difftag.root .
#cp current/TnPTree_mc_difftag.root .; python utilities/normalizeMCWeights.py -m TnPTree_mc_difftag.root -d TnPTree_data_difftag.root; mv *norm*.root current/TnPTree_mc_difftag_norm.root; rm -f TnPTree_mc*.root
cp current/TnPTree_madgraph_difftag.root .; python utilities/normalizeMCWeights.py -m TnPTree_madgraph_difftag.root -d TnPTree_data_difftag.root; mv *norm*.root current/TnPTree_madgraph_difftag_norm.root; rm -f TnPTree_madgraph*.root
cp current/TnPTree_powheg_difftag.root .; python utilities/normalizeMCWeights.py -m TnPTree_powheg_difftag.root -d TnPTree_data_difftag.root; mv *norm*.root current/TnPTree_powheg_difftag_norm.root; rm -f TnPTree_powheg*.root
cp current/TnPTree_powheg_mini_difftag.root .; python utilities/normalizeMCWeights.py -m TnPTree_powheg_mini_difftag.root -d TnPTree_data_difftag.root; mv *norm*.root current/TnPTree_powheg_mini_difftag_norm.root; rm -f TnPTree_powheg_mini*.root
cp current/TnPTree_amcatnlo_difftag.root .; python utilities/normalizeMCWeights.py -m TnPTree_amcatnlo_difftag.root -d TnPTree_data_difftag.root; mv *norm*.root current/TnPTree_amcatnlo_difftag_norm.root; rm -f TnPTree_amcatnlo*.root
rm -f *.root

