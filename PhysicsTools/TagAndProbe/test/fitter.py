import FWCore.ParameterSet.Config as cms

process = cms.Process("TagProbe")
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

##                      _              _       
##   ___ ___  _ __  ___| |_ __ _ _ __ | |_ ___ 
##  / __/ _ \| '_ \/ __| __/ _` | '_ \| __/ __|
## | (_| (_) | | | \__ \ || (_| | | | | |_\__ \
##  \___\___/|_| |_|___/\__\__,_|_| |_|\__|___/
##                                              
################################################

isMC = False
InputFileName = "prova.root"
OutputFilePrefix = "efficiency-data-"

################################################
HLTDef = "passingHLT0"
PDFName = "pdfSignalPlusBackground"

if isMC:
    InputFileName = "TnP_MC.root"
    PDFName = "pdfSignalPlusBackground"
    OutputFilePrefix = "efficiency-mc-"
################################################

#specifies the binning of parameters
EfficiencyBins = cms.PSet(probe_sc_et = cms.vdouble( 25, 40 ),
                          probe_sc_abseta = cms.vdouble( 0.0, 1.5, 2.5 )
                          )

## for super clusters
#EfficiencyBinsSC = cms.PSet(probe_et = cms.vdouble( 25, 30, 35, 40, 45, 50, 200 ),
#                            probe_eta = cms.vdouble( -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5 )
#                            )


#### For data: except for HLT step
EfficiencyBinningSpecification = cms.PSet(
    #specifies what unbinned variables to include in the dataset, the mass is needed for the fit
    UnbinnedVariables = cms.vstring("mass"),
    #specifies the binning of parameters
    BinnedVariables = cms.PSet(EfficiencyBins),
    #first string is the default followed by binRegExp - PDFname pairs
    BinToPDFmap = cms.vstring(PDFName)
)


#### For super clusters
#EfficiencyBinningSpecificationSC = cms.PSet(
#    UnbinnedVariables = cms.vstring("mass"),
#    BinnedVariables = cms.PSet(EfficiencyBinsSC),
#    BinToPDFmap = cms.vstring(PDFName)
#)
#EfficiencyBinningSpecificationSCMC = cms.PSet(
#    UnbinnedVariables = cms.vstring("mass"),
#    BinnedVariables = cms.PSet(EfficiencyBinsSC,mcTrue = cms.vstring("true")),
#    BinToPDFmap = cms.vstring()  
#)


#### For MC truth: do truth matching
EfficiencyBinningSpecificationMC = cms.PSet(
    UnbinnedVariables = cms.vstring("mass"),
    BinnedVariables = cms.PSet(probe_sc_et = cms.vdouble( 25, 40 ),
                               probe_sc_abseta = cms.vdouble( 0.0, 1.5, 2.5 ),
                               mcTrue = cms.vstring("true")
                               ),
    BinToPDFmap = cms.vstring(PDFName)  
)

#### For HLT step: just do cut & count
#EfficiencyBinningSpecificationHLT = cms.PSet(
#    UnbinnedVariables = cms.vstring("mass"),
#    BinnedVariables = cms.PSet(EfficiencyBins),
#    BinToPDFmap = cms.vstring()  
#)

##########################################################################################
############################################################################################

if isMC:
    mcTruthModules = cms.PSet(
        MCtruth_Medium = cms.PSet(EfficiencyBinningSpecificationMC,
                                  EfficiencyCategoryAndState = cms.vstring("passingMedium", "pass"),
                                  ),
        )
else:
    mcTruthModules = cms.PSet()

############################################################################################
############################################################################################
####### GsfElectron->Id / selection efficiency 
############################################################################################
############################################################################################

