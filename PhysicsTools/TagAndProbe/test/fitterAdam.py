import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('analysis')

options.register(
    "pdfName",
    "pdfSignalPlusBackground",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Fit shape"
    )

options.register(
    "noData",
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Don't compute data efficiencies"
    )

options.register(
    "noMC",
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Don't compute MC efficiencies"
    )

options.register(
    "noID",
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Don't compute efficiencies for Gsf->ID"
    )

options.register(
    "noIso",
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Don't compute efficiencies for ID->ID+Iso"
    )

options.register(
    "noStandard",
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Don't compute efficiencies for ID->ID+Standard Iso"
    )

options.register(
    "doUnmatched",
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Compute MC efficiencies without truth-matching"
    )

options.parseArguments()

process = cms.Process("TagProbe")
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout','cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

measBinnedVariables = cms.PSet(
    probe_sc_et = cms.vdouble(10., 20., 30., 40., 50., 200.),
    probe_sc_abseta = cms.vdouble(0., 1.442, 1.556, 2.5),
    )
dataVariables = cms.PSet(
    mass = cms.vstring("Tag-Probe Mass", "60.0", "120.0", " GeV/c^{2}"),
    probe_sc_et = cms.vstring("Probe E_{T}", "0", "200", "GeV/c"),
    probe_sc_abseta = cms.vstring("Probe #eta", "0", "2.5", ""),
    )

trueBinnedVariables = cms.PSet(
    measBinnedVariables,
    mcTrue = cms.vstring("true"),
    )

dataUnbinnedVariables = cms.vstring("mass")
mcUnbinnedVariables = cms.vstring("mass","PUweight")

trueVars = cms.PSet(
    BinnedVariables = trueBinnedVariables,
    UnbinnedVariables = mcUnbinnedVariables,
    BinToPDFmap = cms.vstring(options.pdfName),
    )
mcVars = trueVars.clone()
mcVars.BinnedVariables = measBinnedVariables
dataVars = mcVars.clone()
dataVars.UnbinnedVariables = dataUnbinnedVariables

trueVeto = cms.PSet(trueVars, EfficiencyCategoryAndState = cms.vstring("passingVeto","pass"))
trueLoose = cms.PSet(trueVars, EfficiencyCategoryAndState = cms.vstring("passingLoose","pass"))
trueMedium = cms.PSet(trueVars, EfficiencyCategoryAndState = cms.vstring("passingMedium","pass"))
trueTight = cms.PSet(trueVars, EfficiencyCategoryAndState = cms.vstring("passingTight","pass"))
trueStandard = cms.PSet(trueVars, EfficiencyCategoryAndState = cms.vstring("passingStandard","pass"))
trueMini = cms.PSet(trueVars, EfficiencyCategoryAndState = cms.vstring("passingMini","pass"))
mcVeto = cms.PSet(mcVars, EfficiencyCategoryAndState = cms.vstring("passingVeto","pass"))
mcLoose = cms.PSet(mcVars, EfficiencyCategoryAndState = cms.vstring("passingLoose","pass"))
mcMedium = cms.PSet(mcVars, EfficiencyCategoryAndState = cms.vstring("passingMedium","pass"))
mcTight = cms.PSet(mcVars, EfficiencyCategoryAndState = cms.vstring("passingTight","pass"))
mcStandard = cms.PSet(mcVars, EfficiencyCategoryAndState = cms.vstring("passingStandard","pass"))
mcMini = cms.PSet(mcVars, EfficiencyCategoryAndState = cms.vstring("passingMini","pass"))
dataVeto = cms.PSet(dataVars, EfficiencyCategoryAndState = cms.vstring("passingVeto","pass"))
dataLoose = cms.PSet(dataVars, EfficiencyCategoryAndState = cms.vstring("passingLoose","pass"))
dataMedium = cms.PSet(dataVars, EfficiencyCategoryAndState = cms.vstring("passingMedium","pass"))
dataTight = cms.PSet(dataVars, EfficiencyCategoryAndState = cms.vstring("passingTight","pass"))
dataStandard = cms.PSet(dataVars, EfficiencyCategoryAndState = cms.vstring("passingStandard","pass"))
dataMini = cms.PSet(dataVars, EfficiencyCategoryAndState = cms.vstring("passingMini","pass"))

mcVariables = cms.PSet(dataVariables, PUweight = cms.vstring("PU weight", "0", "100", ""))

