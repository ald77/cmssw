import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
import PhysicsTools.TagAndProbe.commonFit as common

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
                getattr(common.all_pdfs, pdf)[i] = line.replace("[1.]","[0.9,0.,1.]")
            i = i + 1

process = cms.Process("TagProbe")
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

InputFileName = "current/TnPTree_id_norm.root"
OutputFile = "eff_mc_id.root"
PDFName = "pdfSignalPlusBackground"

################################################
IDEfficiencyBins = cms.PSet(
    probe_sc_et = cms.vdouble(10. ,20. ,30. ,40. ,50. ,200.),
    probe_sc_abseta = cms.vdouble(0., 1.442, 1.566, 2.5),
    )
IsoEfficiencyBins = cms.PSet(
    probe_sc_et = cms.vdouble(10. ,20. ,30. ,40. ,50. ,200.),
    #probe_sc_abseta = cms.vdouble(0., 1.442, 1.566, 2.5),
    probe_Ele_Act = cms.vdouble(0., 0.02, 0.05, 0.15, 1.),
    )

#specifies the binning of parameters
EfficiencyBins = cms.PSet(
    probe_sc_et = cms.vdouble(10. ,20. ,30. ,40. ,50. ,200.),
    probe_sc_abseta = cms.vdouble(0., 1.442, 1.566, 2.5),
    )

McVetoBinningSpecification = cms.PSet(
    UnbinnedVariables = cms.vstring("mass", "totWeight", "Ele_dRTau", "probe_dRTau"),
    BinnedVariables = cms.PSet(IDEfficiencyBins, mcTrue = cms.vstring("true")),
    BinToPDFmap = cms.vstring(
        "standard",
        "*eta_bin1*et_bin0*","veto_pt_10_20",
        "*eta_bin1*et_bin1*","veto_pt_20_30",
        "*eta_bin1*et_bin2*","veto_pt_30_40",
        "*eta_bin1*et_bin3*","veto_pt_40_50",
        "*eta_bin1*et_bin4*","veto_pt_50_200",
        )
)
McLooseBinningSpecification = McVetoBinningSpecification.clone()
McLooseBinningSpecification.BinToPDFmap = cms.vstring(
        "standard",
        "*eta_bin1*et_bin0*","loose_pt_10_20",
        "*eta_bin1*et_bin1*","loose_pt_20_30",
        "*eta_bin1*et_bin2*","loose_pt_30_40",
        "*eta_bin1*et_bin3*","loose_pt_40_50",
        "*eta_bin1*et_bin4*","loose_pt_50_200",
)
McMediumBinningSpecification = McVetoBinningSpecification.clone()
McMediumBinningSpecification.BinToPDFmap = cms.vstring(
        "standard",
        "*eta_bin1*et_bin0*","medium_pt_10_20",
        "*eta_bin1*et_bin1*","medium_pt_20_30",
        "*eta_bin1*et_bin2*","medium_pt_30_40",
        "*eta_bin1*et_bin3*","medium_pt_40_50",
        "*eta_bin1*et_bin4*","medium_pt_50_200",
)
McTightBinningSpecification = McVetoBinningSpecification.clone()
McTightBinningSpecification.BinToPDFmap = cms.vstring(
        "standard",
        "*eta_bin1*et_bin0*","tight_pt_10_20",
        "*eta_bin1*et_bin1*","tight_pt_20_30",
        "*eta_bin1*et_bin2*","tight_pt_30_40",
        "*eta_bin1*et_bin3*","tight_pt_40_50",
        "*eta_bin1*et_bin4*","tight_pt_50_200",
)
McIsoBinningSpecification = cms.PSet(
    UnbinnedVariables = cms.vstring("mass", "totWeight", "Ele_dRTau", "probe_dRTau"),
    BinnedVariables = cms.PSet(IsoEfficiencyBins, mcTrue = cms.vstring("true")),
    BinToPDFmap = cms.vstring("standard"),
)
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
DataIsoBinningSpecification = McIsoBinningSpecification.clone()
DataIsoBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataIsoBinningSpecification.BinnedVariables = cms.PSet(IsoEfficiencyBins)

