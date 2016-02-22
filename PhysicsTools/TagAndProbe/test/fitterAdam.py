import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
import PhysicsTools.TagAndProbe.commonFit as common

def BinSpec(name):
    return cms.vstring(
        "ERROR_TEMPLATE_NOT_FOUND_ERROR",
        "*probe_Ele_pt_bin0*probe_sc_abseta_bin0*",name+"_barrel_10p0To20p0_0p0To1p442",
        "*probe_Ele_pt_bin1*probe_sc_abseta_bin0*",name+"_barrel_20p0To30p0_0p0To1p442",
        "*probe_Ele_pt_bin2*probe_sc_abseta_bin0*",name+"_barrel_30p0To40p0_0p0To1p442",
        "*probe_Ele_pt_bin3*probe_sc_abseta_bin0*",name+"_barrel_40p0To50p0_0p0To1p442",
        "*probe_Ele_pt_bin4*probe_sc_abseta_bin0*",name+"_barrel_50p0To200p0_0p0To1p442",
        "*probe_Ele_pt_bin0*probe_sc_abseta_bin1*",name+"_barrel_10p0To20p0_0p0To1p442",
        "*probe_Ele_pt_bin1*probe_sc_abseta_bin1*",name+"_barrel_20p0To30p0_0p0To1p442",
        "*probe_Ele_pt_bin2*probe_sc_abseta_bin1*",name+"_barrel_30p0To40p0_0p0To1p442",
        "*probe_Ele_pt_bin3*probe_sc_abseta_bin1*",name+"_barrel_40p0To50p0_0p0To1p442",
        "*probe_Ele_pt_bin4*probe_sc_abseta_bin1*",name+"_barrel_50p0To200p0_0p0To1p442",
        "*probe_Ele_pt_bin0*probe_sc_abseta_bin2*",name+"_crack_10p0To20p0_1p442To1p566",
        "*probe_Ele_pt_bin1*probe_sc_abseta_bin2*",name+"_crack_20p0To30p0_1p442To1p566",
        "*probe_Ele_pt_bin2*probe_sc_abseta_bin2*",name+"_crack_30p0To40p0_1p442To1p566",
        "*probe_Ele_pt_bin3*probe_sc_abseta_bin2*",name+"_crack_40p0To50p0_1p442To1p566",
        "*probe_Ele_pt_bin4*probe_sc_abseta_bin2*",name+"_crack_50p0To200p0_1p442To1p566",
        "*probe_Ele_pt_bin0*probe_sc_abseta_bin3*",name+"_endcap_10p0To20p0_1p566To2p5",
        "*probe_Ele_pt_bin1*probe_sc_abseta_bin3*",name+"_endcap_20p0To30p0_1p566To2p5",
        "*probe_Ele_pt_bin2*probe_sc_abseta_bin3*",name+"_endcap_30p0To40p0_1p566To2p5",
        "*probe_Ele_pt_bin3*probe_sc_abseta_bin3*",name+"_endcap_40p0To50p0_1p566To2p5",
        "*probe_Ele_pt_bin4*probe_sc_abseta_bin3*",name+"_endcap_50p0To200p0_1p566To2p5",
        "*probe_Ele_pt_bin0*probe_sc_abseta_bin4*",name+"_endcap_10p0To20p0_1p566To2p5",
        "*probe_Ele_pt_bin1*probe_sc_abseta_bin4*",name+"_endcap_20p0To30p0_1p566To2p5",
        "*probe_Ele_pt_bin2*probe_sc_abseta_bin4*",name+"_endcap_30p0To40p0_1p566To2p5",
        "*probe_Ele_pt_bin3*probe_sc_abseta_bin4*",name+"_endcap_40p0To50p0_1p566To2p5",
        "*probe_Ele_pt_bin4*probe_sc_abseta_bin4*",name+"_endcap_50p0To200p0_1p566To2p5",
        "*probe_Ele_pt_bin0*probe_ele_RelAct_bin*",name+"_alleta_10p0To20p0_0p0To2p5",
        "*probe_Ele_pt_bin1*probe_ele_RelAct_bin*",name+"_alleta_20p0To30p0_0p0To2p5",
        "*probe_Ele_pt_bin2*probe_ele_RelAct_bin*",name+"_alleta_30p0To40p0_0p0To2p5",
        "*probe_Ele_pt_bin3*probe_ele_RelAct_bin*",name+"_alleta_40p0To50p0_0p0To2p5",
        "*probe_Ele_pt_bin4*probe_ele_RelAct_bin*",name+"_alleta_50p0To200p0_0p0To2p5",
        "*probe_Ele_pt_bin0*event_nPV_bin*",name+"_alleta_10p0To20p0_0p0To2p5",
        "*probe_Ele_pt_bin1*event_nPV_bin*",name+"_alleta_20p0To30p0_0p0To2p5",
        "*probe_Ele_pt_bin2*event_nPV_bin*",name+"_alleta_30p0To40p0_0p0To2p5",
        "*probe_Ele_pt_bin3*event_nPV_bin*",name+"_alleta_40p0To50p0_0p0To2p5",
        "*probe_Ele_pt_bin4*event_nPV_bin*",name+"_alleta_50p0To200p0_0p0To2p5",
        )

