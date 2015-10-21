#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/Common/interface/View.h"

#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include "DataFormats/L1Trigger/interface/L1EmParticle.h"
#include "DataFormats/L1Trigger/interface/L1EmParticleFwd.h"

#include "DataFormats/Math/interface/deltaR.h"

namespace{
  typedef bool MyBool;

  template<typename T>
    void Store(edm::Event &iEvent,
	       const edm::Handle<std::vector<pat::Electron> > &probes,
	       const std::vector<T> &values,
	       const std::string &name){
    std::auto_ptr<edm::ValueMap<T> > valMap(new edm::ValueMap<T>());
    typename edm::ValueMap<T>::Filler filler(*valMap);
    filler.insert(probes, values.begin(), values.end());
    filler.fill();
    iEvent.put(valMap, name);
  }

  std::vector<bool> And(const std::vector<bool> &a, std::vector<bool> b){
    size_t min_size = a.size(), max_size = b.size();
    if(a.size() > b.size()){
      size_t temp = min_size;
      min_size = max_size;
      max_size = temp;
    }
    std::vector<bool> result(max_size);
    for(size_t i = 0; i < max_size; ++i){
      if(i < min_size){
	result.at(i) = a.at(i) && b.at(i);
      }else{
	result.at(i) = false;
      }
    }
    return result;
  }

  bool PassMVAVLooseFO(double mva, double abssceta){
    if(abssceta<0.8){
      return mva > -0.7;
    }else if(abssceta<1.479){
      return mva > -0.83;
    }else if(abssceta<2.5){
      return mva > -0.92;
    }else{
      return false;
    }
  }

  bool PassMVAVLoose(double mva, double abssceta){
    if(abssceta<0.8){
      return mva > -0.16;
    }else if(abssceta<1.479){
      return mva > -0.65;
    }else if(abssceta<2.5){
      return mva > -0.74;
    }else{
      return false;
    }
  }

  bool PassMVATight(double mva, double abssceta){
    if(abssceta<0.8){
      return mva > 0.87;
    }else if(abssceta<1.479){
      return mva > 0.60;
    }else if(abssceta<2.5){
      return mva > 0.17;
    }else{
      return false;
    }
  }

  bool PassTightIP2D(double dxy, double dz){
    return fabs(dxy) < 0.05 && fabs(dz) < 0.1;
  }

  bool PassIDEmu(const pat::Electron &ele){
    if(ele.isEB()){
      return ele.sigmaIetaIeta() < 0.011
	&& ele.hadronicOverEm() < 0.08
	&& fabs(ele.deltaEtaSuperClusterTrackAtVtx()) < 0.01
	&& fabs(ele.deltaPhiSuperClusterTrackAtVtx()) < 0.04
	&& fabs(1./ele.ecalEnergy() - ele.eSuperClusterOverP()/ele.ecalEnergy()) < 0.01;
    }else if(ele.isEE()){
      return ele.sigmaIetaIeta() < 0.031
	&& ele.hadronicOverEm() < 0.08
	&& fabs(ele.deltaEtaSuperClusterTrackAtVtx()) < 0.01
	&& fabs(ele.deltaPhiSuperClusterTrackAtVtx()) < 0.08
	&& fabs(1./ele.ecalEnergy() - ele.eSuperClusterOverP()/ele.ecalEnergy()) < 0.01;
    }else{
      return false;
    }
  }

  bool PassISOEmu(const pat::Electron &ele){
    return ele.ecalPFClusterIso() / ele.pt() < 0.45
      && ele.hcalPFClusterIso() / ele.pt() < 0.25
      && ele.dr03TkSumPt() / ele.pt() < 0.2;
  }
}

class MyElectronVariableHelper : public edm::EDProducer {
public:
  explicit MyElectronVariableHelper(const edm::ParameterSet & iConfig);
  virtual ~MyElectronVariableHelper() ;
  
  virtual void produce(edm::Event & iEvent, const edm::EventSetup & iSetup) override;
  
private:
  edm::EDGetTokenT<std::vector<pat::Electron> > probesToken_;
  edm::EDGetTokenT<edm::View<reco::Candidate> > probesViewToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > mvaToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > dxyToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > dzToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > miniIsoToken_;
};

