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
    probe_sc_et = cms.vdouble(10. ,20. ,30. ,40. ,50. ,200.),
    probe_sc_abseta = cms.vdouble(0., 1.442, 1.566, 2.5),
    )
IsoEfficiencyBins = cms.PSet()
trail = ""
if (options.doEta):
    IsoEfficiencyBins = cms.PSet(
        probe_sc_et = cms.vdouble(10. ,20. ,30. ,40. ,50. ,200.),
        probe_sc_abseta = cms.vdouble(0., 1.442, 1.566, 2.5),
        )
    trail = "eta"
else:
    IsoEfficiencyBins = cms.PSet(
        probe_sc_et = cms.vdouble(10. ,20. ,30. ,40. ,50. ,200.),
        probe_ele_Act = cms.vdouble(0., 0.02, 0.05, 0.15, 1., 99999.),
        )
    trail = "act"

McVetoBinningSpecification = cms.PSet(
    UnbinnedVariables = cms.vstring("mass", "totWeight", "Ele_dRTau", "probe_dRTau"),
    BinnedVariables = cms.PSet(IDEfficiencyBins, mcTrue = cms.vstring("true")),
    BinToPDFmap = cms.vstring(
        "standard",
        "*eta_bin1*et_bin0*","Veto_crack_10p0To20p0_1p442To1p566",
        "*eta_bin1*et_bin1*","Veto_crack_20p0To30p0_1p442To1p566",
        "*eta_bin1*et_bin2*","Veto_crack_30p0To40p0_1p442To1p566",
        "*eta_bin1*et_bin3*","Veto_crack_40p0To50p0_1p442To1p566",
        "*eta_bin1*et_bin4*","Veto_crack_50p0To200p0_1p442To1p566",
        "*et_bin0*","Veto_alleta_10p0To20p0_0p0To2p5",
        "*et_bin1*","Veto_alleta_20p0To30p0_0p0To2p5",
        "*et_bin2*","Veto_alleta_30p0To40p0_0p0To2p5",
        "*et_bin3*","Veto_alleta_40p0To50p0_0p0To2p5",
        "*et_bin4*","Veto_alleta_50p0To200p0_0p0To2p5",
        )
    )
McLooseBinningSpecification = McVetoBinningSpecification.clone()
McLooseBinningSpecification.BinToPDFmap = cms.vstring(
    "standard",
    "*eta_bin1*et_bin0*","Loose_crack_10p0To20p0_1p442To1p566",
    "*eta_bin1*et_bin1*","Loose_crack_20p0To30p0_1p442To1p566",
    "*eta_bin1*et_bin2*","Loose_crack_30p0To40p0_1p442To1p566",
    "*eta_bin1*et_bin3*","Loose_crack_40p0To50p0_1p442To1p566",
    "*eta_bin1*et_bin4*","Loose_crack_50p0To200p0_1p442To1p566",
    "*et_bin0*","Loose_alleta_10p0To20p0_0p0To2p5",
    "*et_bin1*","Loose_alleta_20p0To30p0_0p0To2p5",
    "*et_bin2*","Loose_alleta_30p0To40p0_0p0To2p5",
    "*et_bin3*","Loose_alleta_40p0To50p0_0p0To2p5",
    "*et_bin4*","Loose_alleta_50p0To200p0_0p0To2p5",
    )
McMediumBinningSpecification = McVetoBinningSpecification.clone()
McMediumBinningSpecification.BinToPDFmap = cms.vstring(
    "standard",
    "*eta_bin1*et_bin0*","Medium_crack_10p0To20p0_1p442To1p566",
    "*eta_bin1*et_bin1*","Medium_crack_20p0To30p0_1p442To1p566",
    "*eta_bin1*et_bin2*","Medium_crack_30p0To40p0_1p442To1p566",
    "*eta_bin1*et_bin3*","Medium_crack_40p0To50p0_1p442To1p566",
    "*eta_bin1*et_bin4*","Medium_crack_50p0To200p0_1p442To1p566",
    "*et_bin0*","Medium_alleta_10p0To20p0_0p0To2p5",
    "*et_bin1*","Medium_alleta_20p0To30p0_0p0To2p5",
    "*et_bin2*","Medium_alleta_30p0To40p0_0p0To2p5",
    "*et_bin3*","Medium_alleta_40p0To50p0_0p0To2p5",
    "*et_bin4*","Medium_alleta_50p0To200p0_0p0To2p5",
    )
