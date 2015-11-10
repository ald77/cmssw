from PhysicsTools.SelectorUtils.centralIDRegistry import central_id_registry

# Common functions and classes for ID definition are imported here:
from RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_tools import *

#
# This is the first round of Spring15 25ns cuts, optimized on  Spring15 25ns samples. 
#
# The ID cuts below are optimized IDs for Spring15 Scenario with 25ns bunch spacing
# The cut values are taken from the twiki:
#       https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedElectronIdentificationRun2
#       (where they may not stay, if a newer version of cuts becomes available for these
#        conditions)
# See also the presentation explaining these working points (this will not change):
#        https://indico.cern.ch/event/370507/contribution/1/attachments/1140657/1633761/Rami_eleCB_ID_25ns.pdf
#
# First, define cut values
#

# Veto working point Barrel and Endcap
idName = "cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-veto"
WP_Veto_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.0152  , # dEtaInCut
    0.216   , # dPhiInCut
    0.0114  , # full5x5_sigmaIEtaIEtaCut
    0.181   , # hOverECut
    0.0564  , # dxyCut
    0.472   , # dzCut
    0.207   , # absEInverseMinusPInverseCut
    0.1     , # relCombIsolationWithEALowPtCut
    0.1     , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    2          # missingHitsCut
    )

WP_Veto_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.0113  , # dEtaInCut
    0.237   , # dPhiInCut
    0.0352  , # full5x5_sigmaIEtaIEtaCut
    0.116   , # hOverECut
    0.222   , # dxyCut
    0.921   , # dzCut
    0.174   , # absEInverseMinusPInverseCut
    0.1     , # relCombIsolationWithEALowPtCut
    0.1     , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    3          # missingHitsCut
    )

# Loose working point Barrel and Endcap
idName = "cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-loose"
WP_Loose_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.0105  , # dEtaInCut
    0.115   , # dPhiInCut
    0.0103  , # full5x5_sigmaIEtaIEtaCut
    0.104   , # hOverECut
    0.0261  , # dxyCut
    0.41    , # dzCut
    0.102   , # absEInverseMinusPInverseCut
    0.1     , # relCombIsolationWithEALowPtCut
    0.1     , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    2          # missingHitsCut
    )

WP_Loose_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.00814 , # dEtaInCut
    0.182   , # dPhiInCut
    0.0301  , # full5x5_sigmaIEtaIEtaCut
    0.0897  , # hOverECut
    0.118   , # dxyCut
    0.822   , # dzCut
    0.126   , # absEInverseMinusPInverseCut
    0.1   , # relCombIsolationWithEALowPtCut
    0.1   , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

# Medium working point Barrel and Endcap
idName = "cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-medium"
WP_Medium_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.0103 , # dEtaInCut
    0.0336 , # dPhiInCut
    0.0101 , # full5x5_sigmaIEtaIEtaCut
    0.0876 , # hOverECut
    0.0118 , # dxyCut
    0.373  , # dzCut
    0.0174 , # absEInverseMinusPInverseCut
    0.1    , # relCombIsolationWithEALowPtCut
    0.1    , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    2          # missingHitsCut
    )

WP_Medium_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.00733 , # dEtaInCut
    0.114   , # dPhiInCut
    0.0283  , # full5x5_sigmaIEtaIEtaCut
    0.0678  , # hOverECut
    0.0739  , # dxyCut
    0.602   , # dzCut
    0.0898  , # absEInverseMinusPInverseCut
    0.1     , # relCombIsolationWithEALowPtCut
    0.1     , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

# Tight working point Barrel and Endcap
idName = "cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-tight"
WP_Tight_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.00926   , # dEtaInCut
    0.0336    , # dPhiInCut
    0.0101    , # full5x5_sigmaIEtaIEtaCut
    0.0597    , # hOverECut
    0.0111    , # dxyCut
    0.0466    , # dzCut
    0.012     , # absEInverseMinusPInverseCut
    0.1       , # relCombIsolationWithEALowPtCut
    0.1       , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    2          # missingHitsCut
    )

WP_Tight_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.00724 , # dEtaInCut
    0.0918  , # dPhiInCut
    0.0279  , # full5x5_sigmaIEtaIEtaCut
    0.0615  , # hOverECut
    0.0351  , # dxyCut
    0.417   , # dzCut
    0.00999 , # absEInverseMinusPInverseCut
    0.1     , # relCombIsolationWithEALowPtCut
    0.1     , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

# Second, define what effective areas to use for pile-up correction
isoInputs = IsolationCutInputs_V2(
    # phoIsolationEffAreas
    "RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt"
)


#
# Set up VID configuration for all cuts and working points
#

cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_veto = configureVIDCutBasedEleID_Mini_V2(WP_Veto_EB, WP_Veto_EE, isoInputs)
cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_loose = configureVIDCutBasedEleID_Mini_V2(WP_Loose_EB, WP_Loose_EE, isoInputs)
cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_medium = configureVIDCutBasedEleID_Mini_V2(WP_Medium_EB, WP_Medium_EE, isoInputs)
cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_tight = configureVIDCutBasedEleID_Mini_V2(WP_Tight_EB, WP_Tight_EE, isoInputs)


# The MD5 sum numbers below reflect the exact set of cut variables
# and values above. If anything changes, one has to 
# 1) comment out the lines below about the registry, 
# 2) run "calculateMD5 <this file name> <one of the VID config names just above>
# 3) update the MD5 sum strings below and uncomment the lines again.
#

central_id_registry.register(cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_veto.idName,
                             'a304cdd11209b38a69b2c8c242d1b69d')
central_id_registry.register(cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_loose.idName,
                             '41d3c1e008fe81a2fca59f7dfe7f7d95')
central_id_registry.register(cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_medium.idName,
                             'c9e0ac748c809f644d87a0d03cbbebbf')
central_id_registry.register(cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_tight.idName,
                             '25e80917b4f31543248ed36ceee09c92')


### for now until we have a database...
cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_veto.isPOGApproved = cms.untracked.bool(True)
cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_loose.isPOGApproved = cms.untracked.bool(True)
cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_medium.isPOGApproved = cms.untracked.bool(True)
cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_tight.isPOGApproved = cms.untracked.bool(True)

# Veto working point Barrel and Endcap
idName = "cutBasedElectronID-Spring15-25ns-Mini4-V1-standalone-veto"
WP_Veto_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.0152  , # dEtaInCut
    0.216   , # dPhiInCut
    0.0114  , # full5x5_sigmaIEtaIEtaCut
    0.181   , # hOverECut
    0.0564  , # dxyCut
    0.472   , # dzCut
    0.207   , # absEInverseMinusPInverseCut
    0.4     , # relCombIsolationWithEALowPtCut
    0.4     , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    2          # missingHitsCut
    )

WP_Veto_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.0113  , # dEtaInCut
    0.237   , # dPhiInCut
    0.0352  , # full5x5_sigmaIEtaIEtaCut
    0.116   , # hOverECut
    0.222   , # dxyCut
    0.921   , # dzCut
    0.174   , # absEInverseMinusPInverseCut
    0.4     , # relCombIsolationWithEALowPtCut
    0.4     , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    3          # missingHitsCut
    )

# Loose working point Barrel and Endcap
idName = "cutBasedElectronID-Spring15-25ns-Mini4-V1-standalone-loose"
WP_Loose_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.0105  , # dEtaInCut
    0.115   , # dPhiInCut
    0.0103  , # full5x5_sigmaIEtaIEtaCut
    0.104   , # hOverECut
    0.0261  , # dxyCut
    0.41    , # dzCut
    0.102   , # absEInverseMinusPInverseCut
    0.4     , # relCombIsolationWithEALowPtCut
    0.4     , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    2          # missingHitsCut
    )

WP_Loose_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.00814 , # dEtaInCut
    0.182   , # dPhiInCut
    0.0301  , # full5x5_sigmaIEtaIEtaCut
    0.0897  , # hOverECut
    0.118   , # dxyCut
    0.822   , # dzCut
    0.126   , # absEInverseMinusPInverseCut
    0.4   , # relCombIsolationWithEALowPtCut
    0.4   , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

# Medium working point Barrel and Endcap
idName = "cutBasedElectronID-Spring15-25ns-Mini4-V1-standalone-medium"
WP_Medium_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.0103 , # dEtaInCut
    0.0336 , # dPhiInCut
    0.0101 , # full5x5_sigmaIEtaIEtaCut
    0.0876 , # hOverECut
    0.0118 , # dxyCut
    0.373  , # dzCut
    0.0174 , # absEInverseMinusPInverseCut
    0.4    , # relCombIsolationWithEALowPtCut
    0.4    , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    2          # missingHitsCut
    )

WP_Medium_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.00733 , # dEtaInCut
    0.114   , # dPhiInCut
    0.0283  , # full5x5_sigmaIEtaIEtaCut
    0.0678  , # hOverECut
    0.0739  , # dxyCut
    0.602   , # dzCut
    0.0898  , # absEInverseMinusPInverseCut
    0.4     , # relCombIsolationWithEALowPtCut
    0.4     , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

