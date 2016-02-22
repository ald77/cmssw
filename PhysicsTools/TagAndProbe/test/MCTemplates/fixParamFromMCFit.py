import ROOT
from optparse import OptionParser
from os import listdir
from os.path import isfile, join

def GetDirName(file_name):
    if file_name == "eff_mc_foid2d.root":
        return "GsfElectronToID/MCtruth_FOID2D"
    elif file_name == "eff_mc_loose.root":
        return "GsfElectronToID/MCtruth_Loose"
    elif file_name == "eff_mc_loose2d.root":
        return "GsfElectronToID/MCtruth_Loose2D"
    elif file_name == "eff_mc_medium.root":
        return "GsfElectronToID/MCtruth_Medium"
    elif file_name == "eff_mc_mvatightconvihit0chg_act.root":
        return "MVATightElectronToIso/MCtruth_ConvIHit0Chg"
    elif file_name == "eff_mc_mvatightconvihit0chg_eta.root":
        return "MVATightElectronToIso/MCtruth_ConvIHit0Chg"
    elif file_name == "eff_mc_mvatightmulti_act.root":
        return "MVATightElectronToIso/MCtruth_Multi"
    elif file_name == "eff_mc_mvatightmulti_eta.root":
        return "MVATightElectronToIso/MCtruth_Multi"
    elif file_name == "eff_mc_mvatightmultiemu_act.root":
        return "MVATightElectronToIso/MCtruth_MultiEmu"
    elif file_name == "eff_mc_mvatightmultiemu_eta.root":
        return "MVATightElectronToIso/MCtruth_MultiEmu"
    elif file_name == "eff_mc_mvavlooseconvihit1_act.root":
        return "MVAVLooseElectronToIso/MCtruth_ConvIHit1"
    elif file_name == "eff_mc_mvavlooseconvihit1_eta.root":
        return "MVAVLooseElectronToIso/MCtruth_ConvIHit1"
    elif file_name == "eff_mc_mvavloosemini4_act.root":
        return "MVAVLooseElectronToIso/MCtruth_Mini4"
    elif file_name == "eff_mc_mvavloosemini4_eta.root":
        return "MVAVLooseElectronToIso/MCtruth_Mini4"
    elif file_name == "eff_mc_mvavloosemini_act.root":
        return "MVAVLooseElectronToIso/MCtruth_Mini"
    elif file_name == "eff_mc_mvavloosemini_eta.root":
        return "MVAVLooseElectronToIso/MCtruth_Mini"
    elif file_name == "eff_mc_tight.root":
        return "GsfElectronToID/MCtruth_Tight"
    elif file_name == "eff_mc_tight2d3d.root":
        return "GsfElectronToID/MCtruth_Tight2D3D"
    elif file_name == "eff_mc_tightid2d3d.root":
        return "GsfElectronToID/MCtruth_TightID2D3D"
    elif file_name == "eff_mc_veto.root":
        return "GsfElectronToID/MCtruth_Veto"
    else:
        return None

def GetFitName(filename, keyname):
    pos = keyname.rfind("__")
    if pos == -1:
        return None
    else:
        return keyname[pos+2:]
    
def GetParamString(name, params):
    for p in xrange(params):
        param = params.at(p)
        if param.GetName() == name:
            if IsFixed(name):
                return "%s[%.3f]"%(myPar.GetName(), myPar.getVal())
            else:
                return "%s[%.3f,%.3f,%.3f]"%(myPar.GetName(), myPar.getVal(), myPar.getMin(), myPar.getMax())

    return None

def main(options):
    with open("../python/commonFit.py", "w") as out:
        out.write("import FWCore.ParameterSet.Config as cms\n")
        out.write("\n")

        block = 0

        files = [ filename for filename in listdir(options.input) if isfile(join(options.input,filename)) and "eff_mc_" in filename ]
        for filename in files:
            f = ROOT.TFile(options.input+"/"+filename)
            directory = f.Get(GetDirName(filename))
            directory.cd()
            keys = directory.GetListOfKeys()
            for key in keys:
                if "__" in key.GetName():
                    subdirectory = directory.Get(key.GetName())
                    subdirectory.cd();
                    results = subdirectory.Get("fitresults")
                    params = results.floatParsFinal()
                    if block%100:
                        if block!=0:
                            out.write(")\n")
                        out.write("block_"+str(block)+" = cms.PSet(\n")
                        maxblock = block
                        block += 1
                    out.write(GetFitName(filename, key.GetName())+" = cms.vstring(\n")
                    out.write("\"RooDoubleCBFast::signalResPass(mass,meanP[0.0,-10.000,10.000],sigmaP[0.956,0.00,10.000],alphaP1[0.999, 0.0,50.0],nP1[1.405,0.000,50.000],alphaP2[0.999,0.0,50.0],nP2[1.405,0.000,50.000])\",\n")
                    out.write("\"RooDoubleCBFast::signalResFail(mass,meanF[0.0,-10.000,10.000],sigmaF[3.331,0.00,10.000],alphaF1[1.586, 0.0,50.0],nF1[0.464,0.000,20.00],alphaF2[1.586,0.0,50.0],nF2[0.464,0.000,20.00])\",\n")
                    out.write("\"RooBreitWigner::signalPassBW(mass, mZpass[91.1876,80.,100.],sigmaZpass[2.4952,0.001,10.])\",\n")
                    out.write("\"RooBreitWigner::signalFailBW(mass, mZfail[91.1876,80.,100.],sigmaZfail[2.4952,0.001,10.])\",\n")
                    out.write("\"RooExponential::signalPassExp(mass, expRatePass["+str(params.at(params.index("expRatePass")).getVal())+"])\",\n")
                    out.write("\"RooExponential::signalFailExp(mass, expRateFail["+str(params.at(params.index("expRateFail")).getVal())+"])\",\n")
                    out.write("\"SUM::signalPhyPass(cPass["+str(params.at(params.index("cPass")).getVal())+"]*signalPassBW, signalPassExp)\",\n")
                    out.write("\"SUM::signalPhyFail(cFail["+str(params.at(params.index("cFail")).getVal())+"]*signalFailBW, signalFailExp)\",\n")
                    out.write("\"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.1, 0, 1], peakPass[90.0])\",\n")
                    out.write("\"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.1, 0, 1], peakFail[90.0])\",\n")
                    out.write("\"FCONV::signalPass(mass, signalPhyPass, signalResPass)\",\n")
                    out.write("\"FCONV::signalFail(mass, signalPhyFail, signalResFail)\",\n")
                    out.write("\"efficiency[0.5,0,1]\",\n")
                    out.write("\"signalFractionInPassing[1.0]\"\n")
                    out.write("),\n")
                    out.write("\n")

if __name__ == "__main__":  
    parser = OptionParser()
    parser.add_option("-i", "--input", default="2016_02_02_nominal", help="Input directory")
    (options, arg) = parser.parse_args()
     
    main(options)