def BinSpec2(name):
    return cms.vstring(
        "ERROR_TEMPLATE_NOT_FOUND_ERROR",
        "*probe_Ele_pt_bin0*probe_sc_abseta_bin0*",name+"_barrel_10p0To20p0_0p0To0p8",
        "*probe_Ele_pt_bin1*probe_sc_abseta_bin0*",name+"_barrel_20p0To30p0_0p0To0p8",
        "*probe_Ele_pt_bin2*probe_sc_abseta_bin0*",name+"_barrel_30p0To40p0_0p0To0p8",
        "*probe_Ele_pt_bin3*probe_sc_abseta_bin0*",name+"_barrel_40p0To50p0_0p0To0p8",
        "*probe_Ele_pt_bin4*probe_sc_abseta_bin0*",name+"_barrel_50p0To200p0_0p0To0p8",
        "*probe_Ele_pt_bin0*probe_sc_abseta_bin1*",name+"_barrel_10p0To20p0_0p8To1p442",
        "*probe_Ele_pt_bin1*probe_sc_abseta_bin1*",name+"_barrel_20p0To30p0_0p8To1p442",
        "*probe_Ele_pt_bin2*probe_sc_abseta_bin1*",name+"_barrel_30p0To40p0_0p8To1p442",
        "*probe_Ele_pt_bin3*probe_sc_abseta_bin1*",name+"_barrel_40p0To50p0_0p8To1p442",
        "*probe_Ele_pt_bin4*probe_sc_abseta_bin1*",name+"_barrel_50p0To200p0_0p8To1p442",
        "*probe_Ele_pt_bin0*probe_sc_abseta_bin2*",name+"_crack_10p0To20p0_1p442To1p566",
        "*probe_Ele_pt_bin1*probe_sc_abseta_bin2*",name+"_crack_20p0To30p0_1p442To1p566",
        "*probe_Ele_pt_bin2*probe_sc_abseta_bin2*",name+"_crack_30p0To40p0_1p442To1p566",
        "*probe_Ele_pt_bin3*probe_sc_abseta_bin2*",name+"_crack_40p0To50p0_1p442To1p566",
        "*probe_Ele_pt_bin4*probe_sc_abseta_bin2*",name+"_crack_50p0To200p0_1p442To1p566",
        "*probe_Ele_pt_bin0*probe_sc_abseta_bin3*",name+"_endcap_10p0To20p0_1p566To2p0",
        "*probe_Ele_pt_bin1*probe_sc_abseta_bin3*",name+"_endcap_20p0To30p0_1p566To2p0",
        "*probe_Ele_pt_bin2*probe_sc_abseta_bin3*",name+"_endcap_30p0To40p0_1p566To2p0",
        "*probe_Ele_pt_bin3*probe_sc_abseta_bin3*",name+"_endcap_40p0To50p0_1p566To2p0",
        "*probe_Ele_pt_bin4*probe_sc_abseta_bin3*",name+"_endcap_50p0To200p0_1p566To2p0",
        "*probe_Ele_pt_bin0*probe_sc_abseta_bin4*",name+"_endcap_10p0To20p0_2p0To2p5",
        "*probe_Ele_pt_bin1*probe_sc_abseta_bin4*",name+"_endcap_20p0To30p0_2p0To2p5",
        "*probe_Ele_pt_bin2*probe_sc_abseta_bin4*",name+"_endcap_30p0To40p0_2p0To2p5",
        "*probe_Ele_pt_bin3*probe_sc_abseta_bin4*",name+"_endcap_40p0To50p0_2p0To2p5",
        "*probe_Ele_pt_bin4*probe_sc_abseta_bin4*",name+"_endcap_50p0To200p0_2p0To2p5",
        "*probe_Ele_pt_bin0*probe_ele_RelAct_bin*",name+"_alleta_10p0To20p0_0p0To2p5",
        "*probe_Ele_pt_bin1*probe_ele_RelAct_bin*",name+"_alleta_20p0To30p0_0p0To2p5",
        "*probe_Ele_pt_bin2*probe_ele_RelAct_bin*",name+"_alleta_30p0To40p0_0p0To2p5",
        "*probe_Ele_pt_bin3*probe_ele_RelAct_bin*",name+"_alleta_40p0To50p0_0p0To2p5",
        "*probe_Ele_pt_bin4*probe_ele_RelAct_bin*",name+"_alleta_50p0To200p0_0p0To2p5",
        "*probe_Ele_pt_bin0*event_nPV_bin*",name+"_alleta_10p0To20p0_0p0To2p5",
        "*probe_Ele_pt_bin1*event_nPV_bin*",name+"_alleta_20p0To30p0_0p0To2p5",
        "*probe_Ele_pt_bin2*event_nPV_bin*",name+"_alleta_30p0To40p0_0p0To2p5",
        "*probe_Ele_pt_bin3*event_nPV_bin*",name+"_alleta_40p0To50p0_0p0To2p5",
        "*probe_Ele_pt_bin4*event_nPV_bin*",name+"_alleta_50p0To200p0_0p0To2p5",
        )

