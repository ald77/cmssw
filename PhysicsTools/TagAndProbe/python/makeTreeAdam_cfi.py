import FWCore.ParameterSet.Config as cms
from PhysicsTools.SelectorUtils.tools.vid_id_tools import *

def AddMiniIso(process, options):
    #Adds clones of objects managed by Matteo so that upstream changes propagate to mini iso objects
    process.ElectronIsolation =  cms.EDProducer("CITKPFIsolationSumProducer",
                                                srcToIsolate = cms.InputTag("slimmedElectrons"),
                                                srcForIsolationCone = cms.InputTag('packedPFCandidates'),
                                                isolationConeDefinitions = cms.VPSet(
            cms.PSet( isolationAlgo = cms.string('ElectronMiniIsolationWithConeVeto'),
                      coneSize = cms.double(0.2),
                      MinConeSize = cms.double(0.05),
                      ktScale = cms.double(10.),
                      VetoConeSizeEndcaps = cms.double(0.015),
                      VetoConeSizeBarrel = cms.double(0.0),
                      isolateAgainst = cms.string('h+'),
                      miniAODVertexCodes = cms.vuint32(2,3) ),
            cms.PSet( isolationAlgo = cms.string('ElectronMiniIsolationWithConeVeto'),
                      coneSize = cms.double(0.2),
                      MinConeSize = cms.double(0.05),
                      ktScale = cms.double(10.),
                      VetoConeSizeEndcaps = cms.double(0.0),
                      VetoConeSizeBarrel = cms.double(0.0),
                      isolateAgainst = cms.string('h0'),
                      miniAODVertexCodes = cms.vuint32(2,3) ),
            cms.PSet( isolationAlgo = cms.string('ElectronMiniIsolationWithConeVeto'),
                      coneSize = cms.double(0.2),
                      MinConeSize = cms.double(0.05),
                      ktScale = cms.double(10.),
                      VetoConeSizeEndcaps = cms.double(0.08),
                      VetoConeSizeBarrel = cms.double(0.0),
                      isolateAgainst = cms.string('gamma'),
                      miniAODVertexCodes = cms.vuint32(2,3) ),
            cms.PSet( isolationAlgo = cms.string('ElectronMiniIsolationWithConeVeto'),
                      coneSize = cms.double(0.2),
                      MinConeSize = cms.double(0.05),
                      ktScale = cms.double(10.),
                      ActivityConeSize = cms.double(0.4),
                      VetoConeSizeEndcaps = cms.double(0.015),
                      VetoConeSizeBarrel = cms.double(0.0),
                      isolateAgainst = cms.string('h+'),
                      miniAODVertexCodes = cms.vuint32(2,3) ),
            cms.PSet( isolationAlgo = cms.string('ElectronMiniIsolationWithConeVeto'),
                      coneSize = cms.double(0.2),
                      MinConeSize = cms.double(0.05),
                      ktScale = cms.double(10.),
                      ActivityConeSize = cms.double(0.4),
                      VetoConeSizeEndcaps = cms.double(0.0),
                      VetoConeSizeBarrel = cms.double(0.0),
                      isolateAgainst = cms.string('h0'),
                      miniAODVertexCodes = cms.vuint32(2,3) ),
            cms.PSet( isolationAlgo = cms.string('ElectronMiniIsolationWithConeVeto'),
                      coneSize = cms.double(0.2),
                      MinConeSize = cms.double(0.05),
                      ktScale = cms.double(10.),
                      ActivityConeSize = cms.double(0.4),
                      VetoConeSizeEndcaps = cms.double(0.08),
                      VetoConeSizeBarrel = cms.double(0.0),
                      isolateAgainst = cms.string('gamma'),
                      miniAODVertexCodes = cms.vuint32(2,3) ),
            )
                                                )

    MiniIsoProbeVars = cms.PSet(process.GsfElectronToRECO.variables,
                                probe_Ele_chMini = cms.InputTag("ElectronIsolation:h+-DR020-BarVeto000-EndVeto001-kt1000-Min005"),
                                probe_Ele_neuMini = cms.InputTag("ElectronIsolation:h0-DR020-BarVeto000-EndVeto000-kt1000-Min005"),
                                probe_Ele_phoMini = cms.InputTag("ElectronIsolation:gamma-DR020-BarVeto000-EndVeto008-kt1000-Min005"),
                                probe_Ele_chAct = cms.InputTag("ElectronIsolation:h+-DR020-BarVeto000-EndVeto001-kt1000-Min005-Act040"),
                                probe_Ele_neuAct = cms.InputTag("ElectronIsolation:h0-DR020-BarVeto000-EndVeto000-kt1000-Min005-Act040"),
                                probe_Ele_phoAct = cms.InputTag("ElectronIsolation:gamma-DR020-BarVeto000-EndVeto008-kt1000-Min005-Act040"),
                                probe_Ele_Act = cms.InputTag("activity:sum"),
                                probe_Ele_Mini = cms.InputTag("miniiso:sum"),
                                )

    setupAllVIDIdsInModule(process,
                           'RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_PHYS14_PU20bx25_Mini_V2_cff',
                           setupVIDElectronSelection)

    activity_pset = cms.PSet()
    for eleid in process.egmGsfElectronIDs.physicsObjectIDs:
        if eleid.idDefinition.idName == "cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-tight":
            for cut in eleid.idDefinition.cutFlow:
                if cut.cutName == "GsfEleEffAreaMiniIsoCut":
                    activity_pset = cut
    
    process.activity = cms.EDProducer("IsolationSum",
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

    process.miniiso =  cms.EDProducer("IsolationSum",
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

    process.goodElectronsPROBECutBasedMiniVeto = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedMiniVeto.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-veto")
    process.goodElectronsPROBECutBasedNoIsoVeto = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedNoIsoVeto.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-noiso-veto")
    process.goodElectronsPROBECutBasedMiniLoose = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedMiniLoose.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-loose")
    process.goodElectronsPROBECutBasedNoIsoLoose = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedNoIsoLoose.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-noiso-loose")
    process.goodElectronsPROBECutBasedMiniMedium = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedMiniMedium.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-medium")
    process.goodElectronsPROBECutBasedNoIsoMedium = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedNoIsoMedium.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-noiso-medium")
    process.goodElectronsPROBECutBasedMiniTight = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedMiniTight.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-tight")
    process.goodElectronsPROBECutBasedNoIsoTight = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedNoIsoTight.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-noiso-tight")

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
    process.goodElectronsProbeLooseNoIso = process.goodElectronsProbeVetoNoIso.clone()
    process.goodElectronsProbeLooseNoIso.inputs = cms.InputTag("goodElectronsPROBECutBasedNoIsoLoose")
    process.goodElectronsProbeMediumNoIso = process.goodElectronsProbeVetoNoIso.clone()
    process.goodElectronsProbeMediumNoIso.inputs = cms.InputTag("goodElectronsPROBECutBasedNoIsoMedium")
    process.goodElectronsProbeTightNoIso = process.goodElectronsProbeVetoNoIso.clone()
    process.goodElectronsProbeTightNoIso.inputs = cms.InputTag("goodElectronsPROBECutBasedNoIsoTight")

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

    if options["MC_FLAG"]:
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
    if (options['MC_FLAG']):
        process.p = cms.Path(
            process.hltHighLevel +
            process.ElectronIsolation +
            process.ele_sequence + 
            process.sc_sequence +
            ####process.GsfDRToNearestTau+
            process.allTagsAndProbes +
            process.pileupReweightingProducer +
            process.mc_sequence +
            process.eleVarHelper +
            process.activity +
            process.miniiso +
            process.tree_sequence
            )
    elif hasattr(process, 'eleVarHelper'):
        process.p = cms.Path(
            process.hltHighLevel +
            process.ElectronIsolation +
            process.ele_sequence + 
            process.sc_sequence +
            ####process.GsfDRToNearestTau+
            process.allTagsAndProbes +
            process.mc_sequence +
            process.eleVarHelper +
            process.activity +
            process.miniiso +
            process.tree_sequence
            )
    else:
        process.p = cms.Path(
            process.hltHighLevel +
            process.ElectronIsolation +
            process.ele_sequence + 
            process.sc_sequence +
            ####process.GsfDRToNearestTau+
            process.allTagsAndProbes +
            process.mc_sequence +
            process.activity +
            process.miniiso +
            process.tree_sequence
            )
