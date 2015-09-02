#! /bin/bash

cp current/*mc*.root .

python utilities/normalizeMCWeights.py -i TnPTree_mc_neg.root -d GsfElectronToID; mv *norm*.root current/TnPTree_id_norm.root;
python utilities/normalizeMCWeights.py -i TnPTree_mc_neg.root -d VetoElectronToIso; mv *norm*.root current/TnPTree_veto_norm.root;
python utilities/normalizeMCWeights.py -i TnPTree_mc_neg.root -d LooseElectronToIso; mv *norm*.root current/TnPTree_loose_norm.root;
python utilities/normalizeMCWeights.py -i TnPTree_mc_neg.root -d MediumElectronToIso; mv *norm*.root current/TnPTree_medium_norm.root;
python utilities/normalizeMCWeights.py -i TnPTree_mc_neg.root -d TightElectronToIso; mv *norm*.root current/TnPTree_tight_norm.root;

rm *.root