McTightBinningSpecification = McVetoBinningSpecification.clone()
McTightBinningSpecification.BinToPDFmap = cms.vstring(
    "standard",
    "*eta_bin1*et_bin0*","Tight_crack_10p0To20p0_1p442To1p566",
    "*eta_bin1*et_bin1*","Tight_crack_20p0To30p0_1p442To1p566",
    "*eta_bin1*et_bin2*","Tight_crack_30p0To40p0_1p442To1p566",
    "*eta_bin1*et_bin3*","Tight_crack_40p0To50p0_1p442To1p566",
    "*eta_bin1*et_bin4*","Tight_crack_50p0To200p0_1p442To1p566",
    "*et_bin0*","Tight_alleta_10p0To20p0_0p0To2p5",
    "*et_bin1*","Tight_alleta_20p0To30p0_0p0To2p5",
    "*et_bin2*","Tight_alleta_30p0To40p0_0p0To2p5",
    "*et_bin3*","Tight_alleta_40p0To50p0_0p0To2p5",
    "*et_bin4*","Tight_alleta_50p0To200p0_0p0To2p5",
    )
McLoose2DBinningSpecification = McVetoBinningSpecification.clone()
McLoose2DBinningSpecification.BinToPDFmap = cms.vstring(
    "standard",
    "*eta_bin1*et_bin0*","Loose2D_crack_10p0To20p0_1p442To1p566",
    "*eta_bin1*et_bin1*","Loose2D_crack_20p0To30p0_1p442To1p566",
    "*eta_bin1*et_bin2*","Loose2D_crack_30p0To40p0_1p442To1p566",
    "*eta_bin1*et_bin3*","Loose2D_crack_40p0To50p0_1p442To1p566",
    "*eta_bin1*et_bin4*","Loose2D_crack_50p0To200p0_1p442To1p566",
    "*et_bin0*","Loose2D_alleta_10p0To20p0_0p0To2p5",
    "*et_bin1*","Loose2D_alleta_20p0To30p0_0p0To2p5",
    "*et_bin2*","Loose2D_alleta_30p0To40p0_0p0To2p5",
    "*et_bin3*","Loose2D_alleta_40p0To50p0_0p0To2p5",
    "*et_bin4*","Loose2D_alleta_50p0To200p0_0p0To2p5",
    )
McFOID2DBinningSpecification = McVetoBinningSpecification.clone()
McFOID2DBinningSpecification.BinToPDFmap = cms.vstring(
    "standard",
    "*eta_bin1*et_bin0*","FOID2D_crack_10p0To20p0_1p442To1p566",
    "*eta_bin1*et_bin1*","FOID2D_crack_20p0To30p0_1p442To1p566",
    "*eta_bin1*et_bin2*","FOID2D_crack_30p0To40p0_1p442To1p566",
    "*eta_bin1*et_bin3*","FOID2D_crack_40p0To50p0_1p442To1p566",
    "*eta_bin1*et_bin4*","FOID2D_crack_50p0To200p0_1p442To1p566",
    "*et_bin0*","FOID2D_alleta_10p0To20p0_0p0To2p5",
    "*et_bin1*","FOID2D_alleta_20p0To30p0_0p0To2p5",
    "*et_bin2*","FOID2D_alleta_30p0To40p0_0p0To2p5",
    "*et_bin3*","FOID2D_alleta_40p0To50p0_0p0To2p5",
    "*et_bin4*","FOID2D_alleta_50p0To200p0_0p0To2p5",
    )