catMCTrue = cms.vstring("MC true", "dummy[true=1,false=0]")
catVeto = cms.vstring("passingVeto", "dummy[pass=1,fail=0]")
catLoose = cms.vstring("passingLoose", "dummy[pass=1,fail=0]")
catMedium = cms.vstring("passingMedium", "dummy[pass=1,fail=0]")
catTight = cms.vstring("passingTight", "dummy[pass=1,fail=0]")
catStandard = cms.vstring("passingStandard", "dummy[pass=1,fail=0]")
catMini = cms.vstring("passingMini", "dummy[pass=1,fail=0]")

dataIsoCats = cms.PSet(passingStandard = catStandard, passingMini = catMini)
mcIsoCats = cms.PSet(dataIsoCats, mcTrue = catMCTrue)
dataIsoEffs = cms.PSet(Standard = dataStandard, Mini = dataMini)
mcIsoEffs = cms.PSet(
    MCtruth_Standard = trueStandard,
    MCtruth_Mini = trueMini,
    Standard = mcStandard,
    Mini = mcMini
    )
dataIDCats = cms.PSet(
    passingVeto = catVeto,
    passingLoose = catLoose,
    passingMedium = catMedium,
    passingTight = catTight
    )
mcIDCats = cms.PSet(dataIDCats, mcTrue = catMCTrue)
dataIDEffs = cms.PSet(
    Veto = dataVeto,
    Loose = dataLoose,
    Medium = dataMedium,
    Tight = dataTight
    )
mcIDEffs = cms.PSet(
    MCtruth_Veto = trueVeto,
    MCtruth_Loose = trueLoose,
    MCtruth_Medium = trueMedium,
    MCtruth_Tight = trueTight,
    Veto = mcVeto,
    Loose = mcLoose,
    Medium = mcMedium,
    Tight = mcTight
    )

if options.noStandard:
    delattr(dataIsoCats, "passingStandard")
    delattr(dataIsoEffs, "Standard")
    delattr(mcIsoCats, "passingStandard")
    delattr(mcIsoEffs, "Standard")
    delattr(mcIsoEffs, "MCtruth_Standard")

if not options.doUnmatched:
    if hasattr(mcIsoEffs, "Standard"):
        delattr(mcIsoEffs, "Standard")
    if hasattr(mcIsoEffs, "Mini"):
        delattr(mcIsoEffs, "Mini")
    if hasattr(mcIDEffs, "Veto"):
        delattr(mcIDEffs, "Veto")
    if hasattr(mcIDEffs, "Loose"):
        delattr(mcIDEffs, "Loose")
    if hasattr(mcIDEffs, "Medium"):
        delattr(mcIDEffs, "Medium")
    if hasattr(mcIDEffs, "Tight"):
        delattr(mcIDEffs, "Tight")

