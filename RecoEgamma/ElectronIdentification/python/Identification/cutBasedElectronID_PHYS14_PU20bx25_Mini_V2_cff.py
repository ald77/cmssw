from PhysicsTools.SelectorUtils.centralIDRegistry import central_id_registry

# Common functions and classes for ID definition are imported here:
from RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_tools import *

#
# This is the first second of PHYS14 cuts, optimized on  PHYS14 samples. 
#
# The ID cuts below are optimized IDs for PHYS14 Scenario PU 20, bx 25ns
# The cut values are taken from the twiki:
#       https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedElectronIdentificationRun2
#       (where they may not stay, if a newer version of cuts becomes available for these
#        conditions)
# See also the presentation explaining these working points (this will not change):
#        https://indico.cern.ch/event/370494/contribution/2/material/slides/0.pdf
#
# First, define cut values
#

# Veto working point Barrel and Endcap
idName = "cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-veto"
WP_Veto_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.013625 , # dEtaInCut
    0.230374 , # dPhiInCut
    0.011586 , # full5x5_sigmaIEtaIEtaCut
    0.181130 , # hOverECut
    0.094095 , # dxyCut
    0.713070 , # dzCut
    0.295751 , # absEInverseMinusPInverseCut
    0.1 , # relCombIsolationWithEALowPtCut
    0.1 , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    2          # missingHitsCut
    )

WP_Veto_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.011932 , # dEtaInCut
    0.255450 , # dPhiInCut
    0.031849 , # full5x5_sigmaIEtaIEtaCut
    0.223870 , # hOverECut
    0.342293 , # dxyCut
    0.953461 , # dzCut
    0.155501 , # absEInverseMinusPInverseCut
    0.1 , # relCombIsolationWithEALowPtCut
    0.1 , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    3          # missingHitsCut
    )

# Loose working point Barrel and Endcap
idName = "cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-loose"
WP_Loose_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.009277 , # dEtaInCut
    0.094739 , # dPhiInCut
    0.010331 , # full5x5_sigmaIEtaIEtaCut
    0.093068 , # hOverECut
    0.035904 , # dxyCut
    0.075496 , # dzCut
    0.189968 , # absEInverseMinusPInverseCut
    0.1 , # relCombIsolationWithEALowPtCut
    0.1 , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

WP_Loose_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.009833 , # dEtaInCut
    0.149934 , # dPhiInCut
    0.031838 , # full5x5_sigmaIEtaIEtaCut
    0.115754 , # hOverECut
    0.099266 , # dxyCut
    0.197897 , # dzCut
    0.140662 , # absEInverseMinusPInverseCut
    0.1 , # relCombIsolationWithEALowPtCut
    0.1 , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

# Medium working point Barrel and Endcap
idName = "cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-medium"
WP_Medium_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.008925 , # dEtaInCut
    0.035973 , # dPhiInCut
    0.009996 , # full5x5_sigmaIEtaIEtaCut
    0.050537 , # hOverECut
    0.012235 , # dxyCut
    0.042020 , # dzCut
    0.091942 , # absEInverseMinusPInverseCut
    0.1 , # relCombIsolationWithEALowPtCut
    0.1 , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

WP_Medium_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.007429 , # dEtaInCut
    0.067879 , # dPhiInCut
    0.030135 , # full5x5_sigmaIEtaIEtaCut
    0.086782 , # hOverECut
    0.036719 , # dxyCut
    0.138142 , # dzCut
    0.100683 , # absEInverseMinusPInverseCut
    0.1 , # relCombIsolationWithEALowPtCut
    0.1 , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

# Tight working point Barrel and Endcap
idName = "cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-tight"
WP_Tight_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.006046 , # dEtaInCut
    0.028092 , # dPhiInCut
    0.009947 , # full5x5_sigmaIEtaIEtaCut
    0.045772 , # hOverECut
    0.008790 , # dxyCut
    0.021226 , # dzCut
    0.020118 , # absEInverseMinusPInverseCut
    0.1 , # relCombIsolationWithEALowPtCut
    0.1 , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

