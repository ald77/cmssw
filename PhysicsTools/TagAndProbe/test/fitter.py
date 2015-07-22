import FWCore.ParameterSet.Config as cms

process = cms.Process("TagProbe")
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

################################################
##                      _              _       
##   ___ ___  _ __  ___| |_ __ _ _ __ | |_ ___ 
##  / __/ _ \| '_ \/ __| __/ _` | '_ \| __/ __|
## | (_| (_) | | | \__ \ || (_| | | | | |_\__ \
##  \___\___/|_| |_|___/\__\__,_|_| |_|\__|___/
##                                              
################################################

isMC = True
InputFileName = "TnPTree.root"
OutputFilePrefix = "efficiency-data-"
PDFName = "gaussPlusLinear"
HLTDef = "passingHLT0"

if isMC:
    InputFileName = "TnPTree.root"
    PDFName = "gaussPlusLinear"
    OutputFilePrefix = "efficiency-mc-"

################################################
#specifies the binning of parameters
EfficiencyBins = cms.PSet(probe_sc_et = cms.vdouble( 25, 40 ),
                          probe_sc_abseta = cms.vdouble( 0.0, 1.5, 2.5 )
                          )

#### For data: except for HLT step
EfficiencyBinningSpecification = cms.PSet(
    #specifies what unbinned variables to include in the dataset, the mass is needed for the fit
    UnbinnedVariables = cms.vstring("mass"),
    #specifies the binning of parameters
    BinnedVariables = cms.PSet(EfficiencyBins),
    #first string is the default followed by binRegExp - PDFname pairs
    BinToPDFmap = cms.vstring(PDFName)
    )

#### For MC truth: do truth matching
EfficiencyBinningSpecificationMC = cms.PSet(
    UnbinnedVariables = cms.vstring("mass"),
    BinnedVariables = cms.PSet(EfficiencyBins,
                               mcTrue = cms.vstring("true")
                               ),
    BinToPDFmap = cms.vstring(PDFName)  
    )

############################################################################################

MCtruth_Veto = cms.PSet(EfficiencyBinningSpecificationMC,
                        EfficiencyCategoryAndState = cms.vstring("passingVeto","pass"),
                        )
MCtruth_Loose = cms.PSet(EfficiencyBinningSpecificationMC,
                         EfficiencyCategoryAndState = cms.vstring("passingLoose","pass"),
                         )
MCtruth_Medium = cms.PSet(EfficiencyBinningSpecificationMC,
                          EfficiencyCategoryAndState = cms.vstring("passingMedium","pass"),
                          )
MCtruth_Tight = cms.PSet(EfficiencyBinningSpecificationMC,
                         EfficiencyCategoryAndState = cms.vstring("passingTight","pass"),
                         )
Eff_Veto = cms.PSet(EfficiencyBinningSpecification,
                      EfficiencyCategoryAndState = cms.vstring("passingVeto","pass"),
                      )
Eff_Loose = cms.PSet(EfficiencyBinningSpecification,
                     EfficiencyCategoryAndState = cms.vstring("passingLoose","pass"),
                     )
Eff_Medium = cms.PSet(EfficiencyBinningSpecification,
                      EfficiencyCategoryAndState = cms.vstring("passingMedium","pass"),
                      )
Eff_Tight = cms.PSet(EfficiencyBinningSpecification,
                     EfficiencyCategoryAndState = cms.vstring("passingTight","pass"),
                     )

if not isMC:
    MCtruth_Veto = cms.PSet()
    MCtruth_Loose = cms.PSet()
    MCtruth_Medium = cms.PSet()
    MCtruth_Tight = cms.PSet()

############################################################################################
############################################################################################
####### GsfElectron->Id / selection efficiency 
############################################################################################
############################################################################################