McTight2D3DBinningSpecification = McVetoBinningSpecification.clone()
McTight2D3DBinningSpecification.BinToPDFmap = cms.vstring(
    "standard",
    "*eta_bin1*et_bin0*","Tight2D3D_crack_10p0To20p0_1p442To1p566",
    "*eta_bin1*et_bin1*","Tight2D3D_crack_20p0To30p0_1p442To1p566",
    "*eta_bin1*et_bin2*","Tight2D3D_crack_30p0To40p0_1p442To1p566",
    "*eta_bin1*et_bin3*","Tight2D3D_crack_40p0To50p0_1p442To1p566",
    "*eta_bin1*et_bin4*","Tight2D3D_crack_50p0To200p0_1p442To1p566",
    "*et_bin0*","Tight2D3D_alleta_10p0To20p0_0p0To2p5",
    "*et_bin1*","Tight2D3D_alleta_20p0To30p0_0p0To2p5",
    "*et_bin2*","Tight2D3D_alleta_30p0To40p0_0p0To2p5",
    "*et_bin3*","Tight2D3D_alleta_40p0To50p0_0p0To2p5",
    "*et_bin4*","Tight2D3D_alleta_50p0To200p0_0p0To2p5",
    )
McTightID2D3DBinningSpecification = McVetoBinningSpecification.clone()
McTightID2D3DBinningSpecification.BinToPDFmap = cms.vstring(
    "standard",
    "*eta_bin1*et_bin0*","TightID2D3D_crack_10p0To20p0_1p442To1p566",
    "*eta_bin1*et_bin1*","TightID2D3D_crack_20p0To30p0_1p442To1p566",
    "*eta_bin1*et_bin2*","TightID2D3D_crack_30p0To40p0_1p442To1p566",
    "*eta_bin1*et_bin3*","TightID2D3D_crack_40p0To50p0_1p442To1p566",
    "*eta_bin1*et_bin4*","TightID2D3D_crack_50p0To200p0_1p442To1p566",
    "*et_bin0*","TightID2D3D_alleta_10p0To20p0_0p0To2p5",
    "*et_bin1*","TightID2D3D_alleta_20p0To30p0_0p0To2p5",
    "*et_bin2*","TightID2D3D_alleta_30p0To40p0_0p0To2p5",
    "*et_bin3*","TightID2D3D_alleta_40p0To50p0_0p0To2p5",
    "*et_bin4*","TightID2D3D_alleta_50p0To200p0_0p0To2p5",
    )
McMediumMiniBinningSpecification = cms.PSet(
    UnbinnedVariables = cms.vstring("mass", "totWeight", "Ele_dRTau", "probe_dRTau"),
    BinnedVariables = cms.PSet(IsoEfficiencyBins, mcTrue = cms.vstring("true")),
    BinToPDFmap = cms.vstring(
        "standard",
        "*eta_bin1*et_bin0*","MediumMini_crack_10p0To20p0_1p442To1p566",
        "*eta_bin1*et_bin1*","MediumMini_crack_20p0To30p0_1p442To1p566",
        "*eta_bin1*et_bin2*","MediumMini_crack_30p0To40p0_1p442To1p566",
        "*eta_bin1*et_bin3*","MediumMini_crack_40p0To50p0_1p442To1p566",
        "*eta_bin1*et_bin4*","MediumMini_crack_50p0To200p0_1p442To1p566",
        "*et_bin0*","MediumMini_alleta_10p0To20p0_0p0To2p5",
        "*et_bin1*","MediumMini_alleta_20p0To30p0_0p0To2p5",
        "*et_bin2*","MediumMini_alleta_30p0To40p0_0p0To2p5",
        "*et_bin3*","MediumMini_alleta_40p0To50p0_0p0To2p5",
        "*et_bin4*","MediumMini_alleta_50p0To200p0_0p0To2p5",
        ),
    )
