#! /bin/bash

mctype=mc
if [ "$#" -ge 1 ]
then
    mctype="$1"
fi

echo "Generating templates with extension $mctype"
file="current/TnPTree_""$mctype""_norm.root"

#All eta
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToVeto_alleta.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingVeto --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToLoose_alleta.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingLoose --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToMedium_alleta.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMedium --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToTight_alleta.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingTight --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToLoose2D_alleta.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingLoose2D --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToFOID2D_alleta.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingFOID2D --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToTight2D3D_alleta.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingTight2D3D --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToTightID2D3D_alleta.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingTightID2D3D --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,2.5 &

python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVAVLooseElectronToMini_alleta.root -d MVAVLooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVAVLooseElectronToMini4_alleta.root -d MVAVLooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini4 --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVAVLooseElectronToConvIHit1_alleta.root -d MVAVLooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingConvIHit1 --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,2.5 &

python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVATightElectronToConvIHit0Chg_alleta.root -d MVATightElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingConvIHit0Chg --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVATightElectronToMulti_alleta.root -d MVATightElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMultiIso --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVATightElectronToMultiEmu_alleta.root -d MVATightElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMultiIsoEmu --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,2.5 &

#Barrel
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToVeto_barrel.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingVeto --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,1.442 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToLoose_barrel.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingLoose --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,1.442 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToMedium_barrel.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMedium --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,1.442 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToTight_barrel.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingTight --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,1.442 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToLoose2D_barrel.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingLoose2D --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,1.442 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToFOID2D_barrel.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingFOID2D --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,1.442 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToTight2D3D_barrel.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingTight2D3D --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,1.442 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToTightID2D3D_barrel.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingTightID2D3D --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,1.442 &

python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVAVLooseElectronToMini_barrel.root -d MVAVLooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,1.442 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVAVLooseElectronToMini4_barrel.root -d MVAVLooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini4 --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,1.442 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVAVLooseElectronToConvIHit1_barrel.root -d MVAVLooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingConvIHit1 --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,1.442 &

python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVATightElectronToConvIHit0Chg_barrel.root -d MVATightElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingConvIHit0Chg --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,1.442 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVATightElectronToMulti_barrel.root -d MVATightElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMultiIso --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,1.442 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVATightElectronToMultiEmu_barrel.root -d MVATightElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMultiIsoEmu --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=0,1.442 &

#Crack
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToVeto_crack.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingVeto --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToLoose_crack.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingLoose --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToMedium_crack.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMedium --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToTight_crack.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingTight --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToLoose2D_crack.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingLoose2D --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToFOID2D_crack.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingFOID2D --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToTight2D3D_crack.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingTight2D3D --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToTightID2D3D_crack.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingTightID2D3D --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.442,1.566 &

python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVAVLooseElectronToMini_crack.root -d MVAVLooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVAVLooseElectronToMini4_crack.root -d MVAVLooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini4 --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVAVLooseElectronToConvIHit1_crack.root -d MVAVLooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingConvIHit1 --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.442,1.566 &

python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVATightElectronToConvIHit0Chg_crack.root -d MVATightElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingConvIHit0Chg --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVATightElectronToMulti_crack.root -d MVATightElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMultiIso --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.442,1.566 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVATightElectronToMultiEmu_crack.root -d MVATightElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMultiIsoEmu --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.442,1.566 &

#Endcap
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToVeto_endcap.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingVeto --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToLoose_endcap.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingLoose --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToMedium_endcap.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMedium --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToTight_endcap.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingTight --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToLoose2D_endcap.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingLoose2D --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToFOID2D_endcap.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingFOID2D --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToTight2D3D_endcap.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingTight2D3D --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/GsfElectronToTightID2D3D_endcap.root -d GsfElectronToID --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingTightID2D3D --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.566,2.5 &

