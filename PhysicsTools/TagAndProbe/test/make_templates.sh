#! /bin/bash

echo "Generating templates"

python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToVeto_crack.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingVeto --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToLoose_crack.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingLoose --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToMedium_crack.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMedium --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToTight_crack.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingTight --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToLoose2D_crack.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingLoose2D --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToFOID2D_crack.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingFOID2D --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToTight2D3D_crack.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingTight2D3D --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToTightID2D3D_crack.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingTightID2D3D --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=1.442,1.566 &

python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/MediumElectronToMini_crack.root -d MediumElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/MediumElectronToMini4_crack.root -d MediumElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini4 --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=1.442,1.566 &

python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/MVAVLooseElectronToMini_crack.root -d MVAVLooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/MVAVLooseElectronToMini4_crack.root -d MVAVLooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini4 --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/MVAVLooseElectronToConvIHit1_crack.root -d MVAVLooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingConvIHit1 --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=1.442,1.566 &

python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/MVATightElectronToConvIHit0Chg_crack.root -d MVATightElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingConvIHit0Chg --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=1.442,1.566 &

python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToVeto_alleta.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingVeto --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToLoose_alleta.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingLoose --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToMedium_alleta.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMedium --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToTight_alleta.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingTight --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToLoose2D_alleta.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingLoose2D --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToFOID2D_alleta.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingFOID2D --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToTight2D3D_alleta.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingTight2D3D --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/GsfElectronToTightID2D3D_alleta.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingTightID2D3D --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,2.5 &

python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/MediumElectronToMini_alleta.root -d MediumElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/MediumElectronToMini4_alleta.root -d MediumElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini4 --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,2.5 &

python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/MVAVLooseElectronToMini_alleta.root -d MVAVLooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/MVAVLooseElectronToMini4_alleta.root -d MVAVLooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini4 --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/MVAVLooseElectronToConvIHit1_alleta.root -d MVAVLooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingConvIHit1 --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,2.5 &

python MCTemplates/getTemplatesFromMC.py -i current/TnPTree_mc_norm.root -o ../data/MVATightElectronToConvIHit0Chg_alleta.root -d MVATightElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingConvIHit0Chg --var1Name=probe_Ele_et --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_eta --var2Bins=0,2.5 &

wait

echo "Generating config files"

python MCTemplates/makeConfigForTemplates.py -i Veto_crack -o ../python/commonFit_Veto_crack.py -t ../data/GsfElectronToVeto_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i Loose_crack -o ../python/commonFit_Loose_crack.py -t ../data/GsfElectronToLoose_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i Medium_crack -o ../python/commonFit_Medium_crack.py -t ../data/GsfElectronToMedium_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i Tight_crack -o ../python/commonFit_Tight_crack.py -t ../data/GsfElectronToTight_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i Loose2D_crack -o ../python/commonFit_Loose2D_crack.py -t ../data/GsfElectronToLoose2D_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i FOID2D_crack -o ../python/commonFit_FOID2D_crack.py -t ../data/GsfElectronToFOID2D_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i Tight2D3D_crack -o ../python/commonFit_Tight2D3D_crack.py -t ../data/GsfElectronToTight2D3D_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i TightID2D3D_crack -o ../python/commonFit_TightID2D3D_crack.py -t ../data/GsfElectronToTightID2D3D_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &

python MCTemplates/makeConfigForTemplates.py -i MediumMini_crack -o ../python/commonFit_MediumMini_crack.py -t ../data/MediumElectronToMini_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i MediumMini4_crack -o ../python/commonFit_MediumMini4_crack.py -t ../data/MediumElectronToMini4_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &

python MCTemplates/makeConfigForTemplates.py -i MVAVLooseMini_crack -o ../python/commonFit_MVAVLooseMini_crack.py -t ../data/MVAVLooseElectronToMini_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i MVAVLooseMini4_crack -o ../python/commonFit_MVAVLooseMini4_crack.py -t ../data/MVAVLooseElectronToMini4_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i MVAVLooseConvIHit1_crack -o ../python/commonFit_MVAVLooseConvIHit1_crack.py -t ../data/MVAVLooseElectronToConvIHit1_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &

