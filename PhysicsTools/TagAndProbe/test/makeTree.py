import FWCore.ParameterSet.Config as cms
import sys

from PhysicsTools.TagAndProbe.treeMakerOptionsMC_cfi import options
#from PhysicsTools.TagAndProbe.treeMakerOptionsData_cfi import options

process = cms.Process("tnp")

process.pileupReweightingProducer = cms.EDProducer("PileupWeightProducer",
                                                   FirstTime = cms.untracked.bool(True)
                                                   )

process.load('HLTrigger.HLTfilters.hltHighLevel_cfi')
process.hltHighLevel.throw = cms.bool(True)
process.hltHighLevel.HLTPaths = options['TnPPATHS']

###################################################################
##    ___            _           _      
##   |_ _|_ __   ___| |_   _  __| | ___ 
##    | || '_ \ / __| | | | |/ _` |/ _ \
##    | || | | | (__| | |_| | (_| |  __/
##   |___|_| |_|\___|_|\__,_|\__,_|\___|
##
###################################################################

process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.EventContent.EventContent_cff')

process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag.globaltag = options['GLOBALTAG']

process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )

process.MessageLogger.cerr.threshold = ''
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

###################################################################
##   ____             _ ____ 
##  |  _ \ ___   ___ | / ___|  ___  _   _ _ __ ___ ___ 
##  | |_) / _ \ / _ \| \___ \ / _ \| | | | '__/ __/ _ \
##  |  __/ (_) | (_) | |___) | (_) | |_| | | | (_|  __/
##  |_|   \___/ \___/|_|____/ \___/ \__,_|_|  \___\___|
##  
###################################################################

process.source = cms.Source("PoolSource",
                            fileNames = options['INPUT_FILE_NAME'],
                            eventsToProcess = options['EVENTSToPROCESS']
                            )

process.maxEvents = cms.untracked.PSet( input = options['MAXEVENTS'])
    
###################################################################
##  _____ _           _                     ___           _       _   _             
## | ____| | ___  ___| |_ _ __ ___  _ __   |_ _|___  ___ | | __ _| |_(_) ___  _ __  
## |  _| | |/ _ \/ __| __| '__/ _ \| '_ \   | |/ __|/ _ \| |/ _` | __| |/ _ \| '_ \ 
## | |___| |  __/ (__| |_| | | (_) | | | |  | |\__ \ (_) | | (_| | |_| | (_) | | | |
## |_____|_|\___|\___|\__|_|  \___/|_| |_| |___|___/\___/|_|\__,_|\__|_|\___/|_| |_|
###################################################################