############################################################################################
############################################################################################
####### GsfElectron->Id / selection efficiency 
############################################################################################
############################################################################################

process.McGsfElectronToVeto = cms.EDAnalyzer(
    "TagProbeFitTreeAnalyzer",
    InputFileNames = cms.vstring("current/TnPTree_id_norm.root"),
    InputDirectoryName = cms.string("GsfElectronToID"),
    InputTreeName = cms.string("fitter_tree"), 
    OutputFileName = cms.string("eff_mc_veto_id.root"),
    NumCPU = cms.uint32(6),
    SaveWorkspace = cms.bool(False), #VERY TIME CONSUMING FOR MC
    doCutAndCount = cms.bool(True),
    floatShapeParameters = cms.bool(True),
    binnedFit = cms.bool(True),
    binsForFit = cms.uint32(60),
    WeightVariable = cms.string("totWeight"),
    # defines all the real variables of the probes available in the input tree and intended for use in the efficiencies
    Variables = cms.PSet(
        mass = cms.vstring("Tag-Probe Mass", "60.0", "120.0", "GeV/c^{2}"),
        probe_sc_et = cms.vstring("Probe E_{T}", "10", "200", "GeV/c"),
        probe_sc_abseta = cms.vstring("Probe #eta", "0", "2.5", ""), 
        probe_Ele_Act = cms.vstring("Probe Activity", "0", "100000000", ""), 
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
process.McGsfElectronToLoose.OutputFileName = cms.string("eff_mc_loose_id.root")
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
process.McGsfElectronToMedium.OutputFileName = cms.string("eff_mc_medium_id.root")
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
process.McGsfElectronToTight.OutputFileName = cms.string("eff_mc_tight_id.root")
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

process.McVetoElectronToIso = process.McGsfElectronToVeto.clone()
process.McVetoElectronToIso.InputFileNames = cms.vstring("current/TnPTree_veto_norm.root")
process.McVetoElectronToIso.InputDirectoryName = cms.string("VetoElectronToIso")
process.McVetoElectronToIso.OutputFileName = cms.string("eff_mc_veto_iso.root")
process.McVetoElectronToIso.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingMini = cms.vstring("passingMini", "dummy[pass=1,fail=0]"),
    )
process.McVetoElectronToIso.Efficiencies = cms.PSet(
    MCtruth_Mini = cms.PSet(
        McIsoBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMini", "pass"),
        ),
    )

process.McLooseElectronToIso = process.McGsfElectronToVeto.clone()
process.McLooseElectronToIso.InputFileNames = cms.vstring("current/TnPTree_loose_norm.root")
process.McLooseElectronToIso.InputDirectoryName = cms.string("LooseElectronToIso")
process.McLooseElectronToIso.OutputFileName = cms.string("eff_mc_loose_iso.root")

process.McMediumElectronToIso = process.McGsfElectronToVeto.clone()
process.McMediumElectronToIso.InputFileNames = cms.vstring("current/TnPTree_medium_norm.root")
process.McMediumElectronToIso.InputDirectoryName = cms.string("MediumElectronToIso")
process.McMediumElectronToIso.OutputFileName = cms.string("eff_mc_medium_iso.root")

process.McTightElectronToIso = process.McGsfElectronToVeto.clone()
process.McTightElectronToIso.InputFileNames = cms.vstring("current/TnPTree_tight_norm.root")
process.McTightElectronToIso.InputDirectoryName = cms.string("TightElectronToIso")
process.McTightElectronToIso.OutputFileName = cms.string("eff_mc_tight_iso.root")

process.DataGsfElectronToVeto = process.McGsfElectronToVeto.clone()
process.DataGsfElectronToVeto.InputFileNames = cms.vstring("current/TnPTree_data.root")
process.DataGsfElectronToVeto.OutputFileName = cms.string("eff_data_veto_id.root")
process.DataGsfElectronToVeto.doCutAndCount = cms.bool(False)
delattr(process.DataGsfElectronToVeto, "WeightVariable")
process.DataGsfElectronToVeto.Variables = cms.PSet(
    mass = cms.vstring("Tag-Probe Mass", "60.0", "120.0", "GeV/c^{2}"),
    probe_sc_et = cms.vstring("Probe E_{T}", "10", "200", "GeV/c"),
    probe_sc_abseta = cms.vstring("Probe #eta", "0", "2.5", ""), 
    probe_Ele_Act = cms.vstring("Probe Activity", "0", "100000000", ""), 
    )
process.DataGsfElectronToVeto.Categories = cms.PSet(passingVeto = cms.vstring("passingVeto", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToVeto.Efficiencies = cms.PSet(
    Veto = cms.PSet(
        DataVetoBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingVeto", "pass"),
        ),
    )

process.DataGsfElectronToLoose = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToLoose.OutputFileName = cms.string("eff_data_loose_id.root")
process.DataGsfElectronToLoose.Categories = cms.PSet(passingLoose = cms.vstring("passingLoose", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToLoose.Efficiencies = cms.PSet(
    Loose = cms.PSet(
        DataLooseBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLoose", "pass"),
        ),
    )

process.DataGsfElectronToMedium = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToMedium.OutputFileName = cms.string("eff_data_medium_id.root")
process.DataGsfElectronToMedium.Categories = cms.PSet(passingMedium = cms.vstring("passingMedium", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToMedium.Efficiencies = cms.PSet(
    Medium = cms.PSet(
        DataMediumBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMedium", "pass"),
        ),
    )

process.DataGsfElectronToTight = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToTight.OutputFileName = cms.string("eff_data_tight_id.root")
process.DataGsfElectronToTight.Categories = cms.PSet(passingTight = cms.vstring("passingTight", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToTight.Efficiencies = cms.PSet(
    Tight = cms.PSet(
        DataTightBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingTight", "pass"),
        ),
    )

process.DataVetoElectronToIso = process.DataGsfElectronToVeto.clone()
process.DataVetoElectronToIso.InputDirectoryName = cms.string("VetoElectronToIso")
process.DataVetoElectronToIso.OutputFileName = cms.string("eff_data_veto_iso.root")
process.DataVetoElectronToIso.Categories = cms.PSet(passingMini = cms.vstring("passingMini", "dummy[pass=1,fail=0]"))
process.DataVetoElectronToIso.Efficiencies = cms.PSet(
    Mini = cms.PSet(
        DataIsoBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMini", "pass"),
        ),
    )

process.DataLooseElectronToIso = process.DataVetoElectronToIso.clone()
process.DataLooseElectronToIso.InputDirectoryName = cms.string("LooseElectronToIso")
process.DataLooseElectronToIso.OutputFileName = cms.string("eff_data_loose_iso.root")

process.DataMediumElectronToIso = process.DataVetoElectronToIso.clone()
process.DataMediumElectronToIso.InputDirectoryName = cms.string("MediumElectronToIso")
process.DataMediumElectronToIso.OutputFileName = cms.string("eff_data_medium_iso.root")

process.DataTightElectronToIso = process.DataVetoElectronToIso.clone()
process.DataTightElectronToIso.InputDirectoryName = cms.string("TightElectronToIso")
process.DataTightElectronToIso.OutputFileName = cms.string("eff_data_tight_iso.root")

process.seq = cms.Sequence()

if (not options.noMC) and (not options.noID):
    process.seq += process.McGsfElectronToVeto
    process.seq += process.McGsfElectronToLoose
    process.seq += process.McGsfElectronToMedium
    process.seq += process.McGsfElectronToTight

if (not options.noMC) and (not options.noIso):
    process.seq += process.McVetoElectronToIso
    process.seq += process.McLooseElectronToIso
    process.seq += process.McMediumElectronToIso
    process.seq += process.McTightElectronToIso

if (not options.noData) and (not options.noID):
    process.seq += process.DataGsfElectronToVeto
    process.seq += process.DataGsfElectronToLoose
    process.seq += process.DataGsfElectronToMedium
    process.seq += process.DataGsfElectronToTight

if (not options.noData) and (not options.noIso):
    process.seq += process.DataVetoElectronToIso
    process.seq += process.DataLooseElectronToIso
    process.seq += process.DataMediumElectronToIso
    process.seq += process.DataTightElectronToIso

process.fit = cms.Path(process.seq)
