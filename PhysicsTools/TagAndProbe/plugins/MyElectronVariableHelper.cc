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
}

class MyElectronVariableHelper : public edm::EDProducer {
public:
  explicit MyElectronVariableHelper(const edm::ParameterSet & iConfig);
  virtual ~MyElectronVariableHelper() ;
  
  virtual void produce(edm::Event & iEvent, const edm::EventSetup & iSetup) override;
  
private:
  edm::EDGetTokenT<std::vector<pat::Electron> > probesToken_;
};

MyElectronVariableHelper::MyElectronVariableHelper(const edm::ParameterSet & iConfig) :
  probesToken_(consumes<std::vector<pat::Electron> >(iConfig.getParameter<edm::InputTag>("probes"))){
  produces<edm::ValueMap<float> >("sip3d");
  produces<edm::ValueMap<bool> >("passConvVeto");
}

MyElectronVariableHelper::~MyElectronVariableHelper(){
}

void MyElectronVariableHelper::produce(edm::Event & iEvent, const edm::EventSetup & iSetup) {
  // read input
  edm::Handle<std::vector<pat::Electron> > probes;
  iEvent.getByToken(probesToken_,  probes);

  // prepare vector for output
  std::vector<float> sip3dValues;
  std::vector<bool> passConvVetoValues;

  for(auto probe = probes->cbegin(); probe != probes->cend(); ++probe){
    sip3dValues.push_back(probe->dB(pat::Electron::PV3D)/probe->edB(pat::Electron::PV3D));
    passConvVetoValues.push_back(probe->passConversionVeto());
  }

  // convert into ValueMap and store
  Store(iEvent, probes, sip3dValues, "sip3d");
  Store(iEvent, probes, passConvVetoValues, "passConvVeto");
}


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(MyElectronVariableHelper);