# Tight working point Barrel and Endcap
idName = "cutBasedElectronID-Spring15-25ns-Mini4-V1-standalone-tight"
WP_Tight_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.00926   , # dEtaInCut
    0.0336    , # dPhiInCut
    0.0101    , # full5x5_sigmaIEtaIEtaCut
    0.0597    , # hOverECut
    0.0111    , # dxyCut
    0.0466    , # dzCut
    0.012     , # absEInverseMinusPInverseCut
    0.4       , # relCombIsolationWithEALowPtCut
    0.4       , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    2          # missingHitsCut
    )

WP_Tight_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.00724 , # dEtaInCut
    0.0918  , # dPhiInCut
    0.0279  , # full5x5_sigmaIEtaIEtaCut
    0.0615  , # hOverECut
    0.0351  , # dxyCut
    0.417   , # dzCut
    0.00999 , # absEInverseMinusPInverseCut
    0.4     , # relCombIsolationWithEALowPtCut
    0.4     , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

# Second, define what effective areas to use for pile-up correction
isoInputs = IsolationCutInputs_V2(
    # phoIsolationEffAreas
    "RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt"
)


#
# Set up VID configuration for all cuts and working points
#

cutBasedElectronID_Spring15_25ns_Mini4_V1_standalone_veto = configureVIDCutBasedEleID_Mini_V2(WP_Veto_EB, WP_Veto_EE, isoInputs)
cutBasedElectronID_Spring15_25ns_Mini4_V1_standalone_loose = configureVIDCutBasedEleID_Mini_V2(WP_Loose_EB, WP_Loose_EE, isoInputs)
cutBasedElectronID_Spring15_25ns_Mini4_V1_standalone_medium = configureVIDCutBasedEleID_Mini_V2(WP_Medium_EB, WP_Medium_EE, isoInputs)
cutBasedElectronID_Spring15_25ns_Mini4_V1_standalone_tight = configureVIDCutBasedEleID_Mini_V2(WP_Tight_EB, WP_Tight_EE, isoInputs)


# The MD5 sum numbers below reflect the exact set of cut variables
# and values above. If anything changes, one has to 
# 1) comment out the lines below about the registry, 
# 2) run "calculateMD5 <this file name> <one of the VID config names just above>
# 3) update the MD5 sum strings below and uncomment the lines again.
#

central_id_registry.register(cutBasedElectronID_Spring15_25ns_Mini4_V1_standalone_veto.idName,
                             '6e49d839c13b2291849f502a4476312e')
central_id_registry.register(cutBasedElectronID_Spring15_25ns_Mini4_V1_standalone_loose.idName,
                             '890d47711fd65cdd34b9653421dbe5c1')
central_id_registry.register(cutBasedElectronID_Spring15_25ns_Mini4_V1_standalone_medium.idName,
                             '02a939bfb1da805325cf9c4173205e13')
central_id_registry.register(cutBasedElectronID_Spring15_25ns_Mini4_V1_standalone_tight.idName,
                             '24e4e5ad50c55d468e61b5f313ef7e0c')

### for now until we have a database...
cutBasedElectronID_Spring15_25ns_Mini4_V1_standalone_veto.isPOGApproved = cms.untracked.bool(True)
cutBasedElectronID_Spring15_25ns_Mini4_V1_standalone_loose.isPOGApproved = cms.untracked.bool(True)
cutBasedElectronID_Spring15_25ns_Mini4_V1_standalone_medium.isPOGApproved = cms.untracked.bool(True)
cutBasedElectronID_Spring15_25ns_Mini4_V1_standalone_tight.isPOGApproved = cms.untracked.bool(True)

#
# First, define cut values
#

# Veto working point Barrel and Endcap
idName = "cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-veto"
WP_Veto_NoIso_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.0152  , # dEtaInCut
    0.216   , # dPhiInCut
    0.0114  , # full5x5_sigmaIEtaIEtaCut
    0.181   , # hOverECut
    0.0564  , # dxyCut
    0.472   , # dzCut
    0.207   , # absEInverseMinusPInverseCut
    9999.   , # relCombIsolationWithEALowPtCut
    9999.   , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    2          # missingHitsCut
    )

WP_Veto_NoIso_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.0113  , # dEtaInCut
    0.237   , # dPhiInCut
    0.0352  , # full5x5_sigmaIEtaIEtaCut
    0.116   , # hOverECut
    0.222   , # dxyCut
    0.921   , # dzCut
    0.174   , # absEInverseMinusPInverseCut
    9999.   , # relCombIsolationWithEALowPtCut
    9999.   , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    3          # missingHitsCut
    )