McMediumMini4BinningSpecification = McMediumMiniBinningSpecification.clone()
McMediumMini4BinningSpecification.BinToPDFmap = cms.vstring(
    "standard",
    "*eta_bin1*et_bin0*","MediumMini4_crack_10p0To20p0_1p442To1p566",
    "*eta_bin1*et_bin1*","MediumMini4_crack_20p0To30p0_1p442To1p566",
    "*eta_bin1*et_bin2*","MediumMini4_crack_30p0To40p0_1p442To1p566",
    "*eta_bin1*et_bin3*","MediumMini4_crack_40p0To50p0_1p442To1p566",
    "*eta_bin1*et_bin4*","MediumMini4_crack_50p0To200p0_1p442To1p566",
    "*et_bin0*","MediumMini4_alleta_10p0To20p0_0p0To2p5",
    "*et_bin1*","MediumMini4_alleta_20p0To30p0_0p0To2p5",
    "*et_bin2*","MediumMini4_alleta_30p0To40p0_0p0To2p5",
    "*et_bin3*","MediumMini4_alleta_40p0To50p0_0p0To2p5",
    "*et_bin4*","MediumMini4_alleta_50p0To200p0_0p0To2p5",
    )
McMVAVLooseMiniBinningSpecification = McMediumMiniBinningSpecification.clone()
McMVAVLooseMiniBinningSpecification.BinToPDFmap = cms.vstring(
    "standard",
    "*eta_bin1*et_bin0*","MVAVLooseMini_crack_10p0To20p0_1p442To1p566",
    "*eta_bin1*et_bin1*","MVAVLooseMini_crack_20p0To30p0_1p442To1p566",
    "*eta_bin1*et_bin2*","MVAVLooseMini_crack_30p0To40p0_1p442To1p566",
    "*eta_bin1*et_bin3*","MVAVLooseMini_crack_40p0To50p0_1p442To1p566",
    "*eta_bin1*et_bin4*","MVAVLooseMini_crack_50p0To200p0_1p442To1p566",
    "*et_bin0*","MVAVLooseMini_alleta_10p0To20p0_0p0To2p5",
    "*et_bin1*","MVAVLooseMini_alleta_20p0To30p0_0p0To2p5",
    "*et_bin2*","MVAVLooseMini_alleta_30p0To40p0_0p0To2p5",
    "*et_bin3*","MVAVLooseMini_alleta_40p0To50p0_0p0To2p5",
    "*et_bin4*","MVAVLooseMini_alleta_50p0To200p0_0p0To2p5",
    )
McMVAVLooseMini4BinningSpecification = McMediumMiniBinningSpecification.clone()
McMVAVLooseMini4BinningSpecification.BinToPDFmap = cms.vstring(
    "standard",
    "*eta_bin1*et_bin0*","MVAVLooseMini4_crack_10p0To20p0_1p442To1p566",
    "*eta_bin1*et_bin1*","MVAVLooseMini4_crack_20p0To30p0_1p442To1p566",
    "*eta_bin1*et_bin2*","MVAVLooseMini4_crack_30p0To40p0_1p442To1p566",
    "*eta_bin1*et_bin3*","MVAVLooseMini4_crack_40p0To50p0_1p442To1p566",
    "*eta_bin1*et_bin4*","MVAVLooseMini4_crack_50p0To200p0_1p442To1p566",
    "*et_bin0*","MVAVLooseMini4_alleta_10p0To20p0_0p0To2p5",
    "*et_bin1*","MVAVLooseMini4_alleta_20p0To30p0_0p0To2p5",
    "*et_bin2*","MVAVLooseMini4_alleta_30p0To40p0_0p0To2p5",
    "*et_bin3*","MVAVLooseMini4_alleta_40p0To50p0_0p0To2p5",
    "*et_bin4*","MVAVLooseMini4_alleta_50p0To200p0_0p0To2p5",
    )