process.ElectronIsolation =  cms.EDProducer("CITKPFIsolationSumProducer",
                                            srcToIsolate = cms.InputTag("slimmedElectrons"),
                                            srcForIsolationCone = cms.InputTag('packedPFCandidates'),
                                            isolationConeDefinitions = cms.VPSet(
        cms.PSet( isolationAlgo = cms.string('ElectronPFIsolationWithConeVeto'),
                  coneSize = cms.double(0.3),
                  VetoConeSizeEndcaps = cms.double(0.015),
                  VetoConeSizeBarrel = cms.double(0.0),
                  isolateAgainst = cms.string('h+'),
                  miniAODVertexCodes = cms.vuint32(2,3) ),
        cms.PSet( isolationAlgo = cms.string('ElectronPFIsolationWithConeVeto'),
                  coneSize = cms.double(0.3),
                  VetoConeSizeEndcaps = cms.double(0.0),
                  VetoConeSizeBarrel = cms.double(0.0),
                  isolateAgainst = cms.string('h0'),
                  miniAODVertexCodes = cms.vuint32(2,3) ),
        cms.PSet( isolationAlgo = cms.string('ElectronPFIsolationWithConeVeto'),
                  coneSize = cms.double(0.3),
                  VetoConeSizeEndcaps = cms.double(0.08),
                  VetoConeSizeBarrel = cms.double(0.0),
                  isolateAgainst = cms.string('gamma'),
                  miniAODVertexCodes = cms.vuint32(2,3) ),
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

###################################################################

###################################################################
##    ____      __ _____ _           _                   
##   / ___|___ / _| ____| | ___  ___| |_ _ __ ___  _ __  
##  | |  _/ __| |_|  _| | |/ _ \/ __| __| '__/ _ \| '_ \ 
##  | |_| \__ \  _| |___| |  __/ (__| |_| | | (_) | | | |
##   \____|___/_| |_____|_|\___|\___|\__|_|  \___/|_| |_|
##  
###################################################################

process.goodElectrons = cms.EDFilter("PATElectronRefSelector",
                                     src = cms.InputTag(options['ELECTRON_COLL']),
                                     cut = cms.string(options['ELECTRON_CUTS'])    
                                     )

###################################################################
##   ____                         ____ _           _            
##  / ___| _   _ _ __   ___ _ __ / ___| |_   _ ___| |_ ___ _ __ 
##  \___ \| | | | '_ \ / _ \ '__| |   | | | | / __| __/ _ \ '__|
##   ___) | |_| | |_) |  __/ |  | |___| | |_| \__ \ ||  __/ |   
##  |____/ \__,_| .__/ \___|_|   \____|_|\__,_|___/\__\___|_|   
##  
###################################################################

process.superClusterCands = cms.EDProducer("ConcreteEcalCandidateProducer",
                                           src = cms.InputTag(options['SUPERCLUSTER_COLL']),
                                           particleType = cms.int32(11),
                                           )

process.goodSuperClusters = cms.EDFilter("RecoEcalCandidateRefSelector",
                                         src = cms.InputTag("superClusterCands"),
                                         cut = cms.string(options['SUPERCLUSTER_CUTS']),
                                         filter = cms.bool(True)
                                         )                                         

process.GsfMatchedSuperClusterCands = cms.EDProducer("ElectronMatchedCandidateProducer",
                                                     src     = cms.InputTag("superClusterCands"),
                                                     ReferenceElectronCollection = cms.untracked.InputTag("goodElectrons"),
                                                     deltaR =  cms.untracked.double(0.3),
                                                     cut = cms.string(options['SUPERCLUSTER_CUTS'])
                                                     )

###################################################################
##    _____ _           _                     ___    _ 
##   | ____| | ___  ___| |_ _ __ ___  _ __   |_ _|__| |
##   |  _| | |/ _ \/ __| __| '__/ _ \| '_ \   | |/ _` |
##   | |___| |  __/ (__| |_| | | (_) | | | |  | | (_| |
##   |_____|_|\___|\___|\__|_|  \___/|_| |_| |___\__,_|
##   
###################################################################

from PhysicsTools.SelectorUtils.tools.vid_id_tools import *

dataFormat = DataFormat.MiniAOD
if (options['useAOD']):
    dataFormat = DataFormat.AOD

switchOnVIDElectronIdProducer(process, dataFormat)

# define which IDs we want to produce
my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_PHYS14_PU20bx25_V2_cff',
                 'RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_PHYS14_PU20bx25_Mini_V2_cff',
                 'RecoEgamma.ElectronIdentification.Identification.heepElectronID_HEEPV51_cff']

for idmod in my_id_modules:
    setupAllVIDIdsInModule(process, idmod, setupVIDElectronSelection)

process.goodElectronsPROBECutBasedVeto = cms.EDProducer("PatElectronSelectorByValueMap",
                                                        input     = cms.InputTag("goodElectrons"), #options['ELECTRON_COLL']),
                                                        cut       = cms.string(options['ELECTRON_CUTS']),
                                                        selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-V2-standalone-veto"),
                                                        id_cut    = cms.bool(True)
                                                        )

process.goodElectronsPROBECutBasedMiniVeto = process.goodElectronsPROBECutBasedVeto.clone()
process.goodElectronsPROBECutBasedMiniVeto.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-veto")
process.goodElectronsPROBECutBasedNoIsoVeto = process.goodElectronsPROBECutBasedVeto.clone()
process.goodElectronsPROBECutBasedNoIsoVeto.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-noiso-veto")
process.goodElectronsPROBECutBasedLoose = process.goodElectronsPROBECutBasedVeto.clone()
process.goodElectronsPROBECutBasedLoose.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-V2-standalone-loose")
process.goodElectronsPROBECutBasedMiniLoose = process.goodElectronsPROBECutBasedVeto.clone()
process.goodElectronsPROBECutBasedMiniLoose.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-loose")
process.goodElectronsPROBECutBasedNoIsoLoose = process.goodElectronsPROBECutBasedVeto.clone()
process.goodElectronsPROBECutBasedNoIsoLoose.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-noiso-loose")
process.goodElectronsPROBECutBasedMedium = process.goodElectronsPROBECutBasedVeto.clone()
process.goodElectronsPROBECutBasedMedium.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-V2-standalone-medium")
process.goodElectronsPROBECutBasedMiniMedium = process.goodElectronsPROBECutBasedVeto.clone()
process.goodElectronsPROBECutBasedMiniMedium.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-medium")
process.goodElectronsPROBECutBasedNoIsoMedium = process.goodElectronsPROBECutBasedVeto.clone()
process.goodElectronsPROBECutBasedNoIsoMedium.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-noiso-medium")
process.goodElectronsPROBECutBasedTight = process.goodElectronsPROBECutBasedVeto.clone()
process.goodElectronsPROBECutBasedTight.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-V2-standalone-tight")
process.goodElectronsPROBECutBasedMiniTight = process.goodElectronsPROBECutBasedVeto.clone()
process.goodElectronsPROBECutBasedMiniTight.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-tight")
process.goodElectronsPROBECutBasedNoIsoTight = process.goodElectronsPROBECutBasedVeto.clone()
process.goodElectronsPROBECutBasedNoIsoTight.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-noiso-tight")

process.goodElectronsTAGCutBasedTight = cms.EDProducer("PatElectronSelectorByValueMap",
                                                   input     = cms.InputTag("goodElectrons"), #options['ELECTRON_COLL']),
                                                   cut       = cms.string(options['ELECTRON_TAG_CUTS']),
                                                   selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-V2-standalone-tight"),
                                                   id_cut    = cms.bool(True)
                                                   )

###################################################################
##    _____     _                         __  __       _       _     _             
##   |_   _| __(_) __ _  __ _  ___ _ __  |  \/  | __ _| |_ ___| |__ (_)_ __   __ _ 
##     | || '__| |/ _` |/ _` |/ _ \ '__| | |\/| |/ _` | __/ __| '_ \| | '_ \ / _` |
##     | || |  | | (_| | (_| |  __/ |    | |  | | (_| | || (__| | | | | | | | (_| |
##     |_||_|  |_|\__, |\__, |\___|_|    |_|  |_|\__,_|\__\___|_| |_|_|_| |_|\__, |
##                |___/ |___/                                                |___/ 
###################################################################

if (len(options['TnPHLTTagFilters']) != len(options['TnPHLTProbeFilters'])):
    print "ERROR: different number of tag and probe filters, please fix it"
    sys.exit(-1)

process.goodElectronsTagHLT = cms.EDProducer("PatElectronTriggerCandProducer",
                                             filterNames = options['TnPHLTTagFilters'],
                                             inputs      = cms.InputTag("goodElectronsTAGCutBasedTight"), #options['ELECTRON_COLL']),
                                             bits        = cms.InputTag('TriggerResults::HLT'),
                                             objects     = cms.InputTag('selectedPatTrigger'),
                                             dR          = cms.double(0.3),
                                             isAND       = cms.bool(True)
                                             )

process.goodElectronsProbeVetoMini = process.goodElectronsTagHLT.clone()
process.goodElectronsProbeVetoMini.inputs = cms.InputTag("goodElectronsPROBECutBasedMiniVeto");
process.goodElectronsProbeVetoNoIso = process.goodElectronsTagHLT.clone()
process.goodElectronsProbeVetoNoIso.inputs = cms.InputTag("goodElectronsPROBECutBasedNoIsoVeto");
process.goodElectronsProbeLooseMini = process.goodElectronsProbeVetoMini.clone()
process.goodElectronsProbeLooseMini.inputs = cms.InputTag("goodElectronsPROBECutBasedMiniLoose");
process.goodElectronsProbeLooseNoIso = process.goodElectronsTagHLT.clone()
process.goodElectronsProbeLooseNoIso.inputs = cms.InputTag("goodElectronsPROBECutBasedNoIsoLoose");
process.goodElectronsProbeMediumMini = process.goodElectronsProbeVetoMini.clone()
process.goodElectronsProbeMediumMini.inputs = cms.InputTag("goodElectronsPROBECutBasedMiniMedium");
process.goodElectronsProbeMediumNoIso = process.goodElectronsTagHLT.clone()
process.goodElectronsProbeMediumNoIso.inputs = cms.InputTag("goodElectronsPROBECutBasedNoIsoMedium");
process.goodElectronsProbeTightMini = process.goodElectronsProbeVetoMini.clone()
process.goodElectronsProbeTightMini.inputs = cms.InputTag("goodElectronsPROBECutBasedMiniTight");
process.goodElectronsProbeTightNoIso = process.goodElectronsTagHLT.clone()
process.goodElectronsProbeTightNoIso.inputs = cms.InputTag("goodElectronsPROBECutBasedNoIsoTight");

process.goodElectronsProbeHLT = cms.EDProducer("PatElectronTriggerCandProducer",
                                               filterNames = options['TnPHLTProbeFilters'],
                                               inputs      = cms.InputTag("goodElectrons"),
                                               bits        = cms.InputTag('TriggerResults::HLT'),
                                               objects     = cms.InputTag('selectedPatTrigger'),
                                               dR          = cms.double(0.3),
                                               isAND       = cms.bool(True)
                                               )

process.goodElectronsProbeMeasureHLT = cms.EDProducer("PatElectronTriggerCandProducer",
                                                      filterNames = options['TnPHLTProbeFilters'],
                                                      inputs      = cms.InputTag("goodElectrons"),#PROBECutBasedVeto"),
                                                      bits        = cms.InputTag('TriggerResults::HLT'),
                                                      objects     = cms.InputTag('selectedPatTrigger'),
                                                      dR          = cms.double(0.3),
                                                      isAND       = cms.bool(True)
                                                      )

process.goodElectronsMeasureHLT = cms.EDProducer("PatElectronTriggerCandProducer",
                                                 filterNames = options['HLTFILTERTOMEASURE'],
                                                 inputs      = cms.InputTag("goodElectronsProbeMeasureHLT"),
                                                 bits        = cms.InputTag('TriggerResults::HLT'),
                                                 objects     = cms.InputTag('selectedPatTrigger'),
                                                 dR          = cms.double(0.3),
                                                 isAND       = cms.bool(False)
                                                 )

process.goodSuperClustersHLT = cms.EDProducer("RecoEcalCandidateTriggerCandProducer",
                                              filterNames  = options['TnPHLTProbeFilters'],
                                              inputs       = cms.InputTag("goodSuperClusters"),
                                              bits         = cms.InputTag('TriggerResults::HLT'),
                                              objects      = cms.InputTag('selectedPatTrigger'),
                                              dR           = cms.double(0.3),
                                              isAND        = cms.bool(True)
                                              )

process.egmGsfElectronIDs.physicsObjectSrc = cms.InputTag(options['ELECTRON_COLL'])
process.ele_sequence = cms.Sequence(
    process.goodElectrons +
    process.ElectronIsolation + 
    process.egmGsfElectronIDSequence +
    process.goodElectronsPROBECutBasedVeto +
    process.goodElectronsPROBECutBasedLoose +
    process.goodElectronsPROBECutBasedMedium +
    process.goodElectronsPROBECutBasedTight +
    process.goodElectronsTAGCutBasedTight +
    process.goodElectronsPROBECutBasedMiniVeto +
    process.goodElectronsPROBECutBasedMiniLoose +
    process.goodElectronsPROBECutBasedMiniMedium +
    process.goodElectronsPROBECutBasedMiniTight +
    process.goodElectronsPROBECutBasedNoIsoVeto +
    process.goodElectronsPROBECutBasedNoIsoLoose +
    process.goodElectronsPROBECutBasedNoIsoMedium +
    process.goodElectronsPROBECutBasedNoIsoTight +
    process.goodElectronsProbeVetoMini + 
    process.goodElectronsProbeVetoNoIso + 
    process.goodElectronsProbeLooseMini + 
    process.goodElectronsProbeLooseNoIso + 
    process.goodElectronsProbeMediumMini + 
    process.goodElectronsProbeMediumNoIso + 
    process.goodElectronsProbeTightMini + 
    process.goodElectronsProbeTightNoIso + 
    process.goodElectronsTagHLT +
    process.goodElectronsProbeHLT +
    process.goodElectronsProbeMeasureHLT +
    process.goodElectronsMeasureHLT
    )

process.sc_sequence = cms.Sequence(process.superClusterCands +
                                   process.goodSuperClusters +
                                   process.goodSuperClustersHLT +
                                   process.GsfMatchedSuperClusterCands
                                   )

###################################################################
##    _____ ___   ____    ____       _          
##   |_   _( _ ) |  _ \  |  _ \ __ _(_)_ __ ___ 
##     | | / _ \/\ |_) | | |_) / _` | | '__/ __|
##     | || (_>  <  __/  |  __/ (_| | | |  \__ \
##     |_| \___/\/_|     |_|   \__,_|_|_|  |___/
##   
###################################################################

process.tagTightHLT = cms.EDProducer("CandViewShallowCloneCombiner",
                                     decay = cms.string("goodElectronsTagHLT@+ goodElectronsProbeMeasureHLT@-"), 
                                     checkCharge = cms.bool(True),
                                     cut = cms.string("40<mass<1000"),
                                     )

process.tagTightSC = cms.EDProducer("CandViewShallowCloneCombiner",
                                    decay = cms.string("goodElectronsTagHLT goodSuperClustersHLT"), 
                                    checkCharge = cms.bool(False),
                                    cut = cms.string("40<mass<1000"),
                                    )

process.tagTightRECO = cms.EDProducer("CandViewShallowCloneCombiner",
                                      decay = cms.string("goodElectronsTagHLT@+ goodElectronsProbeHLT@-"), 
                                      checkCharge = cms.bool(True),
                                      cut = cms.string("40<mass<1000"),
                                    )

process.tagVetoMiniIso = cms.EDProducer("CandViewShallowCloneCombiner",
                                         decay = cms.string("goodElectronsTagHLT@+ goodElectronsProbeVetoNoIso@-"), 
                                         checkCharge = cms.bool(True),
                                         cut = cms.string("40<mass<1000"),
                                         )

process.tagLooseMiniIso = process.tagVetoMiniIso.clone()
process.tagLooseMiniIso.decay = cms.string("goodElectronsTagHLT@+ goodElectronsProbeLooseNoIso@-")
process.tagMediumMiniIso = process.tagVetoMiniIso.clone()
process.tagMediumMiniIso.decay = cms.string("goodElectronsTagHLT@+ goodElectronsProbeMediumNoIso@-")
process.tagTightMiniIso = process.tagVetoMiniIso.clone()
process.tagTightMiniIso.decay = cms.string("goodElectronsTagHLT@+ goodElectronsProbeTightNoIso@-")

process.allTagsAndProbes = cms.Sequence()

if (options['DOTRIGGER']):
    process.allTagsAndProbes *= process.tagTightHLT

if (options['DORECO']):
    process.allTagsAndProbes *= process.tagTightSC

if (options['DOID']):
    process.allTagsAndProbes *= process.tagTightRECO
    process.allTagsAndProbes *= process.tagVetoMiniIso
    process.allTagsAndProbes *= process.tagLooseMiniIso
    process.allTagsAndProbes *= process.tagMediumMiniIso
    process.allTagsAndProbes *= process.tagTightMiniIso

###################################################################
##    __  __  ____   __  __       _       _               
##   |  \/  |/ ___| |  \/  | __ _| |_ ___| |__   ___  ___ 
##   | |\/| | |     | |\/| |/ _` | __/ __| '_ \ / _ \/ __|
##   | |  | | |___  | |  | | (_| | || (__| | | |  __/\__ \
##   |_|  |_|\____| |_|  |_|\__,_|\__\___|_| |_|\___||___/
##                                   
###################################################################

process.McMatchHLT = cms.EDProducer("MCTruthDeltaRMatcherNew",
                                    matchPDGId = cms.vint32(11),
                                    src = cms.InputTag("goodElectrons"),
                                    distMin = cms.double(0.3),
                                    matched = cms.InputTag("prunedGenParticles"),
                                    checkCharge = cms.bool(True)
                                    )

process.McMatchSC = cms.EDProducer("MCTruthDeltaRMatcherNew",
                                   matchPDGId = cms.vint32(11),
                                   src = cms.InputTag("goodSuperClusters"),
                                   distMin = cms.double(0.3),
                                   matched = cms.InputTag("prunedGenParticles"),
                                   checkCharge = cms.bool(False)
                                   )
                     
process.McMatchTag = cms.EDProducer("MCTruthDeltaRMatcherNew",
                                    matchPDGId = cms.vint32(11),
                                    src = cms.InputTag("goodElectronsTAGCutBasedTight"),
                                    distMin = cms.double(0.2),
                                    matched = cms.InputTag("prunedGenParticles"),
                                    checkCharge = cms.bool(True)
                                    )

process.McMatchRECO = cms.EDProducer("MCTruthDeltaRMatcherNew",
                                     matchPDGId = cms.vint32(11),
                                     src = cms.InputTag("goodElectrons"),
                                     distMin = cms.double(0.2),
                                     matched = cms.InputTag("prunedGenParticles"),
                                     checkCharge = cms.bool(True)
                                    )

process.mc_sequence = cms.Sequence()

if (options['MC_FLAG']):
    process.mc_sequence *= (process.McMatchHLT + process.McMatchTag + process.McMatchSC + process.McMatchRECO)

##########################################################################
##    _____           _       _ ____            _            _   _  ____  
##   |_   _|_ _  __ _( )_ __ ( )  _ \ _ __ ___ | |__   ___  | \ | |/ ___| 
##     | |/ _` |/ _` |/| '_ \|/| |_) | '__/ _ \| '_ \ / _ \ |  \| | |  _  
##     | | (_| | (_| | | | | | |  __/| | | (_) | |_) |  __/ | |\  | |_| | 
##     |_|\__,_|\__, | |_| |_| |_|   |_|  \___/|_.__/ \___| |_| \_|\____| 
##              |___/                                                     
##                                                                        
##########################################################################
##    ____                      _     _           
##   |  _ \ ___ _   _ ___  __ _| |__ | | ___  ___ 
##   | |_) / _ \ | | / __|/ _` | '_ \| |/ _ \/ __|
##   |  _ <  __/ |_| \__ \ (_| | |_) | |  __/\__ \
##   |_| \_\___|\__,_|___/\__,_|_.__/|_|\___||___/
##
## I define some common variables for re-use later.
## This will save us repeating the same code for each efficiency category
#########################################################################

ZVariablesToStore = cms.PSet(
    eta = cms.string("eta"),
    abseta = cms.string("abs(eta)"),
    pt  = cms.string("pt"),
    mass  = cms.string("mass"),
    weight = cms.InputTag("pileupWeights")
    )   

SCProbeVariablesToStore = cms.PSet(
    probe_eta    = cms.string("eta"),
    probe_abseta = cms.string("abs(eta)"),
    probe_pt     = cms.string("pt"),
    probe_et     = cms.string("et"),
    probe_e      = cms.string("energy"),
)

ProbeVariablesToStore = cms.PSet(
    probe_Ele_eta    = cms.string("eta"),
    probe_Ele_abseta = cms.string("abs(eta)"),
    probe_Ele_pt     = cms.string("pt"),
    probe_Ele_et     = cms.string("et"),
    probe_Ele_e      = cms.string("energy"),
    probe_Ele_q      = cms.string("charge"),
    #probe_Ele_trackiso = cms.string("dr03TkSumPt"),
    #probe_Ele_reltrackiso = cms.string("dr03TkSumPt/pt"),
## super cluster quantities
    probe_sc_energy = cms.string("superCluster.energy"),
    probe_sc_et     = cms.string("superCluster.energy*sin(superClusterPosition.theta)"),    
    probe_sc_eta    = cms.string("superCluster.eta"),
    probe_sc_abseta = cms.string("abs(superCluster.eta)"),

#id based
    probe_Ele_dEtaIn        = cms.string("deltaEtaSuperClusterTrackAtVtx"),
    probe_Ele_dPhiIn        = cms.string("deltaPhiSuperClusterTrackAtVtx"),
    probe_Ele_sigmaIEtaIEta = cms.string("sigmaIetaIeta"),
    probe_Ele_hoe           = cms.string("hadronicOverEm"),
    probe_Ele_ooemoop       = cms.string("(1.0/ecalEnergy - eSuperClusterOverP/ecalEnergy)"),
    #probe_Ele_mHits         = cms.string("gsfTrack.trackerExpectedHitsInner.numberOfHits")
)

TagVariablesToStore = cms.PSet(
    Ele_eta    = cms.string("eta"),
    Ele_abseta = cms.string("abs(eta)"),
    Ele_pt     = cms.string("pt"),
    Ele_et     = cms.string("et"),
    Ele_e      = cms.string("energy"),
    Ele_q      = cms.string("charge"),
    
    ## super cluster quantities
    sc_energy = cms.string("superCluster.energy"),
    sc_et     = cms.string("superCluster.energy*sin(superClusterPosition.theta)"),    
    sc_eta    = cms.string("superCluster.eta"),
    sc_abseta = cms.string("abs(superCluster.eta)"),
)

CommonStuffForGsfElectronProbe = cms.PSet(
    variables = cms.PSet(ProbeVariablesToStore),
    ignoreExceptions =  cms.bool (True),
    addRunLumiInfo   =  cms.bool (True),
    addEventVariablesInfo   =  cms.bool(True),
    vertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices"),
    jetCollection = cms.InputTag("slimmedJets"),
    jet_pt_cut = cms.double(40.),
    jet_eta_cut = cms.double(2.5),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    pairVariables =  cms.PSet(ZVariablesToStore),
    pairFlags     =  cms.PSet(
        mass60to120 = cms.string("60 < mass < 120")
        ),
    tagVariables   =  cms.PSet(TagVariablesToStore),
    tagFlags       =  cms.PSet(),    
    )

CommonStuffForSuperClusterProbe = CommonStuffForGsfElectronProbe.clone()
CommonStuffForSuperClusterProbe.variables = cms.PSet(SCProbeVariablesToStore)

if options['MC_FLAG']:
    mcTruthCommonStuff = cms.PSet(
        isMC = cms.bool(True),
        tagMatches = cms.InputTag("McMatchTag"),
        motherPdgId = cms.vint32(22,23),
        #motherPdgId = cms.vint32(443), # JPsi
        #motherPdgId = cms.vint32(553), # Yupsilon
        makeMCUnbiasTree = cms.bool(False),
        checkMotherInUnbiasEff = cms.bool(False),
        mcVariables = cms.PSet(
            probe_eta = cms.string("eta"),
            probe_abseta = cms.string("abs(eta)"),
            probe_et  = cms.string("et"),
            probe_e  = cms.string("energy"),
            ),
        mcFlags     =  cms.PSet(
            probe_flag = cms.string("pt>0")
            ),      
        )
else:
    mcTruthCommonStuff = cms.PSet(
        isMC = cms.bool(False)
        )
    
##########################################################################
##   ____      __       __    ___                 ___    _ 
##  / ___|___ / _|      \ \  |_ _|___  ___       |_ _|__| |
## | |  _/ __| |_   _____\ \  | |/ __|/ _ \       | |/ _` |
## | |_| \__ \  _| |_____/ /  | |\__ \ (_) |  _   | | (_| |
##  \____|___/_|        /_/  |___|___/\___/  ( ) |___\__,_|
##                                           |/            
##########################################################################

process.GsfElectronToTrigger = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                              CommonStuffForSuperClusterProbe, mcTruthCommonStuff,
                                              tagProbePairs = cms.InputTag("tagTightHLT"),
                                              arbitration   = cms.string("None"),
                                              flags         = cms.PSet(passingHLT    = cms.InputTag("goodElectronsMeasureHLT")
                                                                       ),                                               
                                              allProbes     = cms.InputTag("goodElectronsProbeMeasureHLT"),
                                              PUWeightSrc   = cms.InputTag("pileupReweightingProducer","pileupWeights")

                                              )