WP_Tight_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.007057 , # dEtaInCut
    0.030159 , # dPhiInCut
    0.028237 , # full5x5_sigmaIEtaIEtaCut
    0.067778 , # hOverECut
    0.027984 , # dxyCut
    0.133431 , # dzCut
    0.098919 , # absEInverseMinusPInverseCut
    0.1 , # relCombIsolationWithEALowPtCut
    0.1 , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

# Second, define what effective areas to use for pile-up correction
isoInputs = IsolationCutInputs_V2(
    # phoIsolationEffAreas
    "RecoEgamma/ElectronIdentification/data/PHYS14/effAreaElectrons_cone03_pfNeuHadronsAndPhotons.txt"
)


#
# Set up VID configuration for all cuts and working points
#

cutBasedElectronID_PHYS14_PU20bx25_Mini_V2_standalone_veto = configureVIDCutBasedEleID_Mini_V2(WP_Veto_EB, WP_Veto_EE, isoInputs)
cutBasedElectronID_PHYS14_PU20bx25_Mini_V2_standalone_loose = configureVIDCutBasedEleID_Mini_V2(WP_Loose_EB, WP_Loose_EE, isoInputs)
cutBasedElectronID_PHYS14_PU20bx25_Mini_V2_standalone_medium = configureVIDCutBasedEleID_Mini_V2(WP_Medium_EB, WP_Medium_EE, isoInputs)
cutBasedElectronID_PHYS14_PU20bx25_Mini_V2_standalone_tight = configureVIDCutBasedEleID_Mini_V2(WP_Tight_EB, WP_Tight_EE, isoInputs)

central_id_registry.register(cutBasedElectronID_PHYS14_PU20bx25_Mini_V2_standalone_veto.idName,
                             '83f993d919f7f4c8fbcdc76b6cca2d58')
central_id_registry.register(cutBasedElectronID_PHYS14_PU20bx25_Mini_V2_standalone_loose.idName,
                             '8b0e5bf29fa4dec84ab56d910ff022f5')
central_id_registry.register(cutBasedElectronID_PHYS14_PU20bx25_Mini_V2_standalone_medium.idName,
                             '2473da7234f0b1850c6abc0b164effb8')
central_id_registry.register(cutBasedElectronID_PHYS14_PU20bx25_Mini_V2_standalone_tight.idName,
                             '80edbff86726362e826be713024b082a')

# Veto working point Barrel and Endcap (no iso)
idName = "cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-noiso-veto"
WP_Veto_NoIso_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.013625 , # dEtaInCut
    0.230374 , # dPhiInCut
    0.011586 , # full5x5_sigmaIEtaIEtaCut
    0.181130 , # hOverECut
    0.094095 , # dxyCut
    0.713070 , # dzCut
    0.295751 , # absEInverseMinusPInverseCut
    9999. , # relCombIsolationWithEALowPtCut
    9999. , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    2          # missingHitsCut
    )

WP_Veto_NoIso_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.011932 , # dEtaInCut
    0.255450 , # dPhiInCut
    0.031849 , # full5x5_sigmaIEtaIEtaCut
    0.223870 , # hOverECut
    0.342293 , # dxyCut
    0.953461 , # dzCut
    0.155501 , # absEInverseMinusPInverseCut
    9999. , # relCombIsolationWithEALowPtCut
    9999. , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    3          # missingHitsCut
    )

# Loose working point Barrel and Endcap (no iso)
idName = "cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-noiso-loose"
WP_Loose_NoIso_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.009277 , # dEtaInCut
    0.094739 , # dPhiInCut
    0.010331 , # full5x5_sigmaIEtaIEtaCut
    0.093068 , # hOverECut
    0.035904 , # dxyCut
    0.075496 , # dzCut
    0.189968 , # absEInverseMinusPInverseCut
    9999. , # relCombIsolationWithEALowPtCut
    9999. , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

WP_Loose_NoIso_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.009833 , # dEtaInCut
    0.149934 , # dPhiInCut
    0.031838 , # full5x5_sigmaIEtaIEtaCut
    0.115754 , # hOverECut
    0.099266 , # dxyCut
    0.197897 , # dzCut
    0.140662 , # absEInverseMinusPInverseCut
    9999. , # relCombIsolationWithEALowPtCut
    9999. , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

