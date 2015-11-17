#ifndef JetConverter_h
#define JetConverter_h

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/PatCandidates/interface/Jet.h"

class JetConverter : public edm::EDProducer{
public:
  explicit JetConverter(const edm::ParameterSet & iConfig);
  virtual ~JetConverter();

  virtual void produce(edm::Event &event, const edm::EventSetup &setup) override;
  
private:
  edm::EDGetTokenT<std::vector<pat::Jet> > jetsToken_;
};


#endif

JetConverter::JetConverter(const edm::ParameterSet &config):
  jetsToken_(consumes<std::vector<pat::Jet> >(config.getParameter<edm::InputTag>("jets"))){
  produces<std::vector<reco::PFJet> >();
}

JetConverter::~JetConverter(){
}

void JetConverter::produce(edm::Event &event, const edm::EventSetup &setup){
  edm::Handle<std::vector<pat::Jet> > jets_in;
  event.getByToken(jetsToken_, jets_in);

  std::vector<reco::PFJet> *jets_out = new std::vector<reco::PFJet>();
  jets_out->resize(jets_in->size());
  for(size_t i = 0; i < jets_in->size(); ++i){
    const pat::Jet &jet_in = jets_in->at(i);
    jets_out->at(i) = reco::PFJet(jet_in.p4()*jet_in.jecFactor("Uncorrected"),
                                  jet_in.vertex(),
                                  jet_in.pfSpecific(),
                                  jet_in.getJetConstituents());
    jets_out->at(i).setJetArea(jet_in.jetArea());
  }

  std::auto_ptr<std::vector<reco::PFJet> > output(jets_out);
  event.put(output);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(JetConverter);