process.GsfElectronToId = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
                                         InputFileNames = cms.vstring(InputFileName),
                                         InputDirectoryName = cms.string("GsfElectronToRECO"),
                                         InputTreeName = cms.string("fitter_tree"),
                                         OutputFileName = cms.string(OutputFilePrefix+"GsfElectronToId.root"),
                                         NumCPU = cms.uint32(8),
                                         SaveWorkspace = cms.bool(True),
                                         floatShapeParameters = cms.bool(True),
                                         binnedFit = cms.bool(True),
                                         binsForFit = cms.uint32(30),
                                         #binsForMassPlots = cms.uint32(120),
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
                                                               passingMedium = cms.vstring("passingMedium", "dummy[pass=1,fail=0]"),
                                                               ),

                                         # defines all the PDFs that will be available for the efficiency calculations; 
                                         # uses RooFit's "factory" syntax;
                                         # each pdf needs to define "signal", "backgroundPass", "backgroundFail" pdfs, "efficiency[0.9,0,1]" 
                                         # and "signalFractionInPassing[0.9]" are used for initial values  
                                         PDFs = cms.PSet(pdfSignalPlusBackground = cms.vstring(
            "RooCBExGaussShape::signalResPass(mass, meanP[0, -5., 5.], sigmaP[1., 0., 5.],alphaP[1.53], nP[.6,0, 1], sigmaP_2[2, 0, 2.], fracP[6e-01,0, 1])",
            "RooCBExGaussShape::signalResFail(mass, meanF[0., -5., 5.], sigmaF[1., 0., 5.],alphaF[1.56], nF[.6, 0,1], sigmaF_2[2, 0, 2.], fracF[6e-01, 0, 1])",
            "ZGeneratorLineShape::signalPhy(mass)", ### NLO line shape
            #"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], betaPass, peakPass[90.0])",
            #"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], betaFail, peakFail[90.0])",
            "RooPolynomial::backgroundPass(mass, aPass[-0.001,-0.01,0.])",
            "RooPolynomial::backgroundFail(mass, aFail[-0.001,-0.01,0.])",
            "FCONV::signalPass(mass, signalPhy, signalResPass)",
            "FCONV::signalFail(mass, signalPhy, signalResFail)",     
            "efficiency[0.5,0,1]",
            "signalFractionInPassing[0.9]"     
            #"RooGaussian::signal(mass, mean2[91.2, 89.0, 93.0], sigma2[2.3, 0.5, 10.0])",
            #"RooExponential::backgroundPass(mass, cPass[-0.02,-5,0])",
            #"RooExponential::backgroundFail(mass, cFail[-0.02,-5,0])",
            #"efficiency[0.9,0,1]",
            #"signalFractionInPassing[1.0]"
            ),
                                                         ),

                                         # defines a set of efficiency calculations, what PDF to use for fitting and how to bin the data;
                                         # there will be a separate output directory for each calculation that includes a simultaneous fit, side band subtraction and counting. 
                                         Efficiencies = cms.PSet(mcTruthModules,
                                                                 #the name of the parameter set becomes the name of the directory
                                                                 Medium = cms.PSet(EfficiencyBinningSpecification,
                                                                                   EfficiencyCategoryAndState = cms.vstring("passingMedium", "pass"),
                                                                                   ),
                                                                 )
                                         )


############################################################################################
############################################################################################
####### SC->GsfElectron efficiency 
############################################################################################
############################################################################################
#if isMC:
#    SCmcTruthModules = cms.PSet(
#        MCtruth_efficiency = cms.PSet(
#        EfficiencyBinningSpecificationSCMC,
#        EfficiencyCategoryAndState = cms.vstring( "probe_passingGsf", "pass" ),
#        ),
#    )
#else:
#    SCmcTruthModules = cms.PSet()    
#
#
#process.SCToGsfElectron = process.GsfElectronToId.clone()
#process.SCToGsfElectron.InputDirectoryName = cms.string("SuperClusterToGsfElectron")
#process.SCToGsfElectron.OutputFileName = cms.string(OutputFilePrefix+"SCToGsfElectron.root")
#process.SCToGsfElectron.Variables = cms.PSet(
#        mass = cms.vstring("Tag-Probe Mass", "60.0", "120.0", "GeV/c^{2}"),
#        probe_et = cms.vstring("Probe E_{T}", "0", "1000", "GeV/c"),
#        probe_eta = cms.vstring("Probe #eta", "-2.5", "2.5", ""),                
#    )
#process.SCToGsfElectron.Categories = cms.PSet(
#    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),           
#    probe_passingGsf = cms.vstring("probe_passingGsf", "dummy[pass=1,fail=0]"),                        
#    )
#process.SCToGsfElectron.Efficiencies = cms.PSet(
#    SCmcTruthModules,
#    efficiency = cms.PSet(
#    EfficiencyBinningSpecificationSC,
#    EfficiencyCategoryAndState = cms.vstring( "probe_passingGsf", "pass" ),
#    ),
#)
#
#############################################################################################
#############################################################################################
######## HLT efficiency 
#############################################################################################
#############################################################################################
#
#
#if isMC:
#    HLTmcTruthModules = cms.PSet(
#        MCtruth_efficiency = cms.PSet(
#        EfficiencyBinningSpecificationMC,
#        EfficiencyCategoryAndState = cms.vstring( HLTDef, "pass" ),
#        ),    
#    )
#else:
#    HLTmcTruthModules = cms.PSet()
#
#
#EfficienciesPset = cms.PSet(
#    HLTmcTruthModules,
#    efficiency = cms.PSet(
#    EfficiencyBinningSpecificationHLT,
#    EfficiencyCategoryAndState = cms.vstring( HLTDef, "pass" ),
#    ),
#)
#
#########
#process.WP95ToHLT = process.GsfElectronToId.clone()
#process.WP95ToHLT.InputDirectoryName = cms.string("WP95ToHLT")
#process.WP95ToHLT.OutputFileName = cms.string(OutputFilePrefix+"WP95ToHLT.root")
#process.WP95ToHLT.Categories = cms.PSet(
#    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),           
#    probe_passingHLT = cms.vstring("probe_passingHLT", "dummy[pass=1,fail=0]"), 
#    )

process.fit = cms.Path(
    process.GsfElectronToId  
    #process.SCToGsfElectron + 
    #process.WP90ToHLT +
    )