# Medium working point Barrel and Endcap (no iso)
idName = "cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-noiso-medium"
WP_Medium_NoIso_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.008925 , # dEtaInCut
    0.035973 , # dPhiInCut
    0.009996 , # full5x5_sigmaIEtaIEtaCut
    0.050537 , # hOverECut
    0.012235 , # dxyCut
    0.042020 , # dzCut
    0.091942 , # absEInverseMinusPInverseCut
    9999. , # relCombIsolationWithEALowPtCut
    9999. , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

WP_Medium_NoIso_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.007429 , # dEtaInCut
    0.067879 , # dPhiInCut
    0.030135 , # full5x5_sigmaIEtaIEtaCut
    0.086782 , # hOverECut
    0.036719 , # dxyCut
    0.138142 , # dzCut
    0.100683 , # absEInverseMinusPInverseCut
    9999. , # relCombIsolationWithEALowPtCut
    9999. , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

# Tight working point Barrel and Endcap (no iso)
idName = "cutBasedElectronID-PHYS14-PU20bx25-Mini-V2-standalone-noiso-tight"
WP_Tight_NoIso_EB = EleWorkingPoint_V2(
    idName   , # idName
    0.006046 , # dEtaInCut
    0.028092 , # dPhiInCut
    0.009947 , # full5x5_sigmaIEtaIEtaCut
    0.045772 , # hOverECut
    0.008790 , # dxyCut
    0.021226 , # dzCut
    0.020118 , # absEInverseMinusPInverseCut
    9999. , # relCombIsolationWithEALowPtCut
    9999. , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

WP_Tight_NoIso_EE = EleWorkingPoint_V2(
    idName   , # idName
    0.007057 , # dEtaInCut
    0.030159 , # dPhiInCut
    0.028237 , # full5x5_sigmaIEtaIEtaCut
    0.067778 , # hOverECut
    0.027984 , # dxyCut
    0.133431 , # dzCut
    0.098919 , # absEInverseMinusPInverseCut
    9999. , # relCombIsolationWithEALowPtCut
    9999. , # relCombIsolationWithEAHighPtCut
    # conversion veto cut needs no parameters, so not mentioned
    1          # missingHitsCut
    )

#
# Set up VID configuration for all cuts and working points
#

cutBasedElectronID_PHYS14_PU20bx25_Mini_V2_standalone_noiso_veto = configureVIDCutBasedEleID_Mini_V2(WP_Veto_NoIso_EB, WP_Veto_NoIso_EE, isoInputs)
cutBasedElectronID_PHYS14_PU20bx25_Mini_V2_standalone_noiso_loose = configureVIDCutBasedEleID_Mini_V2(WP_Loose_NoIso_EB, WP_Loose_NoIso_EE, isoInputs)
cutBasedElectronID_PHYS14_PU20bx25_Mini_V2_standalone_noiso_medium = configureVIDCutBasedEleID_Mini_V2(WP_Medium_NoIso_EB, WP_Medium_NoIso_EE, isoInputs)
cutBasedElectronID_PHYS14_PU20bx25_Mini_V2_standalone_noiso_tight = configureVIDCutBasedEleID_Mini_V2(WP_Tight_NoIso_EB, WP_Tight_NoIso_EE, isoInputs)

central_id_registry.register(cutBasedElectronID_PHYS14_PU20bx25_Mini_V2_standalone_noiso_veto.idName,
                             '0ef18e48b4c743d42281c3e70c54b001')
central_id_registry.register(cutBasedElectronID_PHYS14_PU20bx25_Mini_V2_standalone_noiso_loose.idName,
                             '7fc90c3375d252a5ee2e3e00e0c4bbf6')
central_id_registry.register(cutBasedElectronID_PHYS14_PU20bx25_Mini_V2_standalone_noiso_medium.idName,
                             '0e7d83341084adc5c0abbeaaa9e9c6c2')
central_id_registry.register(cutBasedElectronID_PHYS14_PU20bx25_Mini_V2_standalone_noiso_tight.idName,
                             '0373cc1f9c4cb419758f43ae968acdc4')