if (options['MC_FLAG']):
    process.GsfElectronToTrigger.probeMatches  = cms.InputTag("McMatchHLT")

process.GsfElectronToSC = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                         CommonStuffForSuperClusterProbe, mcTruthCommonStuff,
                                         tagProbePairs = cms.InputTag("tagTightSC"),
                                         arbitration   = cms.string("None"),
                                         flags         = cms.PSet(passingRECO   = cms.InputTag("GsfMatchedSuperClusterCands"),                                                                  
                                                                  ),                                               
                                         allProbes     = cms.InputTag("goodSuperClustersHLT"),
                                         PUWeightSrc   = cms.InputTag("pileupReweightingProducer","pileupWeights")                                        
                                         )

if (options['MC_FLAG']):
    process.GsfElectronToSC.probeMatches  = cms.InputTag("McMatchSC")
    
process.VetoElectronToMiniIso = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                                mcTruthCommonStuff, CommonStuffForGsfElectronProbe,
                                                tagProbePairs = cms.InputTag("tagVetoMiniIso"),
                                                arbitration = cms.string("None"),
                                                flags = cms.PSet(
        passingVeto = cms.InputTag("goodElectronsPROBECutBasedMiniVeto"),
        ),
                                                allProbes = cms.InputTag("goodElectronsProbeVetoNoIso"),
                                                PUWeightSRC = cms.InputTag("pileupReweightingProducer","pileupWeights")
                                                )