process.dataGsfElectronToId = cms.EDAnalyzer(
    "TagProbeFitTreeAnalyzer",
    InputFileNames = cms.vstring("TnPTree_data.root"),
    InputDirectoryName = cms.string("GsfElectronToID"),
    InputTreeName = cms.string("fitter_tree"),
    OutputFileName = cms.string("eff_data_id.root"),
    NumCPU = cms.uint32(6),
    SaveWorkspace = cms.bool(False),
    doCutAndCount = cms.bool(True),
    floatShapeParameters = cms.bool(True),
    binnedFit = cms.bool(True),
    binsForFit = cms.uint32(60),
    Variables = dataVariables,
    Categories = cms.PSet(dataIDCats),
    PDFs = cms.PSet(
        pdfSignalPlusBackground = cms.vstring(
            "RooCBExGaussShape::signalResPass(mass,meanP[-0.0,-5.000,5.000],sigmaP[0.956,0.00,5.000],alphaP[0.999, 0.0,50.0],nP[1.405,0.000,50.000],sigmaP_2[1.000,0.500,15.00])",
            "RooCBExGaussShape::signalResFail(mass,meanF[-0.0,-5.000,5.000],sigmaF[3.331,0.00,5.000],alphaF[1.586, 0.0,50.0],nF[0.464,0.000,20.00],sigmaF_2[1.675,0.500,2.000])",
            "ZGeneratorLineShape::signalPhy(mass)",
            "RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.1, 0, 1], peakPass[90.0])",
            "RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.1, 0, 1], peakFail[90.0])",
            "FCONV::signalPass(mass, signalPhy, signalResPass)",
            "FCONV::signalFail(mass, signalPhy, signalResFail)",
            "efficiency[0.5,0,1]",
            "signalFractionInPassing[0.9,0.,1.]",
            ),
        ZCB = cms.vstring(
            "RooCBShape::signalResPass(mass,meanP[-0.0,-5.000,5.000],sigmaP[0.956,0.00,5.000],alphaP[0.999, 0.0,50.0],nP[1.405,0.000,50.000])",
            "RooCBShape::signalResFail(mass,meanF[-0.0,-5.000,5.000],sigmaF[3.331,0.00,5.000],alphaF[1.586, 0.0,50.0],nF[0.464,0.000,20.00])",
            "ZGeneratorLineShape::signalPhy(mass)",
            "RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.1, 0, 1], peakPass[90.0])",
            "RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.1, 0, 1], peakFail[90.0])",
            "FCONV::signalPass(mass, signalPhy, signalResPass)",
            "FCONV::signalFail(mass, signalPhy, signalResFail)",
            "efficiency[0.5,0,1]",
            "signalFractionInPassing[0.9,0.,1.]",
            ),
        voigtCB = cms.vstring(
            "RooCBShape::signalResPass(mass,meanP[-0.0,-5.000,5.000],sigmaP[0.956,0.00,5.000],alphaP[0.999, 0.0,50.0],nP[1.405,0.000,50.000])",
            "RooCBShape::signalResFail(mass,meanF[-0.0,-5.000,5.000],sigmaF[3.331,0.00,5.000],alphaF[1.586, 0.0,50.0],nF[0.464,0.000,20.00])",
            "Voigtian::signalPhy(mass, mean[91.2, 84.0, 98.0], width[2.4, 0.5, 5.0], sigma[5., 1., 12.0])",
            "RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.1, 0, 1], peakPass[90.0])",
            "RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.1, 0, 1], peakFail[90.0])",
            "FCONV::signalPass(mass, signalPhy, signalResPass)",
            "FCONV::signalFail(mass, signalPhy, signalResFail)",
            "efficiency[0.5,0,1]",
            "signalFractionInPassing[0.9,0.,1.]",
            ),
        BWCB = cms.vstring(
            "RooCBShape::signalResPass(mass,meanP[-0.0,-5.000,5.000],sigmaP[0.956,0.00,5.000],alphaP[0.999, 0.0,50.0],nP[1.405,0.000,50.000])",
            "RooCBShape::signalResFail(mass,meanF[-0.0,-5.000,5.000],sigmaF[3.331,0.00,5.000],alphaF[1.586, 0.0,50.0],nF[0.464,0.000,20.00])",
            "RooBreitWigner::signalPhy(mass, mean[91.2, 84.0, 98.0], width[2.4, 0.5, 5.0])",
            "RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.1, 0, 1], peakPass[90.0])",
            "RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.1, 0, 1], peakFail[90.0])",
            "FCONV::signalPass(mass, signalPhy, signalResPass)",
            "FCONV::signalFail(mass, signalPhy, signalResFail)",
            "efficiency[0.5,0,1]",
            "signalFractionInPassing[0.9,0.,1.]",
            ),
        gaussPlusLinear = cms.vstring(
            "Voigtian::signal(mass, mean[91.2, 84.0, 98.0], width[2.4, 0.5, 5.0], sigma[5., 1., 12.0])",
            "RooExponential::backgroundPass(mass, cPass[0,-2,2])",
            "RooExponential::backgroundFail(mass, cFail[0,-2,2])",
            "efficiency[0.95,0,1]",
            "signalFractionInPassing[0.9,0.,1.]"
            ),
        ),
    Efficiencies = cms.PSet(dataIDEffs),
    )

process.mcGsfElectronToId = process.dataGsfElectronToId.clone()
process.mcGsfElectronToId.InputFileNames = cms.vstring("TnPTree_mc.root")
process.mcGsfElectronToId.OutputFileName = cms.string("eff_mc_id.root")
process.mcGsfElectronToId.WeightVariable = cms.string("PUweight")
process.mcGsfElectronToId.Variables = mcVariables
process.mcGsfElectronToId.Categories = cms.PSet(mcIDCats)
process.mcGsfElectronToId.Efficiencies = cms.PSet(mcIDEffs)