process.GsfElectronToId = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
                                         InputFileNames = cms.vstring(InputFileName),
                                         InputDirectoryName = cms.string("TightElectronToMiniIso"),
                                         InputTreeName = cms.string("fitter_tree"), 
                                         OutputFileName = cms.string(OutputFilePrefix+"GsfElectronToId.root"),
                                         NumCPU = cms.uint32(8),
                                         SaveWorkspace = cms.bool(True),
                                         floatShapeParameters = cms.bool(True),
                                         binnedFit = cms.bool(True),
                                         binsForFit = cms.uint32(30),
                                         #WeightVariable = cms.string("weight"),
                                         #fixVars = cms.vstring("mean"),
                                         
                                         # defines all the real variables of the probes available in the input tree and intended for use in the efficiencies
                                         Variables = cms.PSet(mass = cms.vstring("Tag-Probe Mass", "60.0", "120.0", "GeV/c^{2}"),
                                                              probe_sc_et = cms.vstring("Probe E_{T}", "0", "1000", "GeV/c"),
                                                              probe_sc_abseta = cms.vstring("Probe #eta", "0", "2.5", ""),                
                                                              ),

                                         # defines all the discrete variables of the probes available in the input tree and intended for use in the efficiency calculations
                                         Categories = cms.PSet(mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
                                                               #probe_passConvRej = cms.vstring("probe_passConvRej", "dummy[pass=1,fail=0]"), 
                                                               passingTight = cms.vstring("passingTight", "dummy[pass=1,fail=0]"),
                                                               ),

                                         # defines all the PDFs that will be available for the efficiency calculations; 
                                         # uses RooFit's "factory" syntax;
                                         # each pdf needs to define "signal", "backgroundPass", "backgroundFail" pdfs, "efficiency[0.9,0,1]" 
                                         # and "signalFractionInPassing[0.9]" are used for initial values  
                                         PDFs = cms.PSet(pdfSignalPlusBackground = cms.vstring(
            "RooCBExGaussShape::signalResPass(mass, meanP[0, -5., 5.], sigmaP[1., 0., 5.],alphaP[0.01, 0, 5], nP[.6,0, 1], sigmaP_2[2, 0, 2.], fracP[6e-01,0, 1])",
            "RooCBExGaussShape::signalResFail(mass, meanF[0., -5., 5.], sigmaF[1., 0., 5.],alphaF[0.01, 0, 5], nF[.6, 0,1], sigmaF_2[2, 0, 2.], fracF[6e-01, 0, 1])",
            "ZGeneratorLineShape::signalPhy(mass)", ### NLO line shape
            "RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], betaPass, peakPass[90.0])",
            "RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], betaFail, peakFail[90.0])",
            "FCONV::signalPass(mass, signalPhy, signalResPass)",
            "FCONV::signalFail(mass, signalPhy, signalResFail)",     
            "efficiency[0.5,0,1]",
            "signalFractionInPassing[1.0]"     
            ),

                                                         gaussPlusLinear = cms.vstring(
            "Voigtian::signal(mass, mean[91.2, 84.0, 98.0], width[2.4, 0.5, 5.0], sigma[5., 1., 12.0])",
            "RooExponential::backgroundPass(mass, cPass[0,-2,2])",
            "RooExponential::backgroundFail(mass, cFail[0,-2,2])",
            "efficiency[0.95,0,1]",
            "signalFractionInPassing[0.95]"
            ),
                                                         gaussPlusQuadratic = cms.vstring(
            "Voigtian::signal(mass, mean[91.2, 89.0, 93.0], width[2.4, 0.5, 5.0], sigma[5., 1., 12.0])",
            "RooExponential::backgroundPass(mass, cPass[0,-2,2])",
            #             "Chebychev::backgroundPass(mass, {cPass1[0,-2,2], cPass2[0,-2,2]})",
            "Chebychev::backgroundFail(mass, {cFail1[0,-2,2], cFail2[0,-2,2]})",
            "efficiency[0.95,0,1]", 
            "signalFractionInPassing[0.95]"
            ),
                                                         gaussPlusArgus = cms.vstring(
            "Voigtian::signal(mass, mean[91.2, 89.0, 93.0], width[2.4, 0.5, 5.0], sigma[5., 1., 12.0])",
            "RooExponential::backgroundPass(mass, cPass[0,-5,5])",
            "ArgusBG::backgroundFail(mass, cFail1[86.6, 70, 100], cFail2[-2.8, -100, 100])",
            "efficiency[0.95,0,1]",
            "signalFractionInPassing[0.95]"
            ),
                                                         gaussPlusCMS = cms.vstring(
            "Voigtian::signal(mass, mean[91.2, 89.0, 93.0], width[2.4, 0.5, 5.0], sigma[5., 1., 12.0])",
            #            "RooExponential::backgroundPass(mass, cPass[0,-2,2])",
            "RooCMSShape::backgroundPass(mass, alphaPass[60.,30.,90.], betaPass[0.001, 0.,0.1], betaPass, peakPass[90.0])",
            "RooCMSShape::backgroundFail(mass, alphaFail[60.,30.,90.], betaFail[0.001, 0.,0.1], betaFail, peakFail[90.0])",
            "efficiency[0.95,0,1]",
            "signalFractionInPassing[0.95]"
            ),
                                                         gaussPlusCubic = cms.vstring(
            "Voigtian::signal(mass, mean[91.2, 84.0, 98.0], width[2.4, 0.5, 5.0], sigma[5., 1., 12.0])",
            #             "Chebychev::backgroundPass(mass, {cPass1[0,-2,2], cPass2[0,-2,2],cPass3[0,-2,2]})", 
            #             "Chebychev::backgroundFail(mass, {cFail1[0,-2,2], cFail2[0,-2,2],cFail3[0,-2,2]})",     
            "Chebychev::backgroundPass(mass, {cPass1[0,-2,2], cPass2[0,-2,2],cPass3[0,-2,2],cPass4[0,-2,2]})", 
            "Chebychev::backgroundFail(mass, {cFail1[0,-2,2], cFail2[0,-2,2],cFail3[0,-2,2],cFail4[0,-2,2]})",     
            "efficiency[0.95,0,1]", 
            "signalFractionInPassing[0.95]" 
            ),
                                                         vpvPlusExpo = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
            "SUM::signal(vFrac[0.8,0,1]*signal1, signal2)",
            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
            ),
                                                         ),

                                         # defines a set of efficiency calculations, what PDF to use for fitting and how to bin the data;
                                         # there will be a separate output directory for each calculation that includes a simultaneous fit, side band subtraction and counting. 
                                         Efficiencies = cms.PSet(
        TruthVeto = MCtruth_Veto.clone(),
        Veto = Eff_Veto.clone()
        )
                                         )

