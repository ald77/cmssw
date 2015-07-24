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
            )
                                                )

    setupAllVIDIdsInModule(process,
                           'RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_PHYS14_PU20bx25_Mini_V2_cff',
                           setupVIDElectronSelection)

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

    process.GsfElectronToID = process.GsfElectronToRECO.clone()
    process.GsfElectronToID.tagProbePairs = cms.InputTag("tagTightID")
    process.GsfElectronToID.flags = cms.PSet(
        passingVeto = cms.InputTag("goodElectronsPROBECutBasedNoIsoVeto"),
        passingLoose = cms.InputTag("goodElectronsPROBECutBasedNoIsoLoose"),
        passingMedium = cms.InputTag("goodElectronsPROBECutBasedNoIsoMedium"),
        passingTight = cms.InputTag("goodElectronsPROBECutBasedNoIsoTight"),
        )
    process.GsfElectronToID.allProbes = cms.InputTag("goodElectronsProbeHLT")
    process.VetoElectronToMiniIso = process.GsfElectronToRECO.clone()
    process.VetoElectronToMiniIso.tagProbePairs = cms.InputTag("tagTightMiniVeto")
    process.VetoElectronToMiniIso.flags = cms.PSet(
        passingVeto = cms.InputTag("goodElectronsPROBECutBasedMiniVeto")
        )
    process.VetoElectronToMiniIso.allProbes = cms.InputTag("goodElectronsProbeVetoNoIso")
    process.LooseElectronToMiniIso = process.GsfElectronToRECO.clone()
    process.LooseElectronToMiniIso.tagProbePairs = cms.InputTag("tagTightMiniLoose")
    process.LooseElectronToMiniIso.flags = cms.PSet(
        passingLoose = cms.InputTag("goodElectronsPROBECutBasedMiniLoose")
        )
    process.LooseElectronToMiniIso.allProbes = cms.InputTag("goodElectronsProbeLooseNoIso")
    process.MediumElectronToMiniIso = process.GsfElectronToRECO.clone()
    process.MediumElectronToMiniIso.tagProbePairs = cms.InputTag("tagTightMiniMedium")
    process.MediumElectronToMiniIso.flags = cms.PSet(
        passingMedium = cms.InputTag("goodElectronsPROBECutBasedMiniMedium")
        )
    process.MediumElectronToMiniIso.allProbes = cms.InputTag("goodElectronsProbeMediumNoIso")
    process.TightElectronToMiniIso = process.GsfElectronToRECO.clone()
    process.TightElectronToMiniIso.tagProbePairs = cms.InputTag("tagTightMiniTight")
    process.TightElectronToMiniIso.flags = cms.PSet(
        passingTight = cms.InputTag("goodElectronsPROBECutBasedMiniTight")
        )
    process.TightElectronToMiniIso.allProbes = cms.InputTag("goodElectronsProbeTightNoIso")

    if options["MC_FLAG"]:
        process.GsfElectronToID.probeMatches = cms.InputTag("McMatchRECO")
        process.VetoElectronToMiniIso.probeMatches = cms.InputTag("McMatchRECO")
        process.LooseElectronToMiniIso.probeMatches = cms.InputTag("McMatchRECO")
        process.MediumElectronToMiniIso.probeMatches = cms.InputTag("McMatchRECO")
        process.TightElectronToMiniIso.probeMatches = cms.InputTag("McMatchRECO")

    process.tree_sequence *= process.GsfElectronToID
    process.tree_sequence *= process.VetoElectronToMiniIso
    process.tree_sequence *= process.LooseElectronToMiniIso
    process.tree_sequence *= process.MediumElectronToMiniIso
    process.tree_sequence *= process.TightElectronToMiniIso

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
            process.tree_sequence
            )