options = VarParsing('analysis')

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
    "doEta",
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Bin in eta instead of activity for isolation efficiencies"
    )

options.parseArguments()

if (not options.noMC) and (not options.noData):
    raise Exception("Must select either data or MC")

if (not options.noData):
    for pdf in common.all_pdfs.__dict__:
        param = common.all_pdfs.getParameter(pdf)
        if type(param) is not cms.vstring:
            continue
        i = 0
        for line in getattr(common.all_pdfs, pdf):
            if line.find("signalFractionInPassing") != -1:
                getattr(common.all_pdfs, pdf)[i] = line.replace("[1.0]","[0.9,0.,1.]")
            i = i + 1

process = cms.Process("TagProbe")
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

################################################
#specifies the binning of parameters
IDEfficiencyBins = cms.PSet(
    probe_Ele_pt = cms.vdouble(10. ,20. ,30. ,40. ,50. ,200.),
    #event_nPV = cms.vdouble(0.,5.,10.,15.,20.,100.),
    probe_sc_abseta = cms.vdouble(0., 0.8, 1.442, 1.566, 2.0, 2.5),
    )
IsoEfficiencyBins = cms.PSet()
trail = ""
if (options.doEta):
    IsoEfficiencyBins = cms.PSet(
        probe_Ele_pt = cms.vdouble(10. ,20. ,30. ,40. ,50. ,200.),
        #event_nPV = cms.vdouble(0.,5.,10.,15.,20.,100.),
        probe_sc_abseta = cms.vdouble(0., 0.8, 1.442, 1.566, 2.0, 2.5),
        )
    trail = "eta"
else:
    IsoEfficiencyBins = cms.PSet(
        probe_Ele_pt = cms.vdouble(10. ,20. ,30. ,40. ,50. ,200.),
        #event_nPV = cms.vdouble(0.,5.,10.,15.,20.,100.),
        probe_ele_RelAct = cms.vdouble(0., 0.02, 0.05, 0.15, 1., 99999.),
        )
    trail = "act"

McVetoBinningSpecification = cms.PSet(
    UnbinnedVariables = cms.vstring("mass", "totWeight", "Ele_dRTau", "probe_dRTau"),
    BinnedVariables = cms.PSet(IDEfficiencyBins, mcTrue = cms.vstring("true")),
    BinToPDFmap = BinSpec("Veto"),
    )
McLooseBinningSpecification = McVetoBinningSpecification.clone()
McLooseBinningSpecification.BinToPDFmap = BinSpec("Loose")

McMediumBinningSpecification = McVetoBinningSpecification.clone()
McMediumBinningSpecification.BinToPDFmap = BinSpec("Medium")

McTightBinningSpecification = McVetoBinningSpecification.clone()
McTightBinningSpecification.BinToPDFmap = BinSpec("Tight")

McLoose2DBinningSpecification = McVetoBinningSpecification.clone()
McLoose2DBinningSpecification.BinToPDFmap = BinSpec("Loose2D")

McFOID2DBinningSpecification = McVetoBinningSpecification.clone()
McFOID2DBinningSpecification.BinToPDFmap = BinSpec("FOID2D")

McTight2D3DBinningSpecification = McVetoBinningSpecification.clone()
McTight2D3DBinningSpecification.BinToPDFmap = BinSpec("Tight2D3D")

McTightID2D3DBinningSpecification = McVetoBinningSpecification.clone()
McTightID2D3DBinningSpecification.BinToPDFmap = BinSpec("TightID2D3D")

McMVAVLooseMiniBinningSpecification = cms.PSet(
    UnbinnedVariables = cms.vstring("mass", "totWeight", "Ele_dRTau", "probe_dRTau"),
    BinnedVariables = cms.PSet(IsoEfficiencyBins, mcTrue = cms.vstring("true")),
    BinToPDFmap = BinSpec("MVAVLooseMini"),
    )

McMVAVLooseMini4BinningSpecification = McMVAVLooseMiniBinningSpecification.clone()
McMVAVLooseMini4BinningSpecification.BinToPDFmap = BinSpec("MVAVLooseMini4")

McMVAVLooseConvIHit1BinningSpecification = McMVAVLooseMiniBinningSpecification.clone()
McMVAVLooseConvIHit1BinningSpecification.BinToPDFmap = BinSpec("MVAVLooseConvIHit1")

McMVATightConvIHit0ChgBinningSpecification = McMVAVLooseMiniBinningSpecification.clone()
McMVATightConvIHit0ChgBinningSpecification.BinToPDFmap = BinSpec("MVATightConvIHit0Chg")