process.LooseElectronToMiniIso = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                                mcTruthCommonStuff, CommonStuffForGsfElectronProbe,
                                                tagProbePairs = cms.InputTag("tagLooseMiniIso"),
                                                arbitration = cms.string("None"),
                                                flags = cms.PSet(
        passingLoose = cms.InputTag("goodElectronsPROBECutBasedMiniLoose"),
        ),
                                                allProbes = cms.InputTag("goodElectronsProbeLooseNoIso"),
                                                PUWeightSRC = cms.InputTag("pileupReweightingProducer","pileupWeights")
                                                )
process.MediumElectronToMiniIso = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                                mcTruthCommonStuff, CommonStuffForGsfElectronProbe,
                                                tagProbePairs = cms.InputTag("tagMediumMiniIso"),
                                                arbitration = cms.string("None"),
                                                flags = cms.PSet(
        passingMedium = cms.InputTag("goodElectronsPROBECutBasedMiniMedium"),
        ),
                                                allProbes = cms.InputTag("goodElectronsProbeMediumNoIso"),
                                                PUWeightSRC = cms.InputTag("pileupReweightingProducer","pileupWeights")
                                                )
process.TightElectronToMiniIso = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                                mcTruthCommonStuff, CommonStuffForGsfElectronProbe,
                                                tagProbePairs = cms.InputTag("tagTightMiniIso"),
                                                arbitration = cms.string("None"),
                                                flags = cms.PSet(
        passingTight = cms.InputTag("goodElectronsPROBECutBasedMiniTight"),
        ),
                                                allProbes = cms.InputTag("goodElectronsProbeTightNoIso"),
                                                PUWeightSRC = cms.InputTag("pileupReweightingProducer","pileupWeights")
                                                )

