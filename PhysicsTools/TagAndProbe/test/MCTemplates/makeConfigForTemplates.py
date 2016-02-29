#FIXME ADD TEMPLATE FOR BG PDF CHOICE
import ROOT
from optparse import OptionParser
from getTemplatesFromMC import findBins

def main(options):
    var1s = []
    for v in options.var1Bins.split(","):
        var1s.append(float(v))
    var2s = []
    for v in options.var2Bins.split(","):
        var2s.append(float(v))
    
    outputFile = file(options.outputFile, "w")
    
    outputFile.write("import FWCore.ParameterSet.Config as cms\n\n")
    outputFile.write("all_pdfs = cms.PSet(\n")

    for binVar1 in xrange(len(var1s)-1):
        for binVar2 in xrange(len(var2s)-1):
            psetName = options.idLabel+"_"+str(var1s[binVar1])+"To"+str(var1s[binVar1+1])+"_"+str(var2s[binVar2])+"To"+str(var2s[binVar2+1])
            psetName = psetName.replace(".", "p")
            psetName = psetName.replace("-", "m")
            psetName = psetName + " = cms.vstring(\n"
            outputFile.write(psetName)

            #outputFile.write("\"RooDoubleCBFast::signalResPass(mass,meanP[0.0,-10.000,10.000],sigmaP[0.956,0.00,10.000],alphaP1[0.999, 0.0,50.0],nP1[1.405,0.000,50.000],alphaP2[0.999,0.0,50.0],nP2[1.405,0.000,50.000])\",\n")
            #outputFile.write("\"RooDoubleCBFast::signalResFail(mass,meanF[0.0,-10.000,10.000],sigmaF[3.331,0.00,10.000],alphaF1[1.586, 0.0,50.0],nF1[0.464,0.000,20.00],alphaF2[1.586,0.0,50.0],nF2[0.464,0.000,20.00])\",\n")
            #outputFile.write("\"RooCBShape::signalResPass(mass,meanP[0.0,-10.000,10.000],sigmaP[0.956,0.00,10.000],alphaP[0.999, 0.0,50.0],nP[1.405,0.000,50.000])\",\n")
            #outputFile.write("\"RooCBShape::signalResFail(mass,meanF[0.0,-10.000,10.000],sigmaF[3.331,0.00,10.000],alphaF[1.586, 0.0,50.0],nF[0.464,0.000,20.00])\",\n")
            outputFile.write("\"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])\",\n")
            outputFile.write("\"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])\",\n")
            histNameSt = "hMass_"+str(var1s[binVar1])+"To"+str(var1s[binVar1+1])+"_"+str(var2s[binVar2])+"To"+str(var2s[binVar2+1])
            outputFile.write("\"ZGeneratorLineShape::signalPhyPass(mass,\\\""+options.templateFile+"\\\", \\\""+histNameSt+"_Pass\\\")\",\n"),
            outputFile.write("\"ZGeneratorLineShape::signalPhyFail(mass,\\\""+options.templateFile+"\\\", \\\""+histNameSt+"_Fail\\\")\",\n"),
            #outputFile.write("\"ZGeneratorLineShape::signalPhyPass(mass,\\\""+"../data/ZeeGenLevel.root"+"\\\", \\\"Mass\\\")\",\n"),
            #outputFile.write("\"ZGeneratorLineShape::signalPhyFail(mass,\\\""+"../data/ZeeGenLevel.root"+"\\\", \\\"Mass\\\)\",\n"),
            outputFile.write(options.passBkgPdf+",\n")
            outputFile.write(options.failBkgPdf+",\n")
            outputFile.write("\"FCONV::signalPass(mass, signalPhyPass, signalResPass)\",\n")
            outputFile.write("\"FCONV::signalFail(mass, signalPhyFail, signalResFail)\",\n")     
            #outputFile.write("\"RooDoubleCBFast::signalResPass(mass,meanP[0.0,-10.000,10.000],sigmaP[0.956,0.00,10.000],alphaP1[0.999, 0.0,50.0],nP1[1.405,0.000,50.000],alphaP2[0.999,0.0,50.0],nP2[1.405,0.000,50.000])\",\n")
            #outputFile.write("\"RooDoubleCBFast::signalResFail(mass,meanF[0.0,-10.000,10.000],sigmaF[3.331,0.00,10.000],alphaF1[1.586, 0.0,50.0],nF1[0.464,0.000,20.00],alphaF2[1.586,0.0,50.0],nF2[0.464,0.000,20.00])\",\n")
            #outputFile.write("\"RooBreitWigner::signalPassBWZ(mass, mZpass[91.1876,80.,100.],sigmaZpass[2.4952,0.001,10.])\",\n")
            #outputFile.write("\"RooBreitWigner::signalFailBWZ(mass, mZfail[91.1876,80.,100.],sigmaZfail[2.4952,0.001,10.])\",\n")
            #outputFile.write("\"RooBreitWigner::signalPassBWtail(mass, mtailpass[70.,60.,80.],sigmatailpass[10.,0.001,30.])\",\n")
            #outputFile.write("\"RooBreitWigner::signalFailBWtail(mass, mtailfail[70.,60.,80.],sigmatailfail[10.,0.001,30.])\",\n")
            #outputFile.write("\"RooGaussian::signalPassGaus(mass, meanVP[0.0,-10.,10.],sigmaVP[10.,0.001,30.])\",\n")
            #outputFile.write("\"RooGaussian::signalFailGaus(mass, meanVF[0.0,-10.,10.],sigmaVF[10.,0.001,30.])\",\n")
            #outputFile.write("\"FCONV::signalZPass(mass, signalPassBWZ, signalResPass)\",\n")
            #outputFile.write("\"FCONV::signalZFail(mass, signalFailBWZ, signalResFail)\",\n")
            #outputFile.write("\"FCONV::signalVoigtPass(mass, signalPassBWtail, signalPassGaus)\",\n")
            #outputFile.write("\"FCONV::signalVoigtFail(mass, signalFailBWtail, signalFailGaus)\",\n")
            #outputFile.write("\"SUM::signalPass(cPass[0.9,0.0,1.0]*signalZPass,signalVoigtPass)\",\n")
            #outputFile.write("\"SUM::signalFail(cFail[0.7,0.0,1.0]*signalZFail,signalVoigtFail)\",\n")
            outputFile.write("\"efficiency[0.5,0,1]\",\n")
            outputFile.write("\"signalFractionInPassing[1.0]\"\n")     
            outputFile.write("),\n")
            outputFile.write("\n")
    outputFile.write(")")
    outputFile.close()