MyElectronVariableHelper::MyElectronVariableHelper(const edm::ParameterSet & iConfig) :
  probesToken_(consumes<std::vector<pat::Electron> >(iConfig.getParameter<edm::InputTag>("probes"))),
  probesViewToken_(consumes<edm::View<reco::Candidate> >(iConfig.getParameter<edm::InputTag>("probes"))),
  mvaToken_(consumes<edm::ValueMap<float> >(iConfig.getParameter<edm::InputTag>("mvas"))),
  dxyToken_(consumes<edm::ValueMap<float> >(iConfig.getParameter<edm::InputTag>("dxy"))),
  dzToken_(consumes<edm::ValueMap<float> >(iConfig.getParameter<edm::InputTag>("dz"))),
  miniIsoToken_(consumes<edm::ValueMap<float> >(iConfig.getParameter<edm::InputTag>("miniIso"))){
  produces<edm::ValueMap<float> >("sip3d");
  produces<edm::ValueMap<float> >("ecalIso");
  produces<edm::ValueMap<float> >("hcalIso");
  produces<edm::ValueMap<float> >("trackIso");
  produces<edm::ValueMap<int> >("missIHits");
  produces<edm::ValueMap<MyBool> >("passConvVeto");
  produces<edm::ValueMap<MyBool> >("passMVAVLooseFO");
  produces<edm::ValueMap<MyBool> >("passMVAVLoose");
  produces<edm::ValueMap<MyBool> >("passMVAVLooseMini");
  produces<edm::ValueMap<MyBool> >("passMVAVLooseMini4");
  produces<edm::ValueMap<MyBool> >("passMVATight");
  produces<edm::ValueMap<MyBool> >("passTightIP2D");
  produces<edm::ValueMap<MyBool> >("passTightIP3D");
  produces<edm::ValueMap<MyBool> >("passIDEmu");
  produces<edm::ValueMap<MyBool> >("passISOEmu");
  produces<edm::ValueMap<MyBool> >("passCharge");
  produces<edm::ValueMap<MyBool> >("passIHit0");
  produces<edm::ValueMap<MyBool> >("passIHit1");
  produces<edm::ValueMap<MyBool> >("passLoose2D");
  produces<edm::ValueMap<MyBool> >("passFOID2D");
  produces<edm::ValueMap<MyBool> >("passTight2D3D");
  produces<edm::ValueMap<MyBool> >("passTightID2D3D");
  produces<edm::ValueMap<MyBool> >("passConvIHit1");
  produces<edm::ValueMap<MyBool> >("passConvIHit0Chg");
}

MyElectronVariableHelper::~MyElectronVariableHelper(){
}