process.GsfElectronToRECO = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                           mcTruthCommonStuff, CommonStuffForGsfElectronProbe,
                                           tagProbePairs = cms.InputTag("tagTightRECO"),
                                           arbitration   = cms.string("None"),
                                           flags         = cms.PSet(passingVeto   = cms.InputTag("goodElectronsPROBECutBasedVeto"),
                                                                    passingLoose  = cms.InputTag("goodElectronsPROBECutBasedLoose"),
                                                                    passingMedium = cms.InputTag("goodElectronsPROBECutBasedMedium"),
                                                                    passingTight  = cms.InputTag("goodElectronsPROBECutBasedTight"),
                                                                    ),                                               
                                           allProbes     = cms.InputTag("goodElectronsProbeHLT"),
                                           PUWeightSrc   = cms.InputTag("pileupReweightingProducer","pileupWeights")

                                           )

if (options['MC_FLAG']):
    process.GsfElectronToRECO.probeMatches  = cms.InputTag("McMatchRECO")
    process.VetoElectronToMiniIso.probeMatches  = cms.InputTag("McMatchRECO")
    process.LooseElectronToMiniIso.probeMatches  = cms.InputTag("McMatchRECO")
    process.MediumElectronToMiniIso.probeMatches  = cms.InputTag("McMatchRECO")
    process.TightElectronToMiniIso.probeMatches  = cms.InputTag("McMatchRECO")