if __name__ == "__main__":  
    parser = OptionParser()

    parser.add_option("-i", "--idLabel", default="pdf", help="Prefix for block of PDFs")
    parser.add_option("-o", "--outputFile", default="../../python/commonFit.py", help="Output filename")
    parser.add_option("-t", "--templateFile", default="templatesID.root", help="Output filename")
    parser.add_option("", "--var1Bins", default="20,30,40,50,200", help="Binning to use in var1")
    parser.add_option("", "--var2Bins", default="0.0,1.0,1.4442,1.566,2.0,2.5", help="Binning to use in var2")
    parser.add_option("", "--failBkgPdf", default="\"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.1, 0, 1], peakFail[90.0])\"", help="Background PDF for passing probes")
    parser.add_option("", "--passBkgPdf", default="\"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.1, 0, 1], peakPass[90.0])\"", help="Background PDF for failing probes")
    #parser.add_option("", "--failBkgPdf", default="\"RooExponential::backgroundFail(mass, expRateFail[-0.1,-10.,0.])\"", help="Background PDF for passing probes")
    #parser.add_option("", "--passBkgPdf", default="\"RooExponential::backgroundPass(mass, expRatePass[-0.1,-10.,0.])\"", help="Background PDF for failing probes")

    (options, arg) = parser.parse_args()
     
    main(options)