# Loose working point Barrel and Endcap
idName = "cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-loose"
WP_Loose_NoIso_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.0105  , # dEtaInCut
    0.115   , # dPhiInCut
    0.0103  , # full5x5_sigmaIEtaIEtaCut
    0.104   , # hOverECut
    0.0261  , # dxyCut
    0.41    , # dzCut
    0.102   , # absEInverseMinusPInverseCut
    9999.   , # relCombIsolationWithEALowPtCut
    9999.   , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    2          # missingHitsCut
    )

WP_Loose_NoIso_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.00814 , # dEtaInCut
    0.182   , # dPhiInCut
    0.0301  , # full5x5_sigmaIEtaIEtaCut
    0.0897  , # hOverECut
    0.118   , # dxyCut
    0.822   , # dzCut
    0.126   , # absEInverseMinusPInverseCut
    9999. , # relCombIsolationWithEALowPtCut
    9999. , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

# Medium working point Barrel and Endcap
idName = "cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-medium"
WP_Medium_NoIso_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.0103 , # dEtaInCut
    0.0336 , # dPhiInCut
    0.0101 , # full5x5_sigmaIEtaIEtaCut
    0.0876 , # hOverECut
    0.0118 , # dxyCut
    0.373  , # dzCut
    0.0174 , # absEInverseMinusPInverseCut
    9999.  , # relCombIsolationWithEALowPtCut
    9999.  , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    2          # missingHitsCut
    )

WP_Medium_NoIso_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.00733 , # dEtaInCut
    0.114   , # dPhiInCut
    0.0283  , # full5x5_sigmaIEtaIEtaCut
    0.0678  , # hOverECut
    0.0739  , # dxyCut
    0.602   , # dzCut
    0.0898  , # absEInverseMinusPInverseCut
    9999.   , # relCombIsolationWithEALowPtCut
    9999.   , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

# Tight working point Barrel and Endcap
idName = "cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-tight"
WP_Tight_NoIso_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.00926   , # dEtaInCut
    0.0336    , # dPhiInCut
    0.0101    , # full5x5_sigmaIEtaIEtaCut
    0.0597    , # hOverECut
    0.0111    , # dxyCut
    0.0466    , # dzCut
    0.012     , # absEInverseMinusPInverseCut
    9999.     , # relCombIsolationWithEALowPtCut
    9999.     , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    2          # missingHitsCut
    )

WP_Tight_NoIso_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.00724 , # dEtaInCut
    0.0918  , # dPhiInCut
    0.0279  , # full5x5_sigmaIEtaIEtaCut
    0.0615  , # hOverECut
    0.0351  , # dxyCut
    0.417   , # dzCut
    0.00999 , # absEInverseMinusPInverseCut
    9999.   , # relCombIsolationWithEALowPtCut
    9999.   , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )


#
# Set up VID configuration for all cuts and working points
#

cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_noiso_veto = configureVIDCutBasedEleID_Mini_V2(WP_Veto_NoIso_EB, WP_Veto_NoIso_EE, isoInputs)
cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_noiso_loose = configureVIDCutBasedEleID_Mini_V2(WP_Loose_NoIso_EB, WP_Loose_NoIso_EE, isoInputs)
cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_noiso_medium = configureVIDCutBasedEleID_Mini_V2(WP_Medium_NoIso_EB, WP_Medium_NoIso_EE, isoInputs)
cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_noiso_tight = configureVIDCutBasedEleID_Mini_V2(WP_Tight_NoIso_EB, WP_Tight_NoIso_EE, isoInputs)


# The MD5 sum numbers below reflect the exact set of cut variables
# and values above. If anything changes, one has to 
# 1) comment out the lines below about the registry, 
# 2) run "calculateMD5 <this file name> <one of the VID config names just above>
# 3) update the MD5 sum strings below and uncomment the lines again.
#

central_id_registry.register(cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_noiso_veto.idName,
                             '67e255b4086e4c2810ffa00d3f13c8d5')
central_id_registry.register(cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_noiso_loose.idName,
                             '24a156cfc92174ad348c073047015c31')
central_id_registry.register(cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_noiso_medium.idName,
                             '056c52297bd7ea00319d3820929adf3c')
central_id_registry.register(cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_noiso_tight.idName,
                             'fd4e3ae8626a83cf34cc46f49bdf5168')


### for now until we have a database...
cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_noiso_veto.isPOGApproved = cms.untracked.bool(True)
cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_noiso_loose.isPOGApproved = cms.untracked.bool(True)
cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_noiso_medium.isPOGApproved = cms.untracked.bool(True)
cutBasedElectronID_Spring15_25ns_Mini_V1_standalone_noiso_tight.isPOGApproved = cms.untracked.bool(True)