python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVAVLooseElectronToMini_endcap.root -d MVAVLooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVAVLooseElectronToMini4_endcap.root -d MVAVLooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMini4 --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVAVLooseElectronToConvIHit1_endcap.root -d MVAVLooseElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingConvIHit1 --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.566,2.5 &

python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVATightElectronToConvIHit0Chg_endcap.root -d MVATightElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingConvIHit0Chg --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVATightElectronToMulti_endcap.root -d MVATightElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMultiIso --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.566,2.5 &
python MCTemplates/getTemplatesFromMC.py -i "$file" -o ../data/MVATightElectronToMultiEmu_endcap.root -d MVATightElectronToIso --probeTauVarName=probe_dRTau --tagTauVarName=tag_Ele_dRTau --idprobe=passingMultiIsoEmu --var1Name=probe_Ele_pt --var1Bins=10,20,30,40,50,200 --var2Name=probe_sc_abseta --var2Bins=1.566,2.5 &

wait

echo "Generating config files"

#All eta
python MCTemplates/makeConfigForTemplates.py -i Veto_alleta -o ../python/commonFit_Veto_alleta.py -t ../data/GsfElectronToVeto_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i Loose_alleta -o ../python/commonFit_Loose_alleta.py -t ../data/GsfElectronToLoose_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i Medium_alleta -o ../python/commonFit_Medium_alleta.py -t ../data/GsfElectronToMedium_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i Tight_alleta -o ../python/commonFit_Tight_alleta.py -t ../data/GsfElectronToTight_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i Loose2D_alleta -o ../python/commonFit_Loose2D_alleta.py -t ../data/GsfElectronToLoose2D_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i FOID2D_alleta -o ../python/commonFit_FOID2D_alleta.py -t ../data/GsfElectronToFOID2D_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i Tight2D3D_alleta -o ../python/commonFit_Tight2D3D_alleta.py -t ../data/GsfElectronToTight2D3D_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i TightID2D3D_alleta -o ../python/commonFit_TightID2D3D_alleta.py -t ../data/GsfElectronToTightID2D3D_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &

python MCTemplates/makeConfigForTemplates.py -i MVAVLooseMini_alleta -o ../python/commonFit_MVAVLooseMini_alleta.py -t ../data/MVAVLooseElectronToMini_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i MVAVLooseMini4_alleta -o ../python/commonFit_MVAVLooseMini4_alleta.py -t ../data/MVAVLooseElectronToMini4_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i MVAVLooseConvIHit1_alleta -o ../python/commonFit_MVAVLooseConvIHit1_alleta.py -t ../data/MVAVLooseElectronToConvIHit1_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &

python MCTemplates/makeConfigForTemplates.py -i MVATightConvIHit0Chg_alleta -o ../python/commonFit_MVATightConvIHit0Chg_alleta.py -t ../data/MVATightElectronToConvIHit0Chg_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i MVATightMulti_alleta -o ../python/commonFit_MVATightMulti_alleta.py -t ../data/MVATightElectronToMulti_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &
python MCTemplates/makeConfigForTemplates.py -i MVATightMultiEmu_alleta -o ../python/commonFit_MVATightMultiEmu_alleta.py -t ../data/MVATightElectronToMultiEmu_alleta.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,2.5 &

