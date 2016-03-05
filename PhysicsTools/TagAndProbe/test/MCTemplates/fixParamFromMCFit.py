import ROOT
from optparse import OptionParser
from os import listdir
from os.path import isfile, join
from string import replace

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
    elif "RelAct" in keyname:
        return None
    else:
        output = keyname[pos+2:]
        if keyname.find("probe_sc_abseta_bin0") != -1:
            output = replace(output, "0p0To1p442", "0p0To0p8")
            output = replace(output, "0p0To2p5", "0p0To0p8")
        elif keyname.find("probe_sc_abseta_bin1") != -1:
            output = replace(output, "0p0To1p442", "0p8To1p442")
            output = replace(output, "0p0To2p5", "0p8To1p442")
        elif keyname.find("probe_sc_abseta_bin3") != -1:
            output = replace(output, "1p566To2p5", "1p566To2p0")
            output = replace(output, "0p0To2p5", "1p566To2p0")
        elif keyname.find("probe_sc_abseta_bin4") != -1:
            output = replace(output, "1p566To2p5", "2p0To2p5")
            output = replace(output, "0p0To2p5", "2p0To2p5")
        return output

def Fix(name, params):
    return name+"["+str(params.at(params.index(name)).getVal())+"]"
    
def Constrain(name, params):
    mid = params.at(params.index(name)).getVal()
    elo = abs(params.at(params.index(name)).getAsymErrorLo())
    if elo <= 0:
        elo = abs(params.at(params.index(name)).getError())
    ehi = abs(params.at(params.index(name)).getAsymErrorHi())
    if ehi <= 0:
        ehi = abs(params.at(params.index(name)).getError())
    top = params.at(params.index(name)).getMax()
    bot = params.at(params.index(name)).getMin()
    return name+"["+str(mid)+","+str(max(mid-10.*elo,bot))+","+str(min(mid+10.*ehi,top))+"]"
    
def Float(name, params):
    mid = params.at(params.index(name)).getVal()
    elo = params.at(params.index(name)).getMin()
    ehi = params.at(params.index(name)).getMax()
    return name+"["+str(mid)+","+str(elo)+","+str(ehi)+"]"
    
def main(options):
    with open("../python/commonFit.py", "w") as out:
        out.write("import FWCore.ParameterSet.Config as cms\n")
        out.write("\n")
        out.write("block_0 = cms.PSet(\n")

        entry = 0
        block = 0

        files = [ filename for filename in listdir(options.input) if isfile(join(options.input,filename)) and "eff_mc_" in filename ]
        for filename in files:
            f = ROOT.TFile(options.input+"/"+filename)
            directory = f.Get(GetDirName(filename))
            directory.cd()
            keys = directory.GetListOfKeys()
            for key in keys:
                if "__" not in key.GetName():
                    continue
                subdirectory = directory.Get(key.GetName())
                subdirectory.cd();
                results = subdirectory.Get("fitresults")
                params = results.floatParsFinal()
                if entry == 100:
                    entry = 0
                    block += 1
                    if block != 0:
                        out.write(")\n")
                    out.write("block_"+str(block)+" = cms.PSet(\n")
                else:
                    entry += 1
                if GetFitName(filename, key.GetName()) == None:
                    continue
                print filename+" "+GetDirName(filename)+" "+key.GetName()+" "+GetFitName(filename, key.GetName())
                out.write(GetFitName(filename, key.GetName())+" = cms.vstring(\n")
                out.write("\"RooDoubleCBFast::signalResPass(mass,"+Float("meanP",params)+","+Float("sigmaP",params)+","+Constrain("alphaP1",params)+","+Constrain("nP1",params)+","+Constrain("alphaP2",params)+","+Constrain("nP2",params)+")\",\n")
                out.write("\"RooDoubleCBFast::signalResFail(mass,"+Float("meanF",params)+","+Float("sigmaF",params)+","+Constrain("alphaF1",params)+","+Constrain("nF1",params)+","+Constrain("alphaF2",params)+","+Constrain("nF2",params)+")\",\n")
                out.write("\"RooBreitWigner::signalPassBWZ(mass, "+Float("mZpass",params)+","+Float("sigmaZpass",params)+")\",\n")
                out.write("\"RooBreitWigner::signalFailBWZ(mass, "+Float("mZfail",params)+","+Float("sigmaZfail",params)+")\",\n")
                out.write("\"RooBreitWigner::signalPassBWtail(mass, "+Fix("mtailpass",params)+","+Fix("sigmatailpass",params)+")\",\n")
                out.write("\"RooBreitWigner::signalFailBWtail(mass, "+Fix("mtailfail",params)+","+Fix("sigmatailfail",params)+")\",\n")
                out.write("\"RooGaussian::signalPassGaus(mass, "+Fix("meanVP",params)+","+Fix("sigmaVP",params)+")\",\n")
                out.write("\"RooGaussian::signalFailGaus(mass, "+Fix("meanVF",params)+","+Fix("sigmaVF",params)+")\",\n")
                out.write("\"FCONV::signalZPass(mass, signalPassBWZ, signalResPass)\",\n")
                out.write("\"FCONV::signalZFail(mass, signalFailBWZ, signalResFail)\",\n")
                out.write("\"FCONV::signalVoigtPass(mass, signalPassBWtail, signalPassGaus)\",\n")
                out.write("\"FCONV::signalVoigtFail(mass, signalFailBWtail, signalFailGaus)\",\n")
                out.write("\"SUM::signalPass("+Fix("cPass",params)+"*signalZPass,signalVoigtPass)\",\n")
                out.write("\"SUM::signalFail("+Fix("cFail",params)+"*signalZFail,signalVoigtFail)\",\n")
                out.write("\"RooCMSShape::backgroundPass(mass, "+Float("alphaPass",params)+", "+Float("betaPass",params)+", "+Float("gammaPass",params)+", peakPass[90.0])\",\n")
                out.write("\"RooCMSShape::backgroundFail(mass, "+Float("alphaFail",params)+", "+Float("betaFail",params)+", "+Float("gammaFail",params)+", peakFail[90.0])\",\n")
                out.write("\"efficiency["+str(params.at(params.index("efficiency")).getVal())+",0.,1.]\",\n")
                out.write("\"signalFractionInPassing[1.0]\"\n")
                out.write("),\n")
                out.write("\n")
        out.write(")\n")

        out.write("all_pdfs = cms.PSet(\n")
        for i in range(0,block+1):
            out.write("block_"+str(i)+",\n")
        out.write(")\n")

if __name__ == "__main__":  
    parser = OptionParser()
    parser.add_option("-i", "--input", default="2016_02_02_nominal", help="Input directory")
    (options, arg) = parser.parse_args()
     
    main(options)
