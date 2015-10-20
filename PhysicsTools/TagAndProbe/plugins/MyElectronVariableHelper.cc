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
};

MyElectronVariableHelper::MyElectronVariableHelper(const edm::ParameterSet & iConfig) :
  probesToken_(consumes<std::vector<pat::Electron> >(iConfig.getParameter<edm::InputTag>("probes"))),
  probesViewToken_(consumes<edm::View<reco::Candidate> >(iConfig.getParameter<edm::InputTag>("probes"))),
  mvaToken_(consumes<edm::ValueMap<float> >(iConfig.getParameter<edm::InputTag>("mvas"))){
  produces<edm::ValueMap<float> >("sip3d");
  produces<edm::ValueMap<MyBool> >("passConvVeto");
  produces<edm::ValueMap<MyBool> >("passMVAVLooseFO");
  produces<edm::ValueMap<MyBool> >("passMVAVLoose");
  produces<edm::ValueMap<MyBool> >("passMVATight");
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

  // prepare vector for output
  std::vector<float> sip3dValues;
  std::vector<MyBool> passConvVetoValues;
  std::vector<MyBool> passMVAVLooseFO;
  std::vector<MyBool> passMVAVLoose;
  std::vector<MyBool> passMVATight;

  size_t i = 0;
  for(auto probe = probes->cbegin(); probe != probes->cend(); ++probe){
    sip3dValues.push_back(probe->dB(pat::Electron::PV3D)/probe->edB(pat::Electron::PV3D));
    passConvVetoValues.push_back(probe->passConversionVeto());
    edm::RefToBase<reco::Candidate> pp = probes_view->refAt(i);
    passMVAVLooseFO.push_back(PassMVAVLooseFO(((*mvas)[pp]), probe->superCluster()->eta()));
    passMVAVLoose.push_back(PassMVAVLoose(((*mvas)[pp]), probe->superCluster()->eta()));
    passMVATight.push_back(PassMVATight(((*mvas)[pp]), probe->superCluster()->eta()));
    ++i;
  }

  // convert into ValueMap and store
  Store(iEvent, probes, sip3dValues, "sip3d");
  Store(iEvent, probes, passConvVetoValues, "passConvVeto");
  Store(iEvent, probes, passMVAVLooseFO, "passMVAVLooseFO");
  Store(iEvent, probes, passMVAVLoose, "passMVAVLoose");
  Store(iEvent, probes, passMVATight, "passMVATight");
}


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(MyElectronVariableHelper);