#Barrel
python MCTemplates/makeConfigForTemplates.py -i Veto_barrel -o ../python/commonFit_Veto_barrel.py -t ../data/GsfElectronToVeto_barrel.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,1.442 &
python MCTemplates/makeConfigForTemplates.py -i Loose_barrel -o ../python/commonFit_Loose_barrel.py -t ../data/GsfElectronToLoose_barrel.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,1.442 &
python MCTemplates/makeConfigForTemplates.py -i Medium_barrel -o ../python/commonFit_Medium_barrel.py -t ../data/GsfElectronToMedium_barrel.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,1.442 &
python MCTemplates/makeConfigForTemplates.py -i Tight_barrel -o ../python/commonFit_Tight_barrel.py -t ../data/GsfElectronToTight_barrel.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,1.442 &
python MCTemplates/makeConfigForTemplates.py -i Loose2D_barrel -o ../python/commonFit_Loose2D_barrel.py -t ../data/GsfElectronToLoose2D_barrel.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,1.442 &
python MCTemplates/makeConfigForTemplates.py -i FOID2D_barrel -o ../python/commonFit_FOID2D_barrel.py -t ../data/GsfElectronToFOID2D_barrel.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,1.442 &
python MCTemplates/makeConfigForTemplates.py -i Tight2D3D_barrel -o ../python/commonFit_Tight2D3D_barrel.py -t ../data/GsfElectronToTight2D3D_barrel.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,1.442 &
python MCTemplates/makeConfigForTemplates.py -i TightID2D3D_barrel -o ../python/commonFit_TightID2D3D_barrel.py -t ../data/GsfElectronToTightID2D3D_barrel.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,1.442 &

python MCTemplates/makeConfigForTemplates.py -i MVAVLooseMini_barrel -o ../python/commonFit_MVAVLooseMini_barrel.py -t ../data/MVAVLooseElectronToMini_barrel.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,1.442 &
python MCTemplates/makeConfigForTemplates.py -i MVAVLooseMini4_barrel -o ../python/commonFit_MVAVLooseMini4_barrel.py -t ../data/MVAVLooseElectronToMini4_barrel.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,1.442 &
python MCTemplates/makeConfigForTemplates.py -i MVAVLooseConvIHit1_barrel -o ../python/commonFit_MVAVLooseConvIHit1_barrel.py -t ../data/MVAVLooseElectronToConvIHit1_barrel.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,1.442 &

python MCTemplates/makeConfigForTemplates.py -i MVATightConvIHit0Chg_barrel -o ../python/commonFit_MVATightConvIHit0Chg_barrel.py -t ../data/MVATightElectronToConvIHit0Chg_barrel.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,1.442 &
python MCTemplates/makeConfigForTemplates.py -i MVATightMulti_barrel -o ../python/commonFit_MVATightMulti_barrel.py -t ../data/MVATightElectronToMulti_barrel.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,1.442 &
python MCTemplates/makeConfigForTemplates.py -i MVATightMultiEmu_barrel -o ../python/commonFit_MVATightMultiEmu_barrel.py -t ../data/MVATightElectronToMultiEmu_barrel.root --var1Bins=10,20,30,40,50,200 --var2Bins=0,1.442 &

#Crack
python MCTemplates/makeConfigForTemplates.py -i Veto_crack -o ../python/commonFit_Veto_crack.py -t ../data/GsfElectronToVeto_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i Loose_crack -o ../python/commonFit_Loose_crack.py -t ../data/GsfElectronToLoose_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i Medium_crack -o ../python/commonFit_Medium_crack.py -t ../data/GsfElectronToMedium_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i Tight_crack -o ../python/commonFit_Tight_crack.py -t ../data/GsfElectronToTight_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i Loose2D_crack -o ../python/commonFit_Loose2D_crack.py -t ../data/GsfElectronToLoose2D_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i FOID2D_crack -o ../python/commonFit_FOID2D_crack.py -t ../data/GsfElectronToFOID2D_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i Tight2D3D_crack -o ../python/commonFit_Tight2D3D_crack.py -t ../data/GsfElectronToTight2D3D_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i TightID2D3D_crack -o ../python/commonFit_TightID2D3D_crack.py -t ../data/GsfElectronToTightID2D3D_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &

python MCTemplates/makeConfigForTemplates.py -i MVAVLooseMini_crack -o ../python/commonFit_MVAVLooseMini_crack.py -t ../data/MVAVLooseElectronToMini_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i MVAVLooseMini4_crack -o ../python/commonFit_MVAVLooseMini4_crack.py -t ../data/MVAVLooseElectronToMini4_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i MVAVLooseConvIHit1_crack -o ../python/commonFit_MVAVLooseConvIHit1_crack.py -t ../data/MVAVLooseElectronToConvIHit1_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &

