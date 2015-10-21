import FWCore.ParameterSet.Config as cms
from PhysicsTools.SelectorUtils.tools.vid_id_tools import *

def AddMiniIso(process, options, varOptions):
    #Adds clones of objects managed by Matteo so that upstream changes propagate to mini iso objects
    process.ElectronIsolation =  cms.EDProducer(
        "CITKPFIsolationSumProducer",
        srcToIsolate = cms.InputTag("slimmedElectrons"),
        srcForIsolationCone = cms.InputTag('packedPFCandidates'),
        isolationConeDefinitions = cms.VPSet(
            cms.PSet(
                isolationAlgo = cms.string('ElectronMiniIsolationWithConeVeto'),
                coneSize = cms.double(0.2),
                MinConeSize = cms.double(0.05),
                ktScale = cms.double(10.),
                VetoConeSizeEndcaps = cms.double(0.015),
                VetoConeSizeBarrel = cms.double(0.0),
                isolateAgainst = cms.string('h+'),
                miniAODVertexCodes = cms.vuint32(2,3),
                ),
            cms.PSet(
                isolationAlgo = cms.string('ElectronMiniIsolationWithConeVeto'),
                coneSize = cms.double(0.2),
                MinConeSize = cms.double(0.05),
                ktScale = cms.double(10.),
                VetoConeSizeEndcaps = cms.double(0.0),
                VetoConeSizeBarrel = cms.double(0.0),
                isolateAgainst = cms.string('h0'),
                miniAODVertexCodes = cms.vuint32(2,3),
                ),
            cms.PSet(
                isolationAlgo = cms.string('ElectronMiniIsolationWithConeVeto'),
                coneSize = cms.double(0.2),
                MinConeSize = cms.double(0.05),
                ktScale = cms.double(10.),
                VetoConeSizeEndcaps = cms.double(0.08),
                VetoConeSizeBarrel = cms.double(0.0),
                isolateAgainst = cms.string('gamma'),
                miniAODVertexCodes = cms.vuint32(2,3),
                ),
            cms.PSet(
                isolationAlgo = cms.string('ElectronMiniIsolationWithConeVeto'),
                coneSize = cms.double(0.2),
                MinConeSize = cms.double(0.05),
                ktScale = cms.double(10.),
                ActivityConeSize = cms.double(0.4),
                VetoConeSizeEndcaps = cms.double(0.015),
                VetoConeSizeBarrel = cms.double(0.0),
                isolateAgainst = cms.string('h+'),
                miniAODVertexCodes = cms.vuint32(2,3),
                ),
            cms.PSet(
                isolationAlgo = cms.string('ElectronMiniIsolationWithConeVeto'),
                coneSize = cms.double(0.2),
                MinConeSize = cms.double(0.05),
                ktScale = cms.double(10.),
                ActivityConeSize = cms.double(0.4),
                VetoConeSizeEndcaps = cms.double(0.0),
                VetoConeSizeBarrel = cms.double(0.0),
                isolateAgainst = cms.string('h0'),
                miniAODVertexCodes = cms.vuint32(2,3),
                ),
            cms.PSet(
                isolationAlgo = cms.string('ElectronMiniIsolationWithConeVeto'),
                coneSize = cms.double(0.2),
                MinConeSize = cms.double(0.05),
                ktScale = cms.double(10.),
                ActivityConeSize = cms.double(0.4),
                VetoConeSizeEndcaps = cms.double(0.08),
                VetoConeSizeBarrel = cms.double(0.0),
                isolateAgainst = cms.string('gamma'),
                miniAODVertexCodes = cms.vuint32(2,3),
                ),
            ),
        )

    process.MyEleVars = cms.EDProducer(
        "MyElectronVariableHelper",
        probes = cms.InputTag(options['ELECTRON_COLL']),
        mvas = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        dxy = cms.InputTag("eleVarHelper:dxy"),
        dz = cms.InputTag("eleVarHelper:dz"),
        miniIso = cms.InputTag("relminiiso:sum")
        )

    MiniIsoProbeVars = cms.PSet(
        process.GsfElectronToRECO.variables,
        probe_ele_chMini = cms.InputTag("ElectronIsolation:h+-DR020-BarVeto000-EndVeto001-kt1000-Min005"),
        probe_ele_neuMini = cms.InputTag("ElectronIsolation:h0-DR020-BarVeto000-EndVeto000-kt1000-Min005"),
        probe_ele_phoMini = cms.InputTag("ElectronIsolation:gamma-DR020-BarVeto000-EndVeto008-kt1000-Min005"),
        probe_ele_chAct = cms.InputTag("ElectronIsolation:h+-DR020-BarVeto000-EndVeto001-kt1000-Min005-Act040"),
        probe_ele_neuAct = cms.InputTag("ElectronIsolation:h0-DR020-BarVeto000-EndVeto000-kt1000-Min005-Act040"),
        probe_ele_phoAct = cms.InputTag("ElectronIsolation:gamma-DR020-BarVeto000-EndVeto008-kt1000-Min005-Act040"),
        probe_ele_Act = cms.InputTag("absactivity:sum"),
        probe_ele_Mini = cms.InputTag("relminiiso:sum"),
        probe_ele_RelAct = cms.InputTag("relactivity:sum"),
        probe_ele_AbsMini = cms.InputTag("absminiiso:sum"),
        probe_ele_sip3d = cms.InputTag("MyEleVars:sip3d"),
        probe_ele_ecalIso = cms.InputTag("MyEleVars:ecalIso"),
        probe_ele_hcalIso = cms.InputTag("MyEleVars:hcalIso"),
        probe_ele_trackIso = cms.InputTag("MyEleVars:trackIso"),
        probe_ele_missIHits = cms.InputTag("MyEleVars:missIHits"),
        probe_ele_passConvVeto = cms.InputTag("MyEleVars:passConvVeto"),
        probe_ele_passMVAVLooseFO = cms.InputTag("MyEleVars:passMVAVLooseFO"),
        probe_ele_passMVAVLoose = cms.InputTag("MyEleVars:passMVAVLoose"),
        probe_ele_passMVATight = cms.InputTag("MyEleVars:passMVATight"),
        probe_ele_passTightIP2D = cms.InputTag("MyEleVars:passTightIP2D"),
        probe_ele_passTightIP3D = cms.InputTag("MyEleVars:passTightIP3D"),
        probe_ele_passIDEmu = cms.InputTag("MyEleVars:passIDEmu"),
        probe_ele_passISOEmu = cms.InputTag("MyEleVars:passISOEmu"),
        probe_ele_passCharge = cms.InputTag("MyEleVars:passCharge"),
        probe_ele_passIHit0 = cms.InputTag("MyEleVars:passIHit0"),
        probe_ele_passIHit1 = cms.InputTag("MyEleVars:passIHit1"),
        probe_ele_passLoose2D = cms.InputTag("MyEleVars:passLoose2D"),
        probe_ele_passFOID2D = cms.InputTag("MyEleVars:passFOID2D"),
        probe_ele_passTight2D3D = cms.InputTag("MyEleVars:passTight2D3D"),
        probe_ele_passTightID2D3D = cms.InputTag("MyEleVars:passTightID2D3D"),
        probe_ele_passConvIHit1 = cms.InputTag("MyEleVars:passConvIHit1"),
        probe_ele_passConvIHit0 = cms.InputTag("MyEleVars:passConvIHit0"),
        )

    setupAllVIDIdsInModule(process,
                           'RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Spring15_25ns_Mini_V1_cff',
                           setupVIDElectronSelection)

    activity_pset = cms.PSet()
    for eleid in process.egmGsfElectronIDs.physicsObjectIDs:
        if eleid.idDefinition.idName == "cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-tight":
            for cut in eleid.idDefinition.cutFlow:
                if cut.cutName == "GsfEleEffAreaMiniIsoCut":
                    activity_pset = cut
    
    process.absactivity = cms.EDProducer(
        "IsolationSum",
        effAreasConfigFile = activity_pset.effAreasConfigFile,
        probes = cms.InputTag("slimmedElectrons"),
        rho = activity_pset.rho,
        chadIso = cms.InputTag("ElectronIsolation:h+-DR020-BarVeto000-EndVeto001-kt1000-Min005-Act040"),
        nhadIso = cms.InputTag("ElectronIsolation:h0-DR020-BarVeto000-EndVeto000-kt1000-Min005-Act040"),
        phoIso = cms.InputTag("ElectronIsolation:gamma-DR020-BarVeto000-EndVeto008-kt1000-Min005-Act040"),
        minRadius = cms.double(0.05),
        maxRadius = cms.double(0.2),
        ktScale = cms.double(10.),
        actRadius = cms.double(0.4),
        isRelativeIso = cms.bool(False),
        )
    process.relactivity = cms.EDProducer(
        "IsolationSum",
        effAreasConfigFile = activity_pset.effAreasConfigFile,
        probes = cms.InputTag("slimmedElectrons"),
        rho = activity_pset.rho,
        chadIso = cms.InputTag("ElectronIsolation:h+-DR020-BarVeto000-EndVeto001-kt1000-Min005-Act040"),
        nhadIso = cms.InputTag("ElectronIsolation:h0-DR020-BarVeto000-EndVeto000-kt1000-Min005-Act040"),
        phoIso = cms.InputTag("ElectronIsolation:gamma-DR020-BarVeto000-EndVeto008-kt1000-Min005-Act040"),
        minRadius = cms.double(0.05),
        maxRadius = cms.double(0.2),
        ktScale = cms.double(10.),
        actRadius = cms.double(0.4),
        isRelativeIso = cms.bool(True),
        )
    process.absminiiso =  cms.EDProducer(
        "IsolationSum",
        effAreasConfigFile = activity_pset.effAreasConfigFile,
        probes = cms.InputTag("slimmedElectrons"),
        rho = activity_pset.rho,
        chadIso = cms.InputTag("ElectronIsolation:h+-DR020-BarVeto000-EndVeto001-kt1000-Min005"),
        nhadIso = cms.InputTag("ElectronIsolation:h0-DR020-BarVeto000-EndVeto000-kt1000-Min005"),
        phoIso = cms.InputTag("ElectronIsolation:gamma-DR020-BarVeto000-EndVeto008-kt1000-Min005"),
        minRadius = cms.double(0.05),
        maxRadius = cms.double(0.2),
        ktScale = cms.double(10.),
        isRelativeIso = cms.bool(False),
        )                                      
    process.relminiiso =  cms.EDProducer(
        "IsolationSum",
        effAreasConfigFile = activity_pset.effAreasConfigFile,
        probes = cms.InputTag("slimmedElectrons"),
        rho = activity_pset.rho,
        chadIso = cms.InputTag("ElectronIsolation:h+-DR020-BarVeto000-EndVeto001-kt1000-Min005"),
        nhadIso = cms.InputTag("ElectronIsolation:h0-DR020-BarVeto000-EndVeto000-kt1000-Min005"),
        phoIso = cms.InputTag("ElectronIsolation:gamma-DR020-BarVeto000-EndVeto008-kt1000-Min005"),
        minRadius = cms.double(0.05),
        maxRadius = cms.double(0.2),
        ktScale = cms.double(10.),
        isRelativeIso = cms.bool(True),
        )

    process.iso_sums = cms.Sequence(
        process.absactivity +
        process.relactivity +
        process.absminiiso +
        process.relminiiso
        )                                   

    #Applies probe cuts and WP (numerators and denominators both need to be listed here)
    process.goodElectronsPROBECutBasedNoIsoVeto = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedNoIsoVeto.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-veto")
    process.goodElectronsPROBECutBasedNoIsoLoose = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedNoIsoLoose.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-loose")
    process.goodElectronsPROBECutBasedNoIsoMedium = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedNoIsoMedium.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-medium")
    process.goodElectronsPROBECutBasedNoIsoTight = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedNoIsoTight.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-tight")
    process.goodElectronsPROBECutBasedMiniMedium = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedMiniMedium.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-medium")
    process.goodElectronsPROBECutBasedMini4Medium = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedMini4Medium.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini4-V1-standalone-medium")
    process.goodElectronsPROBEMVAVLooseFO = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMVAVLooseFO.selection = cms.InputTag("MyEleVars:passMVAVLooseFO")
    process.goodElectronsPROBEMVAVLoose = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMVAVLoose.selection = cms.InputTag("MyEleVars:passMVAVLoose")
    process.goodElectronsPROBEMVATight = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMVATight.selection = cms.InputTag("MyEleVars:passMVATight")
    process.goodElectronsPROBEMiniMVAVLoose = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMiniMVAVLoose.selection = cms.InputTag("MyEleVars:passMVAVLooseMini")
    process.goodElectronsPROBEMini4MVAVLoose = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMini4MVAVLoose.selection = cms.InputTag("MyEleVars:passMVAVLooseMini4")
    process.goodElectronsPROBELoose2D = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBELoose2D.selection = cms.InputTag("MyEleVars:passLoose2D")
    process.goodElectronsPROBEFOID2D = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEFOID2D.selection = cms.InputTag("MyEleVars:passFOID2D")
    process.goodElectronsPROBETight2D3D = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBETight2D3D.selection = cms.InputTag("MyEleVars:passTight2D3D")
    process.goodElectronsPROBETightID2D3D = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBETightID2D3D.selection = cms.InputTag("MyEleVars:passTightID2D3D")
    process.goodElectronsPROBEConvIHit1 = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEConvIHit1.selection = cms.InputTag("MyEleVars:passConvIHit1")
    process.goodElectronsPROBEConvIHit0Chg = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEConvIHit0Chg.selection = cms.InputTag("MyEleVars:passConvIHit0Chg")

    #Applies trigger matching (denominators need to be listed here)
    process.goodElectronsProbeMediumNoIso = process.goodElectronsTagHLT.clone()
    process.goodElectronsProbeMediumNoIso.isAND = cms.bool(False)
    process.goodElectronsProbeMediumNoIso.inputs = cms.InputTag("goodElectronsPROBECutBasedNoIsoMedium")
    process.goodElectronsProbeMVAVLoose = process.goodElectronsProbeMediumNoIso.clone()
    process.goodElectronsProbeMVAVLoose.inputs = cms.InputTag("goodElectronsPROBEMVAVLoose")
    process.goodElectronsProbeMVATight = process.goodElectronsProbeMediumNoIso.clone()
    process.goodElectronsProbeMVATight.inputs = cms.InputTag("goodElectronsPROBEMVATight")

    process.ele_sequence += process.goodElectronsPROBECutBasedNoIsoVeto
    process.ele_sequence += process.goodElectronsPROBECutBasedNoIsoLoose
    process.ele_sequence += process.goodElectronsPROBECutBasedNoIsoMedium
    process.ele_sequence += process.goodElectronsPROBECutBasedNoIsoTight
    process.ele_sequence += process.goodElectronsPROBECutBasedMiniMedium
    process.ele_sequence += process.goodElectronsPROBECutBasedMini4Medium
    process.ele_sequence += process.goodElectronsProbeMediumNoIso

    process.my_ele_sequence = cms.Sequence()
    process.my_ele_sequence += process.goodElectronsPROBEMVAVLooseFO
    process.my_ele_sequence += process.goodElectronsPROBEMVAVLoose
    process.my_ele_sequence += process.goodElectronsPROBEMVATight
    process.my_ele_sequence += process.goodElectronsPROBEMiniMVAVLoose
    process.my_ele_sequence += process.goodElectronsPROBEMini4MVAVLoose
    process.my_ele_sequence += process.goodElectronsPROBELoose2D
    process.my_ele_sequence += process.goodElectronsPROBEFOID2D
    process.my_ele_sequence += process.goodElectronsPROBETight2D3D
    process.my_ele_sequence += process.goodElectronsPROBETightID2D3D
    process.my_ele_sequence += process.goodElectronsPROBEConvIHit1
    process.my_ele_sequence += process.goodElectronsPROBEConvIHit0Chg
    process.my_ele_sequence += process.goodElectronsProbeMVAVLoose
    process.my_ele_sequence += process.goodElectronsProbeMVATight

    process.tagTightID = process.tagTightRECO.clone()
    process.tagTightID.decay = cms.string("goodElectronsTagHLT@+ goodElectrons@-")
    process.tagTightMiniMedium = process.tagTightRECO.clone()
    process.tagTightMiniMedium.decay = cms.string("goodElectronsTagHLT@+ goodElectronsPROBECutBasedNoIsoMedium@-")
    process.tagTightMiniMVAVLoose = process.tagTightRECO.clone()
    process.tagTightMiniMVAVLoose.decay = cms.string("goodElectronsTagHLT@+ goodElectronsPROBEMVAVLoose@-")
    process.tagTightMiniMVATight = process.tagTightRECO.clone()
    process.tagTightMiniMVATight.decay = cms.string("goodElectronsTagHLT@+ goodElectronsPROBEMVATight@-")

    process.allTagsAndProbes *= process.tagTightID
    process.allTagsAndProbes *= process.tagTightMiniMedium
    process.allTagsAndProbes *= process.tagTightMiniMVAVLoose
    process.allTagsAndProbes *= process.tagTightMiniMVATight

    process.GsfElectronToRECO.jetCollection = cms.InputTag("slimmedJets")
    process.GsfElectronToRECO.jet_pt_cut = cms.double(30.)
    process.GsfElectronToRECO.jet_eta_cut = cms.double(2.5)
    process.GsfElectronToRECO.match_delta_r = cms.double(0.3)

    process.GsfElectronToID = process.GsfElectronToRECO.clone()
    process.GsfElectronToID.variables = MiniIsoProbeVars
    process.GsfElectronToID.tagProbePairs = cms.InputTag("tagTightID")
    process.GsfElectronToID.flags = cms.PSet(
        passingVeto = cms.InputTag("goodElectronsPROBECutBasedNoIsoVeto"),
        passingLoose = cms.InputTag("goodElectronsPROBECutBasedNoIsoLoose"),
        passingMedium = cms.InputTag("goodElectronsPROBECutBasedNoIsoMedium"),
        passingTight = cms.InputTag("goodElectronsPROBECutBasedNoIsoTight"),
        passingLoose2D = cms.InputTag("goodElectronsPROBELoose2D"),
        passingFOID2D = cms.InputTag("goodElectronsPROBEFOID2D"),
        passingTight2D3D = cms.InputTag("goodElectronsPROBETight2D3D"),
        passingTightID2D3D = cms.InputTag("goodElectronsPROBETightID2D3D"),
        )
    process.GsfElectronToID.allProbes = cms.InputTag("goodElectronsProbeHLT")
    process.MediumElectronToIso = process.GsfElectronToRECO.clone()
    process.MediumElectronToIso.variables = MiniIsoProbeVars
    process.MediumElectronToIso.tagProbePairs = cms.InputTag("tagTightMiniMedium")
    process.MediumElectronToIso.flags = cms.PSet(
        passingMini = cms.InputTag("goodElectronsPROBECutBasedMiniMedium"),
        passingMini4 = cms.InputTag("goodElectronsPROBECutBasedMini4Medium"),
        passingConvIHit1 = cms.InputTag("goodElectronsPROBEConvIHit1"),
        passingConvIHit0Chg = cms.InputTag("goodElectronsPROBEConvIHit0Chg"),
        passingStandard = cms.InputTag("goodElectronsPROBECutBasedMedium"),
        )
    process.MediumElectronToIso.allProbes = cms.InputTag("goodElectronsProbeMediumNoIso")
    process.MVAVLooseElectronToIso = process.GsfElectronToRECO.clone()
    process.MVAVLooseElectronToIso.variables = MiniIsoProbeVars
    process.MVAVLooseElectronToIso.tagProbePairs = cms.InputTag("tagTightMiniMVAVLoose")
    process.MVAVLooseElectronToIso.flags = cms.PSet(
        passingMini = cms.InputTag("goodElectronsPROBEMiniMVAVLoose"),
        passingMini4 = cms.InputTag("goodElectronsPROBEMini4MVAVLoose"),
        passingConvIHit1 = cms.InputTag("goodElectronsPROBEConvIHit1"),
        passingConvIHit0Chg = cms.InputTag("goodElectronsPROBEConvIHit0Chg"),
        passingStandard = cms.InputTag("goodElectronsPROBEMVAVLoose"),
        )
    process.MVAVLooseElectronToIso.allProbes = cms.InputTag("goodElectronsProbeMVAVLoose")
    process.MVATightElectronToIso = process.GsfElectronToRECO.clone()
    process.MVATightElectronToIso.variables = MiniIsoProbeVars
    process.MVATightElectronToIso.tagProbePairs = cms.InputTag("tagTightMiniMVATight")
    process.MVATightElectronToIso.flags = cms.PSet(
        passingConvIHit1 = cms.InputTag("goodElectronsPROBEConvIHit1"),
        passingConvIHit0Chg = cms.InputTag("goodElectronsPROBEConvIHit0Chg"),
        passingStandard = cms.InputTag("goodElectronsPROBEMVATight"),
        )
    process.MVATightElectronToIso.allProbes = cms.InputTag("goodElectronsProbeMVATight")

    if varOptions.isMC:
        process.GsfElectronToID.probeMatches = cms.InputTag("McMatchRECO")
        process.MediumElectronToIso.probeMatches = cms.InputTag("McMatchRECO")

    process.tree_sequence *= process.GsfElectronToID
    process.tree_sequence *= process.MediumElectronToIso
    process.tree_sequence *= process.MVAVLooseElectronToIso
    process.tree_sequence *= process.MVATightElectronToIso

    #Probably a better way to do this, but just copy for now to refresh paths and insert ElectronIsolation

    if varOptions.isMC:
        process.p = cms.Path(
            process.sampleInfo +
            process.hltFilter +
            process.ElectronIsolation +
            process.ele_sequence + 
            process.eleVarHelper +
            process.iso_sums +
            process.MyEleVars +
            process.my_ele_sequence + 
            process.sc_sequence +
            process.allTagsAndProbes +
            process.pileupReweightingProducer +
            process.mc_sequence +
            process.GsfDRToNearestTauProbe + 
            process.GsfDRToNearestTauTag + 
            process.GsfDRToNearestTauSC + 
            process.tree_sequence
            )
    else:
        process.p = cms.Path(
            process.sampleInfo +
            process.hltFilter +
            process.ElectronIsolation +
            process.ele_sequence + 
            process.eleVarHelper +
            process.iso_sums +
            process.MyEleVars +
            process.my_ele_sequence + 
            process.sc_sequence +
            process.allTagsAndProbes +
            process.mc_sequence +
            process.tree_sequence
            )
