#! /bin/bash

python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToVeto.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingVeto --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,1.442,1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToLoose.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingLoose --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,1.442,1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToMedium.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMedium --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,1.442,1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToTight.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingTight --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,1.442,1.566,2.5 &

python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/VetoElectronToMini.root -d VetoElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,1.442,1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/LooseElectronToMini.root -d LooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,1.442,1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/MediumElectronToMini.root -d MediumElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,1.442,1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/TightElectronToMini.root -d TightElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,1.442,1.566,2.5 &

wait