process.dataVetoElectronToIso = process.dataGsfElectronToId.clone()
process.dataVetoElectronToIso.InputDirectoryName = cms.string("VetoElectronToIso")
process.dataVetoElectronToIso.OutputFileName = cms.string("eff_data_veto.root")
process.dataVetoElectronToIso.Categories = cms.PSet(dataIsoCats)
process.dataVetoElectronToIso.Efficiencies = cms.PSet(dataIsoEffs)

process.mcVetoElectronToIso = process.mcGsfElectronToId.clone()
process.mcVetoElectronToIso.InputDirectoryName = cms.string("VetoElectronToIso")
process.mcVetoElectronToIso.OutputFileName = cms.string("eff_mc_veto.root")
process.mcVetoElectronToIso.Categories = cms.PSet(mcIsoCats)
process.mcVetoElectronToIso.Efficiencies = cms.PSet(mcIsoEffs)

process.dataLooseElectronToIso = process.dataGsfElectronToId.clone()
process.dataLooseElectronToIso.InputDirectoryName = cms.string("LooseElectronToIso")
process.dataLooseElectronToIso.OutputFileName = cms.string("eff_data_loose.root")
process.dataLooseElectronToIso.Categories = cms.PSet(dataIsoCats)
process.dataLooseElectronToIso.Efficiencies = cms.PSet(dataIsoEffs)

process.mcLooseElectronToIso = process.mcGsfElectronToId.clone()
process.mcLooseElectronToIso.InputDirectoryName = cms.string("LooseElectronToIso")
process.mcLooseElectronToIso.OutputFileName = cms.string("eff_mc_loose.root")
process.mcLooseElectronToIso.Categories = cms.PSet(mcIsoCats)
process.mcLooseElectronToIso.Efficiencies = cms.PSet(mcIsoEffs)

process.dataMediumElectronToIso = process.dataGsfElectronToId.clone()
process.dataMediumElectronToIso.InputDirectoryName = cms.string("MediumElectronToIso")
process.dataMediumElectronToIso.OutputFileName = cms.string("eff_data_medium.root")
process.dataMediumElectronToIso.Categories = cms.PSet(dataIsoCats)
process.dataMediumElectronToIso.Efficiencies = cms.PSet(dataIsoEffs)

process.mcMediumElectronToIso = process.mcGsfElectronToId.clone()
process.mcMediumElectronToIso.InputDirectoryName = cms.string("MediumElectronToIso")
process.mcMediumElectronToIso.OutputFileName = cms.string("eff_mc_medium.root")
process.mcMediumElectronToIso.Categories = cms.PSet(mcIsoCats)
process.mcMediumElectronToIso.Efficiencies = cms.PSet(mcIsoEffs)

process.dataTightElectronToIso = process.dataGsfElectronToId.clone()
process.dataTightElectronToIso.InputDirectoryName = cms.string("TightElectronToIso")
process.dataTightElectronToIso.OutputFileName = cms.string("eff_data_tight.root")
process.dataTightElectronToIso.Categories = cms.PSet(dataIsoCats)
process.dataTightElectronToIso.Efficiencies = cms.PSet(dataIsoEffs)

process.mcTightElectronToIso = process.mcGsfElectronToId.clone()
process.mcTightElectronToIso.InputDirectoryName = cms.string("TightElectronToIso")
process.mcTightElectronToIso.OutputFileName = cms.string("eff_mc_tight.root")
process.mcTightElectronToIso.Categories = cms.PSet(mcIsoCats)
process.mcTightElectronToIso.Efficiencies = cms.PSet(mcIsoEffs)

process.data_seq = cms.Sequence()
process.mc_seq = cms.Sequence()
if not options.noID:
    process.data_seq += process.dataGsfElectronToId
    process.mc_seq += process.mcGsfElectronToId
if not options.noIso:
    process.data_seq += process.dataVetoElectronToIso
    process.data_seq += process.dataLooseElectronToIso
    process.data_seq += process.dataMediumElectronToIso
    process.data_seq += process.dataTightElectronToIso
    process.mc_seq += process.mcVetoElectronToIso
    process.mc_seq += process.mcLooseElectronToIso
    process.mc_seq += process.mcMediumElectronToIso
    process.mc_seq += process.mcTightElectronToIso

process.fit = cms.Path()
if not options.noData:
    process.fit += process.data_seq
if not options.noMC:
    process.fit += process.mc_seq

process.Timing = cms.Service("Timing")