python MCTemplates/makeConfigForTemplates.py -i MVATightConvIHit0Chg_crack -o ../python/commonFit_MVATightConvIHit0Chg_crack.py -t ../data/MVATightElectronToConvIHit0Chg_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i MVATightMulti_crack -o ../python/commonFit_MVATightMulti_crack.py -t ../data/MVATightElectronToMulti_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &
python MCTemplates/makeConfigForTemplates.py -i MVATightMultiEmu_crack -o ../python/commonFit_MVATightMultiEmu_crack.py -t ../data/MVATightElectronToMultiEmu_crack.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.442,1.566 &

#Endcap
python MCTemplates/makeConfigForTemplates.py -i Veto_endcap -o ../python/commonFit_Veto_endcap.py -t ../data/GsfElectronToVeto_endcap.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.566,2.5 &
python MCTemplates/makeConfigForTemplates.py -i Loose_endcap -o ../python/commonFit_Loose_endcap.py -t ../data/GsfElectronToLoose_endcap.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.566,2.5 &
python MCTemplates/makeConfigForTemplates.py -i Medium_endcap -o ../python/commonFit_Medium_endcap.py -t ../data/GsfElectronToMedium_endcap.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.566,2.5 &
python MCTemplates/makeConfigForTemplates.py -i Tight_endcap -o ../python/commonFit_Tight_endcap.py -t ../data/GsfElectronToTight_endcap.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.566,2.5 &
python MCTemplates/makeConfigForTemplates.py -i Loose2D_endcap -o ../python/commonFit_Loose2D_endcap.py -t ../data/GsfElectronToLoose2D_endcap.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.566,2.5 &
python MCTemplates/makeConfigForTemplates.py -i FOID2D_endcap -o ../python/commonFit_FOID2D_endcap.py -t ../data/GsfElectronToFOID2D_endcap.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.566,2.5 &
python MCTemplates/makeConfigForTemplates.py -i Tight2D3D_endcap -o ../python/commonFit_Tight2D3D_endcap.py -t ../data/GsfElectronToTight2D3D_endcap.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.566,2.5 &
python MCTemplates/makeConfigForTemplates.py -i TightID2D3D_endcap -o ../python/commonFit_TightID2D3D_endcap.py -t ../data/GsfElectronToTightID2D3D_endcap.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.566,2.5 &

python MCTemplates/makeConfigForTemplates.py -i MVAVLooseMini_endcap -o ../python/commonFit_MVAVLooseMini_endcap.py -t ../data/MVAVLooseElectronToMini_endcap.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.566,2.5 &
python MCTemplates/makeConfigForTemplates.py -i MVAVLooseMini4_endcap -o ../python/commonFit_MVAVLooseMini4_endcap.py -t ../data/MVAVLooseElectronToMini4_endcap.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.566,2.5 &
python MCTemplates/makeConfigForTemplates.py -i MVAVLooseConvIHit1_endcap -o ../python/commonFit_MVAVLooseConvIHit1_endcap.py -t ../data/MVAVLooseElectronToConvIHit1_endcap.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.566,2.5 &

python MCTemplates/makeConfigForTemplates.py -i MVATightConvIHit0Chg_endcap -o ../python/commonFit_MVATightConvIHit0Chg_endcap.py -t ../data/MVATightElectronToConvIHit0Chg_endcap.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.566,2.5 &
python MCTemplates/makeConfigForTemplates.py -i MVATightMulti_endcap -o ../python/commonFit_MVATightMulti_endcap.py -t ../data/MVATightElectronToMulti_endcap.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.566,2.5 &
python MCTemplates/makeConfigForTemplates.py -i MVATightMultiEmu_endcap -o ../python/commonFit_MVATightMultiEmu_endcap.py -t ../data/MVATightElectronToMultiEmu_endcap.root --var1Bins=10,20,30,40,50,200 --var2Bins=1.566,2.5 &

wait

echo "Merging config files"