McMVATightMultiBinningSpecification = McMVAVLooseMiniBinningSpecification.clone()
McMVATightMultiBinningSpecification.BinToPDFmap = BinSpec("MVATightMulti")

McMVATightMultiEmuBinningSpecification = McMVAVLooseMiniBinningSpecification.clone()
McMVATightMultiEmuBinningSpecification.BinToPDFmap = BinSpec("MVATightMultiEmu")

DataVetoBinningSpecification = McVetoBinningSpecification.clone()
DataVetoBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataVetoBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)
DataLooseBinningSpecification = McLooseBinningSpecification.clone()
DataLooseBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataLooseBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)
DataMediumBinningSpecification = McMediumBinningSpecification.clone()
DataMediumBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataMediumBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)
DataTightBinningSpecification = McTightBinningSpecification.clone()
DataTightBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataTightBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)
DataLoose2DBinningSpecification = McLoose2DBinningSpecification.clone()
DataLoose2DBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataLoose2DBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)
DataFOID2DBinningSpecification = McFOID2DBinningSpecification.clone()
DataFOID2DBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataFOID2DBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)
DataTight2D3DBinningSpecification = McTight2D3DBinningSpecification.clone()
DataTight2D3DBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataTight2D3DBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)
DataTightID2D3DBinningSpecification = McTightID2D3DBinningSpecification.clone()
DataTightID2D3DBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataTightID2D3DBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)
DataMVAVLooseMiniBinningSpecification = McMVAVLooseMiniBinningSpecification.clone()
DataMVAVLooseMiniBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataMVAVLooseMiniBinningSpecification.BinnedVariables = cms.PSet(IsoEfficiencyBins)
DataMVAVLooseMini4BinningSpecification = McMVAVLooseMini4BinningSpecification.clone()
DataMVAVLooseMini4BinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataMVAVLooseMini4BinningSpecification.BinnedVariables = cms.PSet(IsoEfficiencyBins)
DataMVAVLooseConvIHit1BinningSpecification = McMVAVLooseConvIHit1BinningSpecification.clone()
DataMVAVLooseConvIHit1BinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataMVAVLooseConvIHit1BinningSpecification.BinnedVariables = cms.PSet(IsoEfficiencyBins)
DataMVATightConvIHit0ChgBinningSpecification = McMVATightConvIHit0ChgBinningSpecification.clone()
DataMVATightConvIHit0ChgBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataMVATightConvIHit0ChgBinningSpecification.BinnedVariables = cms.PSet(IsoEfficiencyBins)
DataMVATightMultiBinningSpecification = McMVATightMultiBinningSpecification.clone()
DataMVATightMultiBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataMVATightMultiBinningSpecification.BinnedVariables = cms.PSet(IsoEfficiencyBins)
DataMVATightMultiEmuBinningSpecification = McMVATightMultiEmuBinningSpecification.clone()
DataMVATightMultiEmuBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataMVATightMultiEmuBinningSpecification.BinnedVariables = cms.PSet(IsoEfficiencyBins)


############################################################################################
############################################################################################
####### GsfElectron->Id / selection efficiency 
############################################################################################
############################################################################################

process.McGsfElectronToVeto = cms.EDAnalyzer(
    "TagProbeFitTreeAnalyzer",
    InputFileNames = cms.vstring("current/TnPTree_powheg_mini_norm.root"),
    InputDirectoryName = cms.string("GsfElectronToID"),
    InputTreeName = cms.string("fitter_tree"), 
    OutputFileName = cms.string("eff_mc_veto.root"),
    NumCPU = cms.uint32(6),
    SaveWorkspace = cms.bool(False), #VERY TIME CONSUMING FOR MC
    doCutAndCount = cms.bool(True),
    floatShapeParameters = cms.bool(True),
    fixVars = cms.vstring("meanP","sigmaP","meanF","sigmaF"),
    binnedFit = cms.bool(True),
    binsForFit = cms.uint32(60),
    WeightVariable = cms.string("totWeight"),
    # defines all the real variables of the probes available in the input tree and intended for use in the efficiencies
    Variables = cms.PSet(
        mass = cms.vstring("Tag-Probe Mass", "60.0", "120.0", "GeV/c^{2}"),
        #event_nPV = cms.vstring("Event N_{PV}", "0", "1000000", ""),
        probe_Ele_pt = cms.vstring("Probe p_{T}", "10", "200", "GeV/c"),
        probe_sc_abseta = cms.vstring("Probe |#eta|", "0", "2.5", ""), 
        probe_ele_RelAct = cms.vstring("Probe Activity", "0", "100000000", ""),
        #tag_Ele_pt = cms.vstring("Tag p_{T}", "35.", "1000000000", "GeV/c"),
        totWeight = cms.vstring("totWeight", "0", "100000000", ""), 
        Ele_dRTau = cms.vstring("Ele_dRTau", "0.2", "100000", ""),
        probe_dRTau = cms.vstring("probe_dRTau", "0.2", "100000", ""),
        ),
    # defines all the discrete variables of the probes available in the input tree and intended for use in the efficiency calculation
    Categories = cms.PSet(
        mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
        passingVeto = cms.vstring("passingVeto", "dummy[pass=1,fail=0]"),
        ),
    PDFs = common.all_pdfs,
    # defines a set of efficiency calculations, what PDF to use for fitting and how to bin the data;
    # there will be a separate output directory for each calculation that includes a
    # simultaneous fit, side band subtraction and counting. 
    Efficiencies = cms.PSet(
        MCtruth_Veto = cms.PSet(
            McVetoBinningSpecification,
            EfficiencyCategoryAndState = cms.vstring("passingVeto", "pass"),
            ),
        )
    )