process.GsfElectronToVetoId = process.GsfElectronToId.clone()
process.GsfElectronToVetoId.InputDirectoryName = cms.string("GsfElectronToID")
process.GsfElectronToVetoId.OutputFileName = cms.string(OutputFilePrefix+"GsfElectronToVetoId.root")
process.GsfElectronToVetoId.Categories = cms.PSet(mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
                                                  passingVeto = cms.vstring("passingVeto","dummy[pass=1,fail=0]"),
                                                  )
process.GsfElectronToVetoId.Efficiencies = cms.PSet(
    TruthVeto = MCtruth_Veto.clone(),
    Veto = Eff_Veto.clone()
    )

process.GsfElectronToLooseId = process.GsfElectronToId.clone()
process.GsfElectronToLooseId.InputDirectoryName = cms.string("GsfElectronToID")
process.GsfElectronToLooseId.OutputFileName = cms.string(OutputFilePrefix+"GsfElectronToLooseId.root")
process.GsfElectronToLooseId.Categories = cms.PSet(mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
                                                  passingLoose = cms.vstring("passingLoose","dummy[pass=1,fail=0]"),
                                                  )
process.GsfElectronToLooseId.Efficiencies = cms.PSet(
    TruthLoose = MCtruth_Loose.clone(),
    Loose = Eff_Loose.clone()
    )

process.GsfElectronToMediumId = process.GsfElectronToId.clone()
process.GsfElectronToMediumId.InputDirectoryName = cms.string("GsfElectronToID")
process.GsfElectronToMediumId.OutputFileName = cms.string(OutputFilePrefix+"GsfElectronToMediumId.root")
process.GsfElectronToMediumId.Categories = cms.PSet(mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
                                                    passingMedium = cms.vstring("passingMedium","dummy[pass=1,fail=0]"),
                                                    )
