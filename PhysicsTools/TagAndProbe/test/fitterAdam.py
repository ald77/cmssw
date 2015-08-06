import FWCore.ParameterSet.Config as cms

process = cms.Process("TagProbe")
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout','cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

pdfName = "gaussPlusLinear"

measBinnedVariables = cms.PSet(
    probe_sc_et = cms.vdouble(20., 1000.),
    probe_sc_abseta = cms.vdouble(0., 1.5, 2.5),
)
dataVariables = cms.PSet(
    mass = cms.vstring("Tag-Probe Mass", "60.0", "120.0", " GeV/c^{2}"),
    probe_sc_et = cms.vstring("Probe E_{T}", "0", "1000", "GeV/c"),
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
    BinToPDFmap = cms.vstring(pdfName),
)
mcVars = trueVars.clone()
mcVars.BinnedVariables = measBinnedVariables
dataVars = mcVars.clone()
dataVars.UnbinnedVariables = dataUnbinnedVariables

trueVeto = cms.PSet(trueVars, EfficiencyCategoryAndState = cms.vstring("passingVeto","pass"))
trueLoose = cms.PSet(trueVars, EfficiencyCategoryAndState = cms.vstring("passingLoose","pass"))
trueMedium = cms.PSet(trueVars, EfficiencyCategoryAndState = cms.vstring("passingMedium","pass"))
trueTight = cms.PSet(trueVars, EfficiencyCategoryAndState = cms.vstring("passingTight","pass"))
mcVeto = cms.PSet(mcVars, EfficiencyCategoryAndState = cms.vstring("passingVeto","pass"))
mcLoose = cms.PSet(mcVars, EfficiencyCategoryAndState = cms.vstring("passingLoose","pass"))
mcMedium = cms.PSet(mcVars, EfficiencyCategoryAndState = cms.vstring("passingMedium","pass"))
mcTight = cms.PSet(mcVars, EfficiencyCategoryAndState = cms.vstring("passingTight","pass"))
dataVeto = cms.PSet(dataVars, EfficiencyCategoryAndState = cms.vstring("passingVeto","pass"))
dataLoose = cms.PSet(dataVars, EfficiencyCategoryAndState = cms.vstring("passingLoose","pass"))
dataMedium = cms.PSet(dataVars, EfficiencyCategoryAndState = cms.vstring("passingMedium","pass"))
dataTight = cms.PSet(dataVars, EfficiencyCategoryAndState = cms.vstring("passingTight","pass"))

mcVariables = cms.PSet(dataVariables, PUweight = cms.vstring("PU weight", "0", "100", ""))

catMCTrue = cms.vstring("MC true", "dummy[true=1,false=0]")
catVeto = cms.vstring("passingVeto", "dummy[pass=1,fail=0]")
catLoose = cms.vstring("passingLoose", "dummy[pass=1,fail=0]")
catMedium = cms.vstring("passingMedium", "dummy[pass=1,fail=0]")
catTight = cms.vstring("passingTight", "dummy[pass=1,fail=0]")

process.dataGsfElectronToId = cms.EDAnalyzer(
    "TagProbeFitTreeAnalyzer",
    InputFileNames = cms.vstring("TnPTree_data.root"),
    InputDirectoryName = cms.string("GsfElectronToID"),
    InputTreeName = cms.string("fitter_tree"),
    OutputFileName = cms.string("eff_data_id.root"),
    NumCPU = cms.uint32(1),
    SaveWorkspace = cms.bool(True),
    floatShapeParameters = cms.bool(True),
    binnedFit = cms.bool(True),
    binsForFit = cms.uint32(60),
    Variables = dataVariables,
    Categories = cms.PSet(
        passingVeto = catVeto,
        passingLoose = catLoose,
        passingMedium = catMedium,
        passingTight = catTight,
        ),
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
            "signalFractionInPassing[1.0]",
            ),
        gaussPlusLinear = cms.vstring(
            "Voigtian::signal(mass, mean[91.2, 84.0, 98.0], width[2.4, 0.5, 5.0], sigma[5., 1., 12.0])",
            "RooExponential::backgroundPass(mass, cPass[0,-2,2])",
            "RooExponential::backgroundFail(mass, cFail[0,-2,2])",
            "efficiency[0.95,0,1]",
            "signalFractionInPassing[0.95]"
            ),
        ),
    Efficiencies = cms.PSet(
        Veto = dataVeto,
        Loose = dataLoose,
        Medium = dataMedium,
        Tight = dataTight),
    )

process.mcGsfElectronToId = process.dataGsfElectronToId.clone()
process.mcGsfElectronToId.InputFileNames = cms.vstring("TnPTree_mc.root")
process.mcGsfElectronToId.OutputFileName = cms.string("eff_mc_id.root")
process.mcGsfElectronToId.WeightVariable = cms.string("PUweight")
process.mcGsfElectronToId.Variables = mcVariables
process.mcGsfElectronToId.Categories = cms.PSet(
    mcTrue = catMCTrue,
    passingVeto = catVeto,
    passingLoose = catLoose,
    passingMedium = catMedium,
    passingTight = catTight,
    )