McMVAVLooseConvIHit1BinningSpecification = McMediumMiniBinningSpecification.clone()
McMVAVLooseConvIHit1BinningSpecification.BinToPDFmap = cms.vstring(
    "standard",
    "*eta_bin1*et_bin0*","MVAVLooseConvIHit1_crack_10p0To20p0_1p442To1p566",
    "*eta_bin1*et_bin1*","MVAVLooseConvIHit1_crack_20p0To30p0_1p442To1p566",
    "*eta_bin1*et_bin2*","MVAVLooseConvIHit1_crack_30p0To40p0_1p442To1p566",
    "*eta_bin1*et_bin3*","MVAVLooseConvIHit1_crack_40p0To50p0_1p442To1p566",
    "*eta_bin1*et_bin4*","MVAVLooseConvIHit1_crack_50p0To200p0_1p442To1p566",
    "*et_bin0*","MVAVLooseConvIHit1_alleta_10p0To20p0_0p0To2p5",
    "*et_bin1*","MVAVLooseConvIHit1_alleta_20p0To30p0_0p0To2p5",
    "*et_bin2*","MVAVLooseConvIHit1_alleta_30p0To40p0_0p0To2p5",
    "*et_bin3*","MVAVLooseConvIHit1_alleta_40p0To50p0_0p0To2p5",
    "*et_bin4*","MVAVLooseConvIHit1_alleta_50p0To200p0_0p0To2p5",
    )
McMVATightConvIHit0ChgBinningSpecification = McMediumMiniBinningSpecification.clone()
McMVATightConvIHit0ChgBinningSpecification.BinToPDFmap = cms.vstring(
    "standard",
    "*eta_bin1*et_bin0*","MVATightConvIHit0Chg_crack_10p0To20p0_1p442To1p566",
    "*eta_bin1*et_bin1*","MVATightConvIHit0Chg_crack_20p0To30p0_1p442To1p566",
    "*eta_bin1*et_bin2*","MVATightConvIHit0Chg_crack_30p0To40p0_1p442To1p566",
    "*eta_bin1*et_bin3*","MVATightConvIHit0Chg_crack_40p0To50p0_1p442To1p566",
    "*eta_bin1*et_bin4*","MVATightConvIHit0Chg_crack_50p0To200p0_1p442To1p566",
    "*et_bin0*","MVATightConvIHit0Chg_alleta_10p0To20p0_0p0To2p5",
    "*et_bin1*","MVATightConvIHit0Chg_alleta_20p0To30p0_0p0To2p5",
    "*et_bin2*","MVATightConvIHit0Chg_alleta_30p0To40p0_0p0To2p5",
    "*et_bin3*","MVATightConvIHit0Chg_alleta_40p0To50p0_0p0To2p5",
    "*et_bin4*","MVATightConvIHit0Chg_alleta_50p0To200p0_0p0To2p5",
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
DataMediumMiniBinningSpecification = McMediumMiniBinningSpecification.clone()
DataMediumMiniBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataMediumMiniBinningSpecification.BinnedVariables = cms.PSet(IsoEfficiencyBins)
DataMediumMini4BinningSpecification = McMediumMini4BinningSpecification.clone()
DataMediumMini4BinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataMediumMini4BinningSpecification.BinnedVariables = cms.PSet(IsoEfficiencyBins)
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


############################################################################################
############################################################################################
####### GsfElectron->Id / selection efficiency 
############################################################################################
############################################################################################

process.McGsfElectronToVeto = cms.EDAnalyzer(
    "TagProbeFitTreeAnalyzer",
    InputFileNames = cms.vstring("current/TnPTree_mc_norm.root"),
    InputDirectoryName = cms.string("GsfElectronToID"),
    InputTreeName = cms.string("fitter_tree"), 
    OutputFileName = cms.string("eff_mc_veto.root"),
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
        probe_ele_Act = cms.vstring("Probe Activity", "0", "100000000", ""), 
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
process.McGsfElectronToLoose2D.OutputFileName = cms.string("eff_mc_loose2D.root")
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

process.McMediumElectronToMini = process.McGsfElectronToMedium.clone()
process.McMediumElectronToMini.InputDirectoryName = cms.string("MediumElectronToIso")
process.McMediumElectronToMini.OutputFileName = cms.string("eff_mc_mediummini_"+trail+".root")
process.McMediumElectronToMini.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingMini = cms.vstring("passingMini", "dummy[pass=1,fail=0]"),
    )
process.McMediumElectronToMini.Efficiencies = cms.PSet(
    MCtruth_Mini = cms.PSet(
        McMediumMiniBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMini", "pass"),
        ),
    )

process.McMediumElectronToMini4 = process.McMediumElectronToMini.clone()
process.McMediumElectronToMini4.InputDirectoryName = cms.string("MediumElectronToIso")
process.McMediumElectronToMini4.OutputFileName = cms.string("eff_mc_mediummini4_"+trail+".root")
process.McMediumElectronToMini4.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingMini4 = cms.vstring("passingMini4", "dummy[pass=1,fail=0]"),
    )