process.GsfElectronToMediumId.Efficiencies = cms.PSet(
    TruthMedium = MCtruth_Medium.clone(),
    Medium = Eff_Medium.clone()
    )

process.GsfElectronToTightId = process.GsfElectronToId.clone()
process.GsfElectronToTightId.InputDirectoryName = cms.string("GsfElectronToID")
process.GsfElectronToTightId.OutputFileName = cms.string(OutputFilePrefix+"GsfElectronToTightId.root")
process.GsfElectronToTightId.Categories = cms.PSet(mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
                                                   passingTight = cms.vstring("passingTight","dummy[pass=1,fail=0]"),
                                                   )
process.GsfElectronToTightId.Efficiencies = cms.PSet(
    TruthTight = MCtruth_Tight.clone(),
    Tight = Eff_Tight.clone()
    )

process.VetoElectronToMiniIso = process.GsfElectronToId.clone()
process.VetoElectronToMiniIso.InputDirectoryName = cms.string("VetoElectronToMiniIso")
process.VetoElectronToMiniIso.OutputFileName = cms.string(OutputFilePrefix+"VetoElectronToMiniIso.root")
process.VetoElectronToMiniIso.Categories = cms.PSet(mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
                                                    passingVeto = cms.vstring("passingVeto","dummy[pass=1,fail=0]"),
                                                    )
process.VetoElectronToMiniIso.Efficiencies = cms.PSet(
    TruthVeto = MCtruth_Veto.clone(),
    Veto = Eff_Veto.clone()
    )

process.LooseElectronToMiniIso = process.GsfElectronToId.clone()
process.LooseElectronToMiniIso.InputDirectoryName = cms.string("LooseElectronToMiniIso")
process.LooseElectronToMiniIso.OutputFileName = cms.string(OutputFilePrefix+"LooseElectronToMiniIso.root")
process.LooseElectronToMiniIso.Categories = cms.PSet(mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
                                                     passingLoose = cms.vstring("passingLoose","dummy[pass=1,fail=0]"),
                                                     )
process.LooseElectronToMiniIso.Efficiencies = cms.PSet(
    TruthLoose = MCtruth_Loose.clone(),
    Loose = Eff_Loose.clone()
    )

process.MediumElectronToMiniIso = process.GsfElectronToId.clone()
process.MediumElectronToMiniIso.InputDirectoryName = cms.string("MediumElectronToMiniIso")
process.MediumElectronToMiniIso.OutputFileName = cms.string(OutputFilePrefix+"MediumElectronToMiniIso.root")
process.MediumElectronToMiniIso.Categories = cms.PSet(mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
                                                      passingMedium = cms.vstring("passingMedium","dummy[pass=1,fail=0]"),
                                                      )
process.MediumElectronToMiniIso.Efficiencies = cms.PSet(
    TruthMedium = MCtruth_Medium.clone(),
    Medium = Eff_Medium.clone()
    )

process.TightElectronToMiniIso = process.GsfElectronToId.clone()
process.TightElectronToMiniIso.InputDirectoryName = cms.string("TightElectronToMiniIso")
process.TightElectronToMiniIso.OutputFileName = cms.string(OutputFilePrefix+"TightElectronToMiniIso.root")
process.TightElectronToMiniIso.Categories = cms.PSet(mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
                                                     passingTight = cms.vstring("passingTight","dummy[pass=1,fail=0]"),
                                                     )
process.TightElectronToMiniIso.Efficiencies = cms.PSet(
    TruthTight = MCtruth_Tight.clone(),
    Tight = Eff_Tight.clone()
    )

process.fit = cms.Path(
#    process.GsfElectronToId  +
    process.GsfElectronToVetoId + 
    process.GsfElectronToLooseId + 
    process.GsfElectronToMediumId + 
    process.GsfElectronToTightId + 
    process.VetoElectronToMiniIso +
    process.LooseElectronToMiniIso +
    process.MediumElectronToMiniIso +
    process.TightElectronToMiniIso
    )