void MyElectronVariableHelper::produce(edm::Event & iEvent, const edm::EventSetup & iSetup) {
  // read input
  edm::Handle<std::vector<pat::Electron> > probes;
  iEvent.getByToken(probesToken_,  probes);
  edm::Handle<edm::View<reco::Candidate> > probes_view;
  iEvent.getByToken(probesViewToken_, probes_view);
  edm::Handle<edm::ValueMap<float> > mvas;
  iEvent.getByToken(mvaToken_, mvas);
  edm::Handle<edm::ValueMap<float> > dxys;
  iEvent.getByToken(dxyToken_, dxys);
  edm::Handle<edm::ValueMap<float> > dzs;
  iEvent.getByToken(dzToken_, dzs);
  edm::Handle<edm::ValueMap<float> > miniIsos;
  iEvent.getByToken(miniIsoToken_, miniIsos);

  // prepare vector for output
  std::vector<float> sip3dValues;
  std::vector<float> ecalIsoValues;
  std::vector<float> hcalIsoValues;
  std::vector<float> trackIsoValues;
  std::vector<int> missingInnerHitsValues;
  std::vector<MyBool> passConversionVeto;
  std::vector<MyBool> passMVAVLooseFO;
  std::vector<MyBool> passMVAVLoose;
  std::vector<MyBool> passMVAVLooseMini;
  std::vector<MyBool> passMVAVLooseMini4;
  std::vector<MyBool> passMVATight;
  std::vector<MyBool> passTightIP2D;
  std::vector<MyBool> passTightIP3D;
  std::vector<MyBool> passIDEmu;
  std::vector<MyBool> passISOEmu;
  std::vector<MyBool> passCharge;
  std::vector<MyBool> passIHit0;
  std::vector<MyBool> passIHit1;

  size_t i = 0;
  for(const auto &probe: *probes){
    edm::RefToBase<reco::Candidate> pp = probes_view->refAt(i);

    double ip3d = probe.dB(pat::Electron::PV3D);
    double ip3d_err = probe.edB(pat::Electron::PV3D);
    double sip3d = ip3d/ip3d_err;
    double mva = (*mvas)[pp];
    double dxy = (*dxys)[pp];
    double dz = (*dzs)[pp];
    double mini_iso = (*miniIsos)[pp];
    double ecalIso = probe.ecalPFClusterIso();
    double hcalIso = probe.hcalPFClusterIso();
    double trackIso = probe.dr03TkSumPt();
    int missingInnerHits = probe.gsfTrack()->hitPattern().numberOfHits(reco::HitPattern::MISSING_INNER_HITS);

    sip3dValues.push_back(sip3d);
    ecalIsoValues.push_back(ecalIso);
    hcalIsoValues.push_back(hcalIso);
    trackIsoValues.push_back(trackIso);
    missingInnerHitsValues.push_back(missingInnerHits);
    passConversionVeto.push_back(probe.passConversionVeto());
    passMVAVLooseFO.push_back(PassMVAVLooseFO(mva, fabs(probe.superCluster()->eta())));
    passMVAVLoose.push_back(PassMVAVLoose(mva, fabs(probe.superCluster()->eta())));
    passMVAVLooseMini.push_back(PassMVAVLoose(mva, fabs(probe.superCluster()->eta())) && mini_iso<0.1);
    passMVAVLooseMini4.push_back(PassMVAVLoose(mva, fabs(probe.superCluster()->eta())) && mini_iso<0.4);
    passMVATight.push_back(PassMVATight(mva, fabs(probe.superCluster()->eta())));
    passTightIP2D.push_back(PassTightIP2D(dxy, dz));
    passTightIP3D.push_back(fabs(sip3d < 4.));
    passIDEmu.push_back(PassIDEmu(probe));
    passISOEmu.push_back(PassISOEmu(probe));
    passCharge.push_back(probe.isGsfCtfScPixChargeConsistent());
    passIHit0.push_back(missingInnerHits == 0);
    passIHit1.push_back(missingInnerHits <= 1);
    ++i;
  }

  // convert into ValueMap and store
  Store(iEvent, probes, sip3dValues, "sip3d");
  Store(iEvent, probes, ecalIsoValues, "ecalIso");
  Store(iEvent, probes, hcalIsoValues, "hcalIso");
  Store(iEvent, probes, trackIsoValues, "trackIso");
  Store(iEvent, probes, missingInnerHitsValues, "missIHits");
  Store(iEvent, probes, passConversionVeto, "passConvVeto");
  Store(iEvent, probes, passMVAVLooseFO, "passMVAVLooseFO");
  Store(iEvent, probes, passMVAVLoose, "passMVAVLoose");
  Store(iEvent, probes, passMVAVLooseMini, "passMVAVLooseMini");
  Store(iEvent, probes, passMVAVLooseMini4, "passMVAVLooseMini4");
  Store(iEvent, probes, passMVATight, "passMVATight");
  Store(iEvent, probes, passTightIP2D, "passTightIP2D");
  Store(iEvent, probes, passTightIP3D, "passTightIP3D");
  Store(iEvent, probes, passIDEmu, "passIDEmu");
  Store(iEvent, probes, passISOEmu, "passISOEmu");
  Store(iEvent, probes, passCharge, "passCharge");
  Store(iEvent, probes, passIHit0, "passIHit0");
  Store(iEvent, probes, passIHit1, "passIHit1");
  Store(iEvent, probes, And(passMVAVLoose, passTightIP2D), "passLoose2D");
  Store(iEvent, probes, And(And(passMVAVLooseFO, passIDEmu), passTightIP2D), "passFOID2D");
  Store(iEvent, probes, And(And(passMVATight, passTightIP2D), passTightIP3D), "passTight2D3D");
  Store(iEvent, probes,
	And(And(And(passMVATight, passIDEmu), passTightIP2D), passTightIP3D),
	"passTightID2D3D");
  Store(iEvent, probes, And(passConversionVeto, passIHit1), "passConvIHit1");
  Store(iEvent, probes, And(And(passConversionVeto, passIHit1), passCharge), "passConvIHit0Chg");
}


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(MyElectronVariableHelper);
