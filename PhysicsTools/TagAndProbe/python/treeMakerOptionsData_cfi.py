import FWCore.ParameterSet.Config as cms

options = dict()

options['MC_FLAG']             = cms.bool(False)
options['HLTProcessName']      = "HLT"
options['INPUT_FILE_NAME']     = cms.vstring("/store/relval/CMSSW_7_4_1/DoubleElectron/MINIAOD/GR_R_74_V12A_RelVal_zEl2012D-v1/00000/F4073AF3-85EC-E411-8117-0025905B8596.root")
options['OUTPUT_FILE_NAME']    = "TnPTree_Data.root"
options['ELECTRON_COLL']       = "slimmedElectrons"
options['ELECTRON_CUTS']       = "(abs(superCluster.eta)<2.5) && (ecalEnergy*sin(superClusterPosition.theta)>10.0)"
options['ELECTRON_TAG_CUTS']   = "(abs(superCluster.eta)<=2.5) && !(1.4442<=abs(superCluster.eta)<=1.566) && pt >= 25.0"
options['SUPERCLUSTER_COLL']   = "reducedEgamma:reducedSuperClusters"
options['SUPERCLUSTER_CUTS']   = "abs(eta)<2.5 && !(1.4442< abs(eta) <1.566) && et>10.0"
options['TnPPATHS']            = cms.vstring('HLT_Ele27_eta2p1_WPLoose_Gsf_v*')
options['TnPHLTTagFilters']    = cms.vstring("hltEle27WPLooseGsfTrackIsoFilter")
options['TnPHLTProbeFilters']  = cms.vstring("hltEle27WPLooseGsfTrackIsoFilter")#really want this off, but not sure how
options['HLTPathToMeasure']    = cms.vstring("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v15")
options['HLTFILTERTOMEASURE']  = cms.vstring("hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsoFilter")
options['GLOBALTAG']           = '74X_dataRun2_Prompt_v0'
options['EVENTSToPROCESS']     = cms.untracked.VEventRange()
options['MAXEVENTS']           = cms.untracked.int32(5000) 
options['useAOD']              = cms.bool(False)
options['DOTRIGGER']           = cms.bool(False)
options['DORECO']              = cms.bool(False)
options['DOID']                = cms.bool(True)
options['OUTPUTEDMFILENAME']   = 'edmFile.root'
options['DEBUG']               = cms.bool(False)

options['INPUT_FILE_NAME'] = cms.untracked.vstring(
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/096/00000/22D22D7F-5626-E511-BDE3-02163E011FAB.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/161/00000/7019DC27-9C26-E511-84FF-02163E011CC2.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/162/00000/9CC606D8-4127-E511-8F35-02163E013830.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/163/00000/9C435096-9F26-E511-A1D7-02163E012AB6.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/164/00000/4633CC68-A326-E511-95D0-02163E0124EA.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/167/00000/E661FBF2-A726-E511-8B8B-02163E01207C.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/168/00000/FCB6CB61-BC26-E511-8858-02163E01375B.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/244/00000/084C9A66-9227-E511-91E0-02163E0133F0.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/244/00000/12EE24E2-8F27-E511-80D1-02163E013793.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/251/00000/3A0E6309-8827-E511-B96D-02163E013432.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/252/00000/36D5A4A8-A227-E511-9AAA-02163E0135F3.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/252/00000/6258DF96-A227-E511-BE8A-02163E01259F.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/491/00000/4A5A5D00-C628-E511-ACC7-02163E01414A.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/493/00000/0C69AF3D-CF28-E511-B56A-02163E01414A.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/496/00000/3AA75CED-932C-E511-8248-02163E0133F2.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/497/00000/607EA0EA-E028-E511-BD54-02163E0133FF.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/498/00000/8064CCF6-ED28-E511-87D2-02163E014437.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/499/00000/70310B47-F728-E511-B2EF-02163E0118A2.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/500/00000/0273C876-0E29-E511-8B38-02163E012712.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/521/00000/D28AB765-6629-E511-8AAD-02163E0133D1.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/522/00000/805EB9CD-6129-E511-BF1C-02163E0129A3.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/548/00000/B6D08898-232A-E511-A833-02163E011DDE.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/559/00000/AA62F6DD-A62C-E511-A8EC-02163E013791.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/560/00000/BA599BB8-E129-E511-B26A-02163E0134CC.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/561/00000/5ACDA1DE-FB29-E511-8D8C-02163E0133B5.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/561/00000/CA80E14E-1E2A-E511-8C7D-02163E0122C2.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/562/00000/30DDF910-5E2A-E511-9F4D-02163E01206A.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/562/00000/3CE07240-742A-E511-BA88-02163E01258B.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/562/00000/5CF006D1-602A-E511-95CE-02163E0126E1.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/562/00000/8EE9BBAA-7E2A-E511-AEF7-02163E0143C0.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/562/00000/B41B8802-672A-E511-A9EA-02163E012787.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/562/00000/DCC900B5-972A-E511-9785-02163E012283.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/562/00000/F0A7C9F3-6B2A-E511-A73B-02163E0126A0.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/562/00000/FE5AD795-6E2A-E511-9C40-02163E012787.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/604/00000/AE22AF42-902A-E511-8A22-02163E012B30.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/612/00000/50DA7894-932A-E511-801E-02163E0136A2.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/628/00000/40EF63A0-B52A-E511-8B57-02163E0133F0.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/638/00000/0CDDB666-E72A-E511-9BFD-02163E011DE5.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/638/00000/B2FC1038-372B-E511-AA94-02163E013481.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/642/00000/2C622272-D02A-E511-9F20-02163E013645.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/643/00000/0E4B7E28-8D2C-E511-BFDA-02163E01477B.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/643/00000/1247CF12-932C-E511-B9ED-02163E01354D.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/643/00000/3A437BCB-912C-E511-96D0-02163E012934.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/643/00000/7077210E-8F2C-E511-97D5-02163E0138EC.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/643/00000/9EFCB7EB-C12C-E511-B8BB-02163E012158.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/643/00000/A42F5B12-9C2C-E511-AAB3-02163E0134C3.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/643/00000/C2E62796-942C-E511-8869-02163E0121A1.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/643/00000/CCA6600A-912C-E511-B1EF-02163E0133D0.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/643/00000/D84DA8FC-8F2C-E511-9B5A-02163E01420D.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/716/00000/02C46BE4-302C-E511-A01C-02163E0128BF.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/721/00000/9663EE89-022C-E511-985A-02163E01359E.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/721/00000/CADC920F-E02B-E511-BB9B-02163E01412F.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/781/00000/662647FF-9B2C-E511-85C5-02163E012965.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/883/00000/00CD59FD-2B2D-E511-8DB2-02163E01267F.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/883/00000/500D754A-292D-E511-AEBA-02163E0118F2.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/883/00000/CA2F0F5F-242D-E511-96AB-02163E011D88.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/883/00000/CAA3B776-312D-E511-923A-02163E01280D.root",
    "/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/883/00000/D030EA86-9C2D-E511-8FCB-02163E014181.root",
)