python MCTemplates/makeConfigForTemplates.py -i MVATightConvIHit0Chg_crack -o ../python/commonFit_MVATightConvIHit0Chg_crack.py -t ../data/MVATightElectronToConvIHit0Chg_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &

python MCTemplates/makeConfigForTemplates.py -i Veto_alleta -o ../python/commonFit_Veto_alleta.py -t ../data/GsfElectronToVeto_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i Loose_alleta -o ../python/commonFit_Loose_alleta.py -t ../data/GsfElectronToLoose_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i Medium_alleta -o ../python/commonFit_Medium_alleta.py -t ../data/GsfElectronToMedium_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i Tight_alleta -o ../python/commonFit_Tight_alleta.py -t ../data/GsfElectronToTight_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i Loose2D_alleta -o ../python/commonFit_Loose2D_alleta.py -t ../data/GsfElectronToLoose2D_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i FOID2D_alleta -o ../python/commonFit_FOID2D_alleta.py -t ../data/GsfElectronToFOID2D_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i Tight2D3D_alleta -o ../python/commonFit_Tight2D3D_alleta.py -t ../data/GsfElectronToTight2D3D_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i TightID2D3D_alleta -o ../python/commonFit_TightID2D3D_alleta.py -t ../data/GsfElectronToTightID2D3D_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &

python MCTemplates/makeConfigForTemplates.py -i MediumMini_alleta -o ../python/commonFit_MediumMini_alleta.py -t ../data/MediumElectronToMini_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i MediumMini4_alleta -o ../python/commonFit_MediumMini4_alleta.py -t ../data/MediumElectronToMini4_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &

python MCTemplates/makeConfigForTemplates.py -i MVAVLooseMini_alleta -o ../python/commonFit_MVAVLooseMini_alleta.py -t ../data/MVAVLooseElectronToMini_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i MVAVLooseMini4_alleta -o ../python/commonFit_MVAVLooseMini4_alleta.py -t ../data/MVAVLooseElectronToMini4_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i MVAVLooseConvIHit1_alleta -o ../python/commonFit_MVAVLooseConvIHit1_alleta.py -t ../data/MVAVLooseElectronToConvIHit1_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &

python MCTemplates/makeConfigForTemplates.py -i MVATightConvIHit0Chg_alleta -o ../python/commonFit_MVATightConvIHit0Chg_alleta.py -t ../data/MVATightElectronToConvIHit0Chg_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &

wait

echo "Merging config files"

echo -e "import FWCore.ParameterSet.Config as cms\\n\\nall_pdfs = cms.PSet(" > ../python/commonFit.py

head --lines=-2 ../python/commonFit_Veto_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Loose_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Medium_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Tight_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Loose2D_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_FOID2D_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Tight2D3D_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_TightID2D3D_crack.py | tail --lines=+4  >> ../python/commonFit.py

head --lines=-2 ../python/commonFit_MediumMini_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MediumMini4_crack.py | tail --lines=+4  >> ../python/commonFit.py

head --lines=-2 ../python/commonFit_MVAVLooseMini_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVAVLooseMini4_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVAVLooseConvIHit1_crack.py | tail --lines=+4  >> ../python/commonFit.py

head --lines=-2 ../python/commonFit_MVATightConvIHit0Chg_crack.py | tail --lines=+4  >> ../python/commonFit.py

head --lines=-2 ../python/commonFit_Veto_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Loose_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Medium_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Tight_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Loose2D_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_FOID2D_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Tight2D3D_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_TightID2D3D_alleta.py | tail --lines=+4  >> ../python/commonFit.py

head --lines=-2 ../python/commonFit_MediumMini_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MediumMini4_alleta.py | tail --lines=+4  >> ../python/commonFit.py

head --lines=-2 ../python/commonFit_MVAVLooseMini_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVAVLooseMini4_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVAVLooseConvIHit1_alleta.py | tail --lines=+4  >> ../python/commonFit.py

head --lines=-2 ../python/commonFit_MVATightConvIHit0Chg_alleta.py | tail --lines=+4  >> ../python/commonFit.py

echo -e "\\n)" >> ../python/commonFit.py