process.mcGsfElectronToId.Efficiencies = cms.PSet(
    MCtruth_Veto = trueVeto, 
    MCtruth_Loose = trueLoose,
    MCtruth_Medium = trueMedium,
    MCtruth_Tight = trueTight,
    Veto = mcVeto,
    Loose = mcLoose,
    Medium = mcMedium,
    Tight = mcTight
)

process.dataVetoElectronToMiniIso = process.dataGsfElectronToId.clone()
process.dataVetoElectronToMiniIso.InputDirectoryName = cms.string("VetoElectronToMiniIso")
process.dataVetoElectronToMiniIso.OutputFileName = cms.string("eff_data_veto.root")
process.dataVetoElectronToMiniIso.Categories = cms.PSet(passingVeto = catVeto)
process.dataVetoElectronToMiniIso.Efficiencies = cms.PSet(Veto = dataVeto)

process.mcVetoElectronToMiniIso = process.mcGsfElectronToId.clone()
process.mcVetoElectronToMiniIso.InputDirectoryName = cms.string("VetoElectronToMiniIso")
process.mcVetoElectronToMiniIso.OutputFileName = cms.string("eff_mc_veto.root")
process.mcVetoElectronToMiniIso.Categories = cms.PSet(mcTrue = catMCTrue, passingVeto = catVeto)
process.mcVetoElectronToMiniIso.Efficiencies = cms.PSet(MCtruth_Veto = trueVeto, Veto = mcVeto)

process.dataLooseElectronToMiniIso = process.dataGsfElectronToId.clone()
process.dataLooseElectronToMiniIso.InputDirectoryName = cms.string("LooseElectronToMiniIso")
process.dataLooseElectronToMiniIso.OutputFileName = cms.string("eff_data_loose.root")
process.dataLooseElectronToMiniIso.Categories = cms.PSet(passingLoose = catLoose)
process.dataLooseElectronToMiniIso.Efficiencies = cms.PSet(Loose = dataLoose)

process.mcLooseElectronToMiniIso = process.mcGsfElectronToId.clone()
process.mcLooseElectronToMiniIso.InputDirectoryName = cms.string("LooseElectronToMiniIso")
process.mcLooseElectronToMiniIso.OutputFileName = cms.string("eff_mc_loose.root")
process.mcLooseElectronToMiniIso.Categories = cms.PSet(mcTrue = catMCTrue, passingLoose = catLoose)
process.mcLooseElectronToMiniIso.Efficiencies = cms.PSet(MCtruth_Loose = trueLoose, Loose = mcLoose)

process.dataMediumElectronToMiniIso = process.dataGsfElectronToId.clone()
process.dataMediumElectronToMiniIso.InputDirectoryName = cms.string("MediumElectronToMiniIso")
process.dataMediumElectronToMiniIso.OutputFileName = cms.string("eff_data_medium.root")
process.dataMediumElectronToMiniIso.Categories = cms.PSet(passingMedium = catMedium)
process.dataMediumElectronToMiniIso.Efficiencies = cms.PSet(Medium = dataMedium)

process.mcMediumElectronToMiniIso = process.mcGsfElectronToId.clone()
process.mcMediumElectronToMiniIso.InputDirectoryName = cms.string("MediumElectronToMiniIso")
process.mcMediumElectronToMiniIso.OutputFileName = cms.string("eff_mc_medium.root")
process.mcMediumElectronToMiniIso.Categories = cms.PSet(mcTrue = catMCTrue, passingMedium = catMedium)
process.mcMediumElectronToMiniIso.Efficiencies = cms.PSet(MCtruth_Medium = trueMedium, Medium = mcMedium)

process.dataTightElectronToMiniIso = process.dataGsfElectronToId.clone()
process.dataTightElectronToMiniIso.InputDirectoryName = cms.string("TightElectronToMiniIso")
process.dataTightElectronToMiniIso.OutputFileName = cms.string("eff_data_tight.root")
process.dataTightElectronToMiniIso.Categories = cms.PSet(passingTight = catTight)
process.dataTightElectronToMiniIso.Efficiencies = cms.PSet(Tight = dataTight)

process.mcTightElectronToMiniIso = process.mcGsfElectronToId.clone()
process.mcTightElectronToMiniIso.InputDirectoryName = cms.string("TightElectronToMiniIso")
process.mcTightElectronToMiniIso.OutputFileName = cms.string("eff_mc_tight.root")
process.mcTightElectronToMiniIso.Categories = cms.PSet(mcTrue = catMCTrue, passingTight = catTight)
process.mcTightElectronToMiniIso.Efficiencies = cms.PSet(MCtruth_Tight = trueTight, Tight = mcTight)

process.fit = cms.Path(
    process.dataGsfElectronToId +
    process.mcGsfElectronToId +
    process.dataVetoElectronToMiniIso +
    process.mcVetoElectronToMiniIso +
    process.dataLooseElectronToMiniIso +
    process.mcLooseElectronToMiniIso +
    process.dataMediumElectronToMiniIso +
    process.mcMediumElectronToMiniIso +
    process.dataTightElectronToMiniIso +
    process.mcTightElectronToMiniIso
)
