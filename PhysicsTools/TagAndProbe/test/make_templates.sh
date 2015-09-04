#! /bin/bash

python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_id_norm.root -o ../data/GsfElectronToVeto.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=Veto --ptbins=10,20,30,40,50,200 --etabins=0,1.442,1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_id_norm.root -o ../data/GsfElectronToLoose.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=Loose --ptbins=10,20,30,40,50,200 --etabins=0,1.442,1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_id_norm.root -o ../data/GsfElectronToMedium.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=Medium --ptbins=10,20,30,40,50,200 --etabins=0,1.442,1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_id_norm.root -o ../data/GsfElectronToTight.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=Tight --ptbins=10,20,30,40,50,200 --etabins=0,1.442,1.566,2.5 &

python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_veto_norm.root -o ../data/VetoElectronToMini.root -d VetoElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=Mini --ptbins=10,20,30,40,50,200 --etabins=0,1.442,1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_loose_norm.root -o ../data/LooseElectronToMini.root -d LooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=Mini --ptbins=10,20,30,40,50,200 --etabins=0,1.442,1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_medium_norm.root -o ../data/MediumElectronToMini.root -d MediumElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=Mini --ptbins=10,20,30,40,50,200 --etabins=0,1.442,1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_tight_norm.root -o ../data/TightElectronToMini.root -d TightElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=Mini --ptbins=10,20,30,40,50,200 --etabins=0,1.442,1.566,2.5 &

wait