process.McGsfElectronToLoose = process.McGsfElectronToVeto.clone()
process.McGsfElectronToLoose.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToLoose.OutputFileName = cms.string("eff_mc_loose.root")
process.McGsfElectronToLoose.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingLoose = cms.vstring("passingLoose", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToLoose.Efficiencies = cms.PSet(
    MCtruth_Loose = cms.PSet(
        McLooseBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLoose", "pass"),
        ),
    )

process.McGsfElectronToMedium = process.McGsfElectronToVeto.clone()
process.McGsfElectronToMedium.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToMedium.OutputFileName = cms.string("eff_mc_medium.root")
process.McGsfElectronToMedium.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingMedium = cms.vstring("passingMedium", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToMedium.Efficiencies = cms.PSet(
    MCtruth_Medium = cms.PSet(
        McMediumBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMedium", "pass"),
        ),
    )

process.McGsfElectronToTight = process.McGsfElectronToVeto.clone()
process.McGsfElectronToTight.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToTight.OutputFileName = cms.string("eff_mc_tight.root")
process.McGsfElectronToTight.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingTight = cms.vstring("passingTight", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToTight.Efficiencies = cms.PSet(
    MCtruth_Tight = cms.PSet(
        McTightBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingTight", "pass"),
        ),
    )

process.McGsfElectronToLoose2D = process.McGsfElectronToVeto.clone()
process.McGsfElectronToLoose2D.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToLoose2D.OutputFileName = cms.string("eff_mc_loose2d.root")
process.McGsfElectronToLoose2D.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingLoose2D = cms.vstring("passingLoose2D", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToLoose2D.Efficiencies = cms.PSet(
    MCtruth_Loose2D = cms.PSet(
        McLoose2DBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLoose2D", "pass"),
        ),
    )

process.McGsfElectronToFOID2D = process.McGsfElectronToVeto.clone()
process.McGsfElectronToFOID2D.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToFOID2D.OutputFileName = cms.string("eff_mc_foid2d.root")
process.McGsfElectronToFOID2D.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingFOID2D = cms.vstring("passingFOID2D", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToFOID2D.Efficiencies = cms.PSet(
    MCtruth_FOID2D = cms.PSet(
        McFOID2DBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingFOID2D", "pass"),
        ),
    )

process.McGsfElectronToTight2D3D = process.McGsfElectronToVeto.clone()
process.McGsfElectronToTight2D3D.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToTight2D3D.OutputFileName = cms.string("eff_mc_tight2d3d.root")
process.McGsfElectronToTight2D3D.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingTight2D3D = cms.vstring("passingTight2D3D", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToTight2D3D.Efficiencies = cms.PSet(
    MCtruth_Tight2D3D = cms.PSet(
        McTight2D3DBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingTight2D3D", "pass"),
        ),
    )

process.McGsfElectronToTightID2D3D = process.McGsfElectronToVeto.clone()
process.McGsfElectronToTightID2D3D.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToTightID2D3D.OutputFileName = cms.string("eff_mc_tightid2d3d.root")
process.McGsfElectronToTightID2D3D.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingTightID2D3D = cms.vstring("passingTightID2D3D", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToTightID2D3D.Efficiencies = cms.PSet(
    MCtruth_TightID2D3D = cms.PSet(
        McTightID2D3DBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingTightID2D3D", "pass"),
        ),
    )

process.McMVAVLooseElectronToMini = process.McGsfElectronToMedium.clone()
process.McMVAVLooseElectronToMini.InputDirectoryName = cms.string("MVAVLooseElectronToIso")
process.McMVAVLooseElectronToMini.OutputFileName = cms.string("eff_mc_mvavloosemini_"+trail+".root")
process.McMVAVLooseElectronToMini.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingMini = cms.vstring("passingMini", "dummy[pass=1,fail=0]"),
    )
process.McMVAVLooseElectronToMini.Efficiencies = cms.PSet(
    MCtruth_Mini = cms.PSet(
        McMVAVLooseMiniBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMini", "pass"),
        ),
    )

process.McMVAVLooseElectronToMini4 = process.McMVAVLooseElectronToMini.clone()
process.McMVAVLooseElectronToMini4.InputDirectoryName = cms.string("MVAVLooseElectronToIso")
process.McMVAVLooseElectronToMini4.OutputFileName = cms.string("eff_mc_mvavloosemini4_"+trail+".root")
process.McMVAVLooseElectronToMini4.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingMini4 = cms.vstring("passingMini4", "dummy[pass=1,fail=0]"),
    )
process.McMVAVLooseElectronToMini4.Efficiencies = cms.PSet(
    MCtruth_Mini4 = cms.PSet(
        McMVAVLooseMini4BinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMini4", "pass"),
        ),
    )

process.McMVAVLooseElectronToConvIHit1 = process.McMVAVLooseElectronToMini.clone()
process.McMVAVLooseElectronToConvIHit1.InputDirectoryName = cms.string("MVAVLooseElectronToIso")
process.McMVAVLooseElectronToConvIHit1.OutputFileName = cms.string("eff_mc_mvavlooseconvihit1_"+trail+".root")
process.McMVAVLooseElectronToConvIHit1.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingConvIHit1 = cms.vstring("passingConvIHit1", "dummy[pass=1,fail=0]"),
    )
process.McMVAVLooseElectronToConvIHit1.Efficiencies = cms.PSet(
    MCtruth_ConvIHit1 = cms.PSet(
        McMVAVLooseConvIHit1BinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingConvIHit1", "pass"),
        ),
    )

process.McMVATightElectronToConvIHit0Chg = process.McMVAVLooseElectronToMini.clone()
process.McMVATightElectronToConvIHit0Chg.InputDirectoryName = cms.string("MVATightElectronToIso")
process.McMVATightElectronToConvIHit0Chg.OutputFileName = cms.string("eff_mc_mvatightconvihit0chg_"+trail+".root")
process.McMVATightElectronToConvIHit0Chg.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingConvIHit0Chg = cms.vstring("passingConvIHit0Chg", "dummy[pass=1,fail=0]"),
    )
process.McMVATightElectronToConvIHit0Chg.Efficiencies = cms.PSet(
    MCtruth_ConvIHit0Chg = cms.PSet(
        McMVATightConvIHit0ChgBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingConvIHit0Chg", "pass"),
        ),
    )

process.McMVATightElectronToMulti = process.McMVAVLooseElectronToMini.clone()
process.McMVATightElectronToMulti.InputDirectoryName = cms.string("MVATightElectronToIso")
process.McMVATightElectronToMulti.OutputFileName = cms.string("eff_mc_mvatightmulti_"+trail+".root")
process.McMVATightElectronToMulti.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingMultiIso = cms.vstring("passingMultiIso", "dummy[pass=1,fail=0]"),
    )
process.McMVATightElectronToMulti.Efficiencies = cms.PSet(
    MCtruth_Multi = cms.PSet(
        McMVATightMultiBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMultiIso", "pass"),
        ),
    )

process.McMVATightElectronToMultiEmu = process.McMVAVLooseElectronToMini.clone()
process.McMVATightElectronToMultiEmu.InputDirectoryName = cms.string("MVATightElectronToIso")
process.McMVATightElectronToMultiEmu.OutputFileName = cms.string("eff_mc_mvatightmultiemu_"+trail+".root")
process.McMVATightElectronToMultiEmu.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingMultiIsoEmu = cms.vstring("passingMultiIsoEmu", "dummy[pass=1,fail=0]"),
    )
process.McMVATightElectronToMultiEmu.Efficiencies = cms.PSet(
    MCtruth_MultiEmu = cms.PSet(
        McMVATightMultiEmuBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMultiIsoEmu", "pass"),
        ),
    )

process.DataGsfElectronToVeto = process.McGsfElectronToVeto.clone()
process.DataGsfElectronToVeto.InputFileNames = cms.vstring("current/TnPTree_data.root")
process.DataGsfElectronToVeto.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToVeto.OutputFileName = cms.string("eff_data_veto.root")
process.DataGsfElectronToVeto.doCutAndCount = cms.bool(False)
delattr(process.DataGsfElectronToVeto, "WeightVariable")
process.DataGsfElectronToVeto.Variables = cms.PSet(
    mass = cms.vstring("Tag-Probe Mass", "60.0", "120.0", "GeV/c^{2}"),
    #event_nPV = cms.vstring("Event N_{PV}", "0", "1000000", ""),
    probe_Ele_pt = cms.vstring("Probe p_{T}", "10", "200", "GeV/c"),
    probe_sc_abseta = cms.vstring("Probe |#eta|", "0", "2.5", ""), 
    #tag_Ele_pt = cms.vstring("Tag p_{T}", "35.", "1000000000", "GeV/c"),
    probe_ele_RelAct = cms.vstring("Probe Activity", "0", "100000000", ""), 
    )
process.DataGsfElectronToVeto.Categories = cms.PSet(passingVeto = cms.vstring("passingVeto", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToVeto.Efficiencies = cms.PSet(
    Veto = cms.PSet(
        DataVetoBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingVeto", "pass"),
        ),
    )

process.DataGsfElectronToLoose = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToLoose.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToLoose.OutputFileName = cms.string("eff_data_loose.root")
process.DataGsfElectronToLoose.Categories = cms.PSet(passingLoose = cms.vstring("passingLoose", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToLoose.Efficiencies = cms.PSet(
    Loose = cms.PSet(
        DataLooseBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLoose", "pass"),
        ),
    )

process.DataGsfElectronToMedium = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToMedium.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToMedium.OutputFileName = cms.string("eff_data_medium.root")
process.DataGsfElectronToMedium.Categories = cms.PSet(passingMedium = cms.vstring("passingMedium", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToMedium.Efficiencies = cms.PSet(
    Medium = cms.PSet(
        DataMediumBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMedium", "pass"),
        ),
    )

process.DataGsfElectronToTight = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToTight.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToTight.OutputFileName = cms.string("eff_data_tight.root")
process.DataGsfElectronToTight.Categories = cms.PSet(passingTight = cms.vstring("passingTight", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToTight.Efficiencies = cms.PSet(
    Tight = cms.PSet(
        DataTightBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingTight", "pass"),
        ),
    )

process.DataGsfElectronToLoose2D = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToLoose2D.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToLoose2D.OutputFileName = cms.string("eff_data_loose2d.root")
process.DataGsfElectronToLoose2D.Categories = cms.PSet(passingLoose2D = cms.vstring("passingLoose2D", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToLoose2D.Efficiencies = cms.PSet(
    Loose2D = cms.PSet(
        DataLoose2DBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLoose2D", "pass"),
        ),
    )

process.DataGsfElectronToFOID2D = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToFOID2D.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToFOID2D.OutputFileName = cms.string("eff_data_foid2d.root")
process.DataGsfElectronToFOID2D.Categories = cms.PSet(passingFOID2D = cms.vstring("passingFOID2D", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToFOID2D.Efficiencies = cms.PSet(
    FOID2D = cms.PSet(
        DataFOID2DBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingFOID2D", "pass"),
        ),
    )

process.DataGsfElectronToTight2D3D = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToTight2D3D.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToTight2D3D.OutputFileName = cms.string("eff_data_tight2d3d.root")
process.DataGsfElectronToTight2D3D.Categories = cms.PSet(passingTight2D3D = cms.vstring("passingTight2D3D", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToTight2D3D.Efficiencies = cms.PSet(
    Tight2D3D = cms.PSet(
        DataTight2D3DBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingTight2D3D", "pass"),
        ),
    )

process.DataGsfElectronToTightID2D3D = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToTightID2D3D.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToTightID2D3D.OutputFileName = cms.string("eff_data_tightid2d3d.root")
process.DataGsfElectronToTightID2D3D.Categories = cms.PSet(passingTightID2D3D = cms.vstring("passingTightID2D3D", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToTightID2D3D.Efficiencies = cms.PSet(
    TightID2D3D = cms.PSet(
        DataTightID2D3DBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingTightID2D3D", "pass"),
        ),
    )

process.DataMVAVLooseElectronToMini = process.DataGsfElectronToVeto.clone()
process.DataMVAVLooseElectronToMini.InputDirectoryName = cms.string("MVAVLooseElectronToIso")
process.DataMVAVLooseElectronToMini.OutputFileName = cms.string("eff_data_mvavloosemini_"+trail+".root")
process.DataMVAVLooseElectronToMini.Categories = cms.PSet(passingMini = cms.vstring("passingMini", "dummy[pass=1,fail=0]"))
process.DataMVAVLooseElectronToMini.Efficiencies = cms.PSet(
    Mini = cms.PSet(
        DataMVAVLooseMiniBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMini", "pass"),
        ),
    )

process.DataMVAVLooseElectronToMini4 = process.DataMVAVLooseElectronToMini.clone()
process.DataMVAVLooseElectronToMini4.InputDirectoryName = cms.string("MVAVLooseElectronToIso")
process.DataMVAVLooseElectronToMini4.OutputFileName = cms.string("eff_data_mvavloosemini4_"+trail+".root")
process.DataMVAVLooseElectronToMini4.Categories = cms.PSet(passingMini4 = cms.vstring("passingMini4", "dummy[pass=1,fail=0]"))
process.DataMVAVLooseElectronToMini4.Efficiencies = cms.PSet(
    Mini4 = cms.PSet(
        DataMVAVLooseMini4BinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMini4", "pass"),
        ),
    )

process.DataMVAVLooseElectronToConvIHit1 = process.DataMVAVLooseElectronToMini.clone()
process.DataMVAVLooseElectronToConvIHit1.InputDirectoryName = cms.string("MVAVLooseElectronToIso")
process.DataMVAVLooseElectronToConvIHit1.OutputFileName = cms.string("eff_data_mvavlooseconvihit1_"+trail+".root")
process.DataMVAVLooseElectronToConvIHit1.Categories = cms.PSet(passingConvIHit1 = cms.vstring("passingConvIHit1", "dummy[pass=1,fail=0]"))
process.DataMVAVLooseElectronToConvIHit1.Efficiencies = cms.PSet(
    ConvIHit1 = cms.PSet(
        DataMVAVLooseConvIHit1BinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingConvIHit1", "pass"),
        ),
    )

process.DataMVATightElectronToConvIHit0Chg = process.DataMVAVLooseElectronToMini.clone()
process.DataMVATightElectronToConvIHit0Chg.InputDirectoryName = cms.string("MVATightElectronToIso")
process.DataMVATightElectronToConvIHit0Chg.OutputFileName = cms.string("eff_data_mvatightconvihit0chg_"+trail+".root")
process.DataMVATightElectronToConvIHit0Chg.Categories = cms.PSet(passingConvIHit0Chg = cms.vstring("passingConvIHit0Chg", "dummy[pass=1,fail=0]"))
process.DataMVATightElectronToConvIHit0Chg.Efficiencies = cms.PSet(
    ConvIHit0Chg = cms.PSet(
        DataMVATightConvIHit0ChgBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingConvIHit0Chg", "pass"),
        ),
    )

process.DataMVATightElectronToMulti = process.DataMVAVLooseElectronToMini.clone()
process.DataMVATightElectronToMulti.InputDirectoryName = cms.string("MVATightElectronToIso")
process.DataMVATightElectronToMulti.OutputFileName = cms.string("eff_data_mvatightmulti_"+trail+".root")
process.DataMVATightElectronToMulti.Categories = cms.PSet(passingMultiIso = cms.vstring("passingMultiIso", "dummy[pass=1,fail=0]"))
process.DataMVATightElectronToMulti.Efficiencies = cms.PSet(
    Multi = cms.PSet(
        DataMVATightMultiBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMultiIso", "pass"),
        ),
    )

process.DataMVATightElectronToMultiEmu = process.DataMVAVLooseElectronToMini.clone()
process.DataMVATightElectronToMultiEmu.InputDirectoryName = cms.string("MVATightElectronToIso")
process.DataMVATightElectronToMultiEmu.OutputFileName = cms.string("eff_data_mvatightmultiemu_"+trail+".root")
process.DataMVATightElectronToMultiEmu.Categories = cms.PSet(passingMultiIsoEmu = cms.vstring("passingMultiIsoEmu", "dummy[pass=1,fail=0]"))
process.DataMVATightElectronToMultiEmu.Efficiencies = cms.PSet(
    MultiEmu = cms.PSet(
        DataMVATightMultiEmuBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMultiIsoEmu", "pass"),
        ),
    )

process.seq = cms.Sequence()

if (not options.noMC) and (not options.noID):
    process.seq += process.McGsfElectronToVeto
    process.seq += process.McGsfElectronToLoose
    process.seq += process.McGsfElectronToMedium
    process.seq += process.McGsfElectronToTight
    process.seq += process.McGsfElectronToLoose2D
    process.seq += process.McGsfElectronToFOID2D
    process.seq += process.McGsfElectronToTight2D3D
    process.seq += process.McGsfElectronToTightID2D3D

if (not options.noMC) and (not options.noIso):
    process.seq += process.McMVAVLooseElectronToMini
    process.seq += process.McMVAVLooseElectronToMini4
    process.seq += process.McMVAVLooseElectronToConvIHit1
    process.seq += process.McMVATightElectronToConvIHit0Chg
    process.seq += process.McMVATightElectronToMulti
    process.seq += process.McMVATightElectronToMultiEmu

if (not options.noData) and (not options.noID):
    process.seq += process.DataGsfElectronToVeto
    process.seq += process.DataGsfElectronToLoose
    process.seq += process.DataGsfElectronToMedium
    process.seq += process.DataGsfElectronToTight
    process.seq += process.DataGsfElectronToLoose2D
    process.seq += process.DataGsfElectronToFOID2D
    process.seq += process.DataGsfElectronToTight2D3D
    process.seq += process.DataGsfElectronToTightID2D3D

if (not options.noData) and (not options.noIso):
    process.seq += process.DataMVAVLooseElectronToMini
    process.seq += process.DataMVAVLooseElectronToMini4
    process.seq += process.DataMVAVLooseElectronToConvIHit1
    process.seq += process.DataMVATightElectronToConvIHit0Chg
    process.seq += process.DataMVATightElectronToMulti
    process.seq += process.DataMVATightElectronToMultiEmu

process.fit = cms.Path(process.seq)