process.McMediumElectronToMini4.Efficiencies = cms.PSet(
    MCtruth_Mini4 = cms.PSet(
        McMediumMini4BinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMini4", "pass"),
        ),
    )

process.McMVAVLooseElectronToMini = process.McMediumElectronToMini.clone()
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

process.McMVAVLooseElectronToMini4 = process.McMediumElectronToMini.clone()
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

process.McMVAVLooseElectronToConvIHit1 = process.McMediumElectronToMini.clone()
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

process.McMVATightElectronToConvIHit0Chg = process.McMediumElectronToMini.clone()
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

process.DataGsfElectronToVeto = process.McGsfElectronToVeto.clone()
process.DataGsfElectronToVeto.InputFileNames = cms.vstring("current/TnPTree_data.root")
process.DataGsfElectronToVeto.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToVeto.OutputFileName = cms.string("eff_data_veto.root")
process.DataGsfElectronToVeto.doCutAndCount = cms.bool(False)
delattr(process.DataGsfElectronToVeto, "WeightVariable")
process.DataGsfElectronToVeto.Variables = cms.PSet(
    mass = cms.vstring("Tag-Probe Mass", "60.0", "120.0", "GeV/c^{2}"),
    probe_sc_et = cms.vstring("Probe E_{T}", "10", "200", "GeV/c"),
    probe_sc_abseta = cms.vstring("Probe #eta", "0", "2.5", ""), 
    probe_ele_Act = cms.vstring("Probe Activity", "0", "100000000", ""), 
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

process.DataMediumElectronToMini = process.DataGsfElectronToVeto.clone()
process.DataMediumElectronToMini.InputDirectoryName = cms.string("MediumElectronToIso")
process.DataMediumElectronToMini.OutputFileName = cms.string("eff_data_mediummini_"+trail+".root")
process.DataMediumElectronToMini.Categories = cms.PSet(passingMini = cms.vstring("passingMini", "dummy[pass=1,fail=0]"))
process.DataMediumElectronToMini.Efficiencies = cms.PSet(
    Mini = cms.PSet(
        DataMediumMiniBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMini", "pass"),
        ),
    )

process.DataMediumElectronToMini4 = process.DataMediumElectronToMini.clone()
process.DataMediumElectronToMini4.InputDirectoryName = cms.string("MediumElectronToIso")
process.DataMediumElectronToMini4.OutputFileName = cms.string("eff_data_mediummini4_"+trail+".root")
process.DataMediumElectronToMini4.Categories = cms.PSet(passingMini4 = cms.vstring("passingMini4", "dummy[pass=1,fail=0]"))
process.DataMediumElectronToMini4.Efficiencies = cms.PSet(
    Mini4 = cms.PSet(
        DataMediumMini4BinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMini4", "pass"),
        ),
    )

process.DataMVAVLooseElectronToMini = process.DataMediumElectronToMini.clone()
process.DataMVAVLooseElectronToMini.InputDirectoryName = cms.string("MVAVLooseElectronToIso")
process.DataMVAVLooseElectronToMini.OutputFileName = cms.string("eff_data_mvavloosemini_"+trail+".root")
process.DataMVAVLooseElectronToMini.Categories = cms.PSet(passingMini = cms.vstring("passingMini", "dummy[pass=1,fail=0]"))
process.DataMVAVLooseElectronToMini.Efficiencies = cms.PSet(
    Mini = cms.PSet(
        DataMVAVLooseMiniBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMini", "pass"),
        ),
    )

process.DataMVAVLooseElectronToMini4 = process.DataMediumElectronToMini.clone()
process.DataMVAVLooseElectronToMini4.InputDirectoryName = cms.string("MVAVLooseElectronToIso")
process.DataMVAVLooseElectronToMini4.OutputFileName = cms.string("eff_data_mvavloosemini4_"+trail+".root")
process.DataMVAVLooseElectronToMini4.Categories = cms.PSet(passingMini4 = cms.vstring("passingMini4", "dummy[pass=1,fail=0]"))
process.DataMVAVLooseElectronToMini4.Efficiencies = cms.PSet(
    Mini4 = cms.PSet(
        DataMVAVLooseMini4BinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMini4", "pass"),
        ),
    )

process.DataMVAVLooseElectronToConvIHit1 = process.DataMediumElectronToMini.clone()
process.DataMVAVLooseElectronToConvIHit1.InputDirectoryName = cms.string("MVAVLooseElectronToIso")
process.DataMVAVLooseElectronToConvIHit1.OutputFileName = cms.string("eff_data_mvavlooseconvihit1_"+trail+".root")
process.DataMVAVLooseElectronToConvIHit1.Categories = cms.PSet(passingConvIHit1 = cms.vstring("passingConvIHit1", "dummy[pass=1,fail=0]"))
process.DataMVAVLooseElectronToConvIHit1.Efficiencies = cms.PSet(
    ConvIHit1 = cms.PSet(
        DataMVAVLooseConvIHit1BinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingConvIHit1", "pass"),
        ),
    )

process.DataMVATightElectronToConvIHit0Chg = process.DataMediumElectronToMini.clone()
process.DataMVATightElectronToConvIHit0Chg.InputDirectoryName = cms.string("MVATightElectronToIso")
process.DataMVATightElectronToConvIHit0Chg.OutputFileName = cms.string("eff_data_mvavlooseconvihit0chg_"+trail+".root")
process.DataMVATightElectronToConvIHit0Chg.Categories = cms.PSet(passingConvIHit0Chg = cms.vstring("passingConvIHit0Chg", "dummy[pass=1,fail=0]"))
process.DataMVATightElectronToConvIHit0Chg.Efficiencies = cms.PSet(
    ConvIHit0Chg = cms.PSet(
        DataMVATightConvIHit0ChgBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingConvIHit0Chg", "pass"),
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
    process.seq += process.McMediumElectronToMini
    process.seq += process.McMediumElectronToMini4
    process.seq += process.McMVAVLooseElectronToMini
    process.seq += process.McMVAVLooseElectronToMini4
    process.seq += process.McMVAVLooseElectronToConvIHit1
    process.seq += process.McMVATightElectronToConvIHit0Chg

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
    process.seq += process.DataMediumElectronToMini
    process.seq += process.DataMediumElectronToMini4
    process.seq += process.DataMVAVLooseElectronToMini
    process.seq += process.DataMVAVLooseElectronToMini4
    process.seq += process.DataMVAVLooseElectronToConvIHit1
    process.seq += process.DataMVATightElectronToConvIHit0Chg

process.fit = cms.Path(process.seq)