echo -e "import FWCore.ParameterSet.Config as cms\\n" > ../python/commonFit.py

#All eta
echo -e "alleta = cms.PSet(" >> ../python/commonFit.py

head --lines=-2 ../python/commonFit_Veto_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Loose_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Medium_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Tight_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Loose2D_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_FOID2D_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Tight2D3D_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_TightID2D3D_alleta.py | tail --lines=+4  >> ../python/commonFit.py

head --lines=-2 ../python/commonFit_MVAVLooseMini_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVAVLooseMini4_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVAVLooseConvIHit1_alleta.py | tail --lines=+4  >> ../python/commonFit.py

head --lines=-2 ../python/commonFit_MVATightConvIHit0Chg_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVATightMulti_alleta.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVATightMultiEmu_alleta.py | tail --lines=+4  >> ../python/commonFit.py

echo -e ")"\\n >> ../python/commonFit.py

#Barrel
echo -e "barrel = cms.PSet(" >> ../python/commonFit.py

head --lines=-2 ../python/commonFit_Veto_barrel.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Loose_barrel.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Medium_barrel.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Tight_barrel.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Loose2D_barrel.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_FOID2D_barrel.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Tight2D3D_barrel.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_TightID2D3D_barrel.py | tail --lines=+4  >> ../python/commonFit.py

head --lines=-2 ../python/commonFit_MVAVLooseMini_barrel.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVAVLooseMini4_barrel.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVAVLooseConvIHit1_barrel.py | tail --lines=+4  >> ../python/commonFit.py

head --lines=-2 ../python/commonFit_MVATightConvIHit0Chg_barrel.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVATightMulti_barrel.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVATightMultiEmu_barrel.py | tail --lines=+4  >> ../python/commonFit.py

echo -e ")\\n" >> ../python/commonFit.py

#Crack
echo -e "crack = cms.PSet(" >> ../python/commonFit.py

head --lines=-2 ../python/commonFit_Veto_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Loose_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Medium_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Tight_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Loose2D_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_FOID2D_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Tight2D3D_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_TightID2D3D_crack.py | tail --lines=+4  >> ../python/commonFit.py

head --lines=-2 ../python/commonFit_MVAVLooseMini_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVAVLooseMini4_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVAVLooseConvIHit1_crack.py | tail --lines=+4  >> ../python/commonFit.py

head --lines=-2 ../python/commonFit_MVATightConvIHit0Chg_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVATightMulti_crack.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVATightMultiEmu_crack.py | tail --lines=+4  >> ../python/commonFit.py

echo -e ")\\n" >> ../python/commonFit.py

#Endcap
echo -e "endcap = cms.PSet(" >> ../python/commonFit.py

head --lines=-2 ../python/commonFit_Veto_endcap.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Loose_endcap.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Medium_endcap.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Tight_endcap.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Loose2D_endcap.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_FOID2D_endcap.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_Tight2D3D_endcap.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_TightID2D3D_endcap.py | tail --lines=+4  >> ../python/commonFit.py

head --lines=-2 ../python/commonFit_MVAVLooseMini_endcap.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVAVLooseMini4_endcap.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVAVLooseConvIHit1_endcap.py | tail --lines=+4  >> ../python/commonFit.py

head --lines=-2 ../python/commonFit_MVATightConvIHit0Chg_endcap.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVATightMulti_endcap.py | tail --lines=+4  >> ../python/commonFit.py
head --lines=-2 ../python/commonFit_MVATightMultiEmu_endcap.py | tail --lines=+4  >> ../python/commonFit.py

echo -e ")\\n" >> ../python/commonFit.py

#Merge
echo -e "all_pdfs = cms.PSet(" >> ../python/commonFit.py
echo -e "  alleta," >> ../python/commonFit.py
echo -e "  barrel," >> ../python/commonFit.py
echo -e "  crack," >> ../python/commonFit.py
echo -e "  endcap," >> ../python/commonFit.py
echo -e ")" >> ../python/commonFit.py

#Cleanup
rm -f ../python/commonFit_*_*.py
