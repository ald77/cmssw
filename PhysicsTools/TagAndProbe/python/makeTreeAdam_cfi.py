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

    #Applies probe cuts and WP
    process.goodElectronsPROBECutBasedMiniVeto = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedMiniVeto.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-veto")
    process.goodElectronsPROBECutBasedNoIsoVeto = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedNoIsoVeto.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-veto")
    process.goodElectronsPROBECutBasedMiniLoose = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedMiniLoose.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-loose")
    process.goodElectronsPROBECutBasedNoIsoLoose = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedNoIsoLoose.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-loose")
    process.goodElectronsPROBECutBasedMiniMedium = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedMiniMedium.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-medium")
    process.goodElectronsPROBECutBasedNoIsoMedium = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedNoIsoMedium.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-medium")
    process.goodElectronsPROBECutBasedMiniTight = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedMiniTight.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-tight")
    process.goodElectronsPROBECutBasedNoIsoTight = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedNoIsoTight.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-tight")
    process.goodElectronsPROBEMVAVLooseFO = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMVAVLooseFO.selection = cms.InputTag("MyEleVars:passMVAVLooseFO");
    process.goodElectronsPROBEMVAVLoose = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMVAVLoose.selection = cms.InputTag("MyEleVars:passMVAVLoose");
    process.goodElectronsPROBEMVATight = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMVATight.selection = cms.InputTag("MyEleVars:passMVATight");

    #Applies trigger matching
    process.goodElectronsProbeVetoMini = process.goodElectronsTagHLT.clone()
    process.goodElectronsProbeVetoMini.isAND = cms.bool(False)
    process.goodElectronsProbeVetoMini.inputs = cms.InputTag("goodElectronsPROBECutBasedMiniVeto")
    process.goodElectronsProbeLooseMini = process.goodElectronsProbeVetoMini.clone()
    process.goodElectronsProbeLooseMini.inputs = cms.InputTag("goodElectronsPROBECutBasedMiniLoose")
    process.goodElectronsProbeMediumMini = process.goodElectronsProbeVetoMini.clone()
    process.goodElectronsProbeMediumMini.inputs = cms.InputTag("goodElectronsPROBECutBasedMiniMedium")
    process.goodElectronsProbeTightMini = process.goodElectronsProbeVetoMini.clone()
    process.goodElectronsProbeTightMini.inputs = cms.InputTag("goodElectronsPROBECutBasedMiniTight")
    process.goodElectronsProbeVetoNoIso = process.goodElectronsProbeVetoMini.clone()
    process.goodElectronsProbeVetoNoIso.inputs = cms.InputTag("goodElectronsPROBECutBasedNoIsoVeto")
    process.goodElectronsProbeLooseNoIso = process.goodElectronsProbeVetoMini.clone()
    process.goodElectronsProbeLooseNoIso.inputs = cms.InputTag("goodElectronsPROBECutBasedNoIsoLoose")
    process.goodElectronsProbeMediumNoIso = process.goodElectronsProbeVetoMini.clone()
    process.goodElectronsProbeMediumNoIso.inputs = cms.InputTag("goodElectronsPROBECutBasedNoIsoMedium")
    process.goodElectronsProbeTightNoIso = process.goodElectronsProbeVetoMini.clone()
    process.goodElectronsProbeTightNoIso.inputs = cms.InputTag("goodElectronsPROBECutBasedNoIsoTight")
    process.goodElectronsProbeMVAVLooseFO = process.goodElectronsProbeVetoMini.clone()
    process.goodElectronsProbeMVAVLooseFO.inputs = cms.InputTag("goodElectronsPROBEMVAVLooseFO")
    process.goodElectronsProbeMVAVLoose = process.goodElectronsProbeVetoMini.clone()
    process.goodElectronsProbeMVAVLoose.inputs = cms.InputTag("goodElectronsPROBEMVAVLoose")
    process.goodElectronsProbeMVATight = process.goodElectronsProbeVetoMini.clone()
    process.goodElectronsProbeMVATight.inputs = cms.InputTag("goodElectronsPROBEMVATight")

    process.ele_sequence += process.goodElectronsPROBECutBasedMiniVeto
    process.ele_sequence += process.goodElectronsPROBECutBasedMiniLoose
    process.ele_sequence += process.goodElectronsPROBECutBasedMiniMedium
    process.ele_sequence += process.goodElectronsPROBECutBasedMiniTight
    process.ele_sequence += process.goodElectronsPROBECutBasedNoIsoVeto
    process.ele_sequence += process.goodElectronsPROBECutBasedNoIsoLoose
    process.ele_sequence += process.goodElectronsPROBECutBasedNoIsoMedium
    process.ele_sequence += process.goodElectronsPROBECutBasedNoIsoTight
    process.ele_sequence += process.goodElectronsProbeVetoMini
    process.ele_sequence += process.goodElectronsProbeLooseMini
    process.ele_sequence += process.goodElectronsProbeMediumMini
    process.ele_sequence += process.goodElectronsProbeTightMini
    process.ele_sequence += process.goodElectronsProbeVetoNoIso
    process.ele_sequence += process.goodElectronsProbeLooseNoIso
    process.ele_sequence += process.goodElectronsProbeMediumNoIso
    process.ele_sequence += process.goodElectronsProbeTightNoIso

    process.my_ele_sequence = cms.Sequence()
    process.my_ele_sequence += process.goodElectronsPROBEMVAVLooseFO
    process.my_ele_sequence += process.goodElectronsProbeMVAVLooseFO
    process.my_ele_sequence += process.goodElectronsPROBEMVAVLoose
    process.my_ele_sequence += process.goodElectronsProbeMVAVLoose
    process.my_ele_sequence += process.goodElectronsPROBEMVATight
    process.my_ele_sequence += process.goodElectronsProbeMVATight

    process.tagTightID = process.tagTightRECO.clone()
    process.tagTightID.decay = cms.string("goodElectronsTagHLT@+ goodElectrons@-")
    process.tagTightMiniVeto = process.tagTightRECO.clone()
    process.tagTightMiniVeto.decay = cms.string("goodElectronsTagHLT@+ goodElectronsPROBECutBasedNoIsoVeto@-")
    process.tagTightMiniLoose = process.tagTightRECO.clone()
    process.tagTightMiniLoose.decay = cms.string("goodElectronsTagHLT@+ goodElectronsPROBECutBasedNoIsoLoose@-")
    process.tagTightMiniMedium = process.tagTightRECO.clone()
    process.tagTightMiniMedium.decay = cms.string("goodElectronsTagHLT@+ goodElectronsPROBECutBasedNoIsoMedium@-")
    process.tagTightMiniTight = process.tagTightRECO.clone()
    process.tagTightMiniTight.decay = cms.string("goodElectronsTagHLT@+ goodElectronsPROBECutBasedNoIsoTight@-")

    process.allTagsAndProbes *= process.tagTightID
    process.allTagsAndProbes *= process.tagTightMiniVeto
    process.allTagsAndProbes *= process.tagTightMiniLoose
    process.allTagsAndProbes *= process.tagTightMiniMedium
    process.allTagsAndProbes *= process.tagTightMiniTight

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
        passingMVAVLooseFO = cms.InputTag("goodElectronsPROBEMVAVLooseFO"),
        passingMVAVLoose = cms.InputTag("goodElectronsPROBEMVAVLoose"),
        passingMVATight = cms.InputTag("goodElectronsPROBEMVATight"),
        )
    process.GsfElectronToID.allProbes = cms.InputTag("goodElectronsProbeHLT")
    process.VetoElectronToIso = process.GsfElectronToRECO.clone()
    process.VetoElectronToIso.variables = MiniIsoProbeVars
    process.VetoElectronToIso.tagProbePairs = cms.InputTag("tagTightMiniVeto")
    process.VetoElectronToIso.flags = cms.PSet(
        passingMini = cms.InputTag("goodElectronsPROBECutBasedMiniVeto"),
        passingStandard = cms.InputTag("goodElectronsPROBECutBasedVeto"),
        )
    process.VetoElectronToIso.allProbes = cms.InputTag("goodElectronsProbeVetoNoIso")
    process.LooseElectronToIso = process.GsfElectronToRECO.clone()
    process.LooseElectronToIso.variables = MiniIsoProbeVars
    process.LooseElectronToIso.tagProbePairs = cms.InputTag("tagTightMiniLoose")
    process.LooseElectronToIso.flags = cms.PSet(
        passingMini = cms.InputTag("goodElectronsPROBECutBasedMiniLoose"),
        passingStandard = cms.InputTag("goodElectronsPROBECutBasedLoose"),
        )
    process.LooseElectronToIso.allProbes = cms.InputTag("goodElectronsProbeLooseNoIso")
    process.MediumElectronToIso = process.GsfElectronToRECO.clone()
    process.MediumElectronToIso.variables = MiniIsoProbeVars
    process.MediumElectronToIso.tagProbePairs = cms.InputTag("tagTightMiniMedium")
    process.MediumElectronToIso.flags = cms.PSet(
        passingMini = cms.InputTag("goodElectronsPROBECutBasedMiniMedium"),
        passingStandard = cms.InputTag("goodElectronsPROBECutBasedMedium"),
        )
    process.MediumElectronToIso.allProbes = cms.InputTag("goodElectronsProbeMediumNoIso")
    process.TightElectronToIso = process.GsfElectronToRECO.clone()
    process.TightElectronToIso.variables = MiniIsoProbeVars
    process.TightElectronToIso.tagProbePairs = cms.InputTag("tagTightMiniTight")
    process.TightElectronToIso.flags = cms.PSet(
        passingMini = cms.InputTag("goodElectronsPROBECutBasedMiniTight"),
        passingStandard = cms.InputTag("goodElectronsPROBECutBasedTight"),
        )
    process.TightElectronToIso.allProbes = cms.InputTag("goodElectronsProbeTightNoIso")

    if varOptions.isMC:
        process.GsfElectronToID.probeMatches = cms.InputTag("McMatchRECO")
        process.VetoElectronToIso.probeMatches = cms.InputTag("McMatchRECO")
        process.LooseElectronToIso.probeMatches = cms.InputTag("McMatchRECO")
        process.MediumElectronToIso.probeMatches = cms.InputTag("McMatchRECO")
        process.TightElectronToIso.probeMatches = cms.InputTag("McMatchRECO")

    process.tree_sequence *= process.GsfElectronToID
    process.tree_sequence *= process.VetoElectronToIso
    process.tree_sequence *= process.LooseElectronToIso
    process.tree_sequence *= process.MediumElectronToIso
    process.tree_sequence *= process.TightElectronToIso

    #Probably a better way to do this, but just copy for now to refresh paths and insert ElectronIsolation

    if varOptions.isMC:
        process.p = cms.Path(
            process.sampleInfo +
            process.hltFilter +
            process.ElectronIsolation +
            process.ele_sequence + 
            process.eleVarHelper +
            process.MyEleVars +
            process.my_ele_sequence + 
            process.sc_sequence +
            process.allTagsAndProbes +
            process.pileupReweightingProducer +
            process.mc_sequence +
            process.iso_sums +
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
            process.MyEleVars +
            process.my_ele_sequence + 
            process.sc_sequence +
            process.allTagsAndProbes +
            process.mc_sequence +
            process.iso_sums +
            process.tree_sequence
            )