process.GsfElectronMiniToRECO = process.GsfElectronToRECO.clone()
process.GsfElectronMiniToRECO.flags = cms.PSet(
    passingVeto = cms.InputTag("goodElectronsPROBECutBasedMiniVeto"),
    passingLoose = cms.InputTag("goodElectronsPROBECutBasedMiniLoose"),
    passingMedium = cms.InputTag("goodElectronsPROBECutBasedMiniMedium"),
    passingTight = cms.InputTag("goodElectronsPROBECutBasedMiniTight"),
)

process.tree_sequence = cms.Sequence()
if (options['DOTRIGGER']):
    process.tree_sequence *= process.GsfElectronToTrigger

if (options['DORECO']):
    process.tree_sequence *= process.GsfElectronToSC

if (options['DOID']):
    process.tree_sequence *= process.GsfElectronToRECO
    process.tree_sequence *= process.GsfElectronMiniToRECO
    process.tree_sequence *= process.VetoElectronToMiniIso
    process.tree_sequence *= process.LooseElectronToMiniIso
    process.tree_sequence *= process.MediumElectronToMiniIso
    process.tree_sequence *= process.TightElectronToMiniIso

##########################################################################
##    ____       _   _     
##   |  _ \ __ _| |_| |__  
##   | |_) / _` | __| '_ \ 
##   |  __/ (_| | |_| | | |
##   |_|   \__,_|\__|_| |_|
##
##########################################################################

process.out = cms.OutputModule("PoolOutputModule", 
                               fileName = cms.untracked.string(options['OUTPUTEDMFILENAME']),
                               SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("p"))
                               )
process.outpath = cms.EndPath(process.out)
if (not options['DEBUG']):
    process.outpath.remove(process.out)

process.p = cms.Path(
    process.hltHighLevel +
    process.ele_sequence + 
    process.sc_sequence +
    ####process.GsfDRToNearestTau+
    process.allTagsAndProbes +
    process.pileupReweightingProducer +
    process.mc_sequence +
    process.tree_sequence
    )

process.TFileService = cms.Service(
    "TFileService", fileName = cms.string(options['OUTPUT_FILE_NAME'])
    )
