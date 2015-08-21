#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/Common/interface/View.h"

#include "PhysicsTools/SelectorUtils/interface/CutApplicatorWithEventContentBase.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "RecoEgamma/EgammaTools/interface/EffectiveAreas.h"

typedef std::vector<pat::Electron> ElectronCollection;
typedef edm::Ref<ElectronCollection> ElectronRef;
typedef edm::RefVector<ElectronCollection> ElectronRefVector;

class ActivityProducer : public edm::EDProducer{
public:
  explicit ActivityProducer(const edm::ParameterSet &pset);
  ~ActivityProducer();

private:
  virtual void produce(edm::Event &event, const edm::EventSetup &setup) override;

  EffectiveAreas effectiveAreas_;
  edm::EDGetTokenT<ElectronRefVector > probesToken_;
  edm::EDGetTokenT<ElectronCollection> collToken_;
  edm::EDGetTokenT<double> rhoToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > chadToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > nhadToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > phoToken_;
  bool isRelativeIso_;
};

ActivityProducer::ActivityProducer(const edm::ParameterSet &pset):
  effectiveAreas_((pset.getParameter<edm::FileInPath>("effAreasConfigFile")).fullPath()),
  probesToken_(consumes<ElectronRefVector>(pset.getParameter<edm::InputTag>("probes"))),
  collToken_(consumes<ElectronCollection>(pset.getParameter<edm::InputTag>("probes"))),
  rhoToken_(consumes<double>(pset.getParameter<edm::InputTag>("rho"))),
  chadToken_(consumes<edm::ValueMap<float> >(pset.getParameter<edm::InputTag>("chadIso"))),
  nhadToken_(consumes<edm::ValueMap<float> >(pset.getParameter<edm::InputTag>("nhadIso"))),
  phoToken_(consumes<edm::ValueMap<float> >(pset.getParameter<edm::InputTag>("phoIso"))),
  isRelativeIso_(pset.getParameter<bool>("isRelativeIso")){
  produces<edm::ValueMap<float> >("activity");
}

ActivityProducer::~ActivityProducer(){
}

void ActivityProducer::produce(edm::Event &event, const edm::EventSetup &setup){
  edm::Handle<double> rhoHandle;
  edm::Handle<edm::ValueMap<float> > chadHandle, nhadHandle, phoHandle;
  edm::Handle<ElectronRefVector> probesHandle;
  edm::Handle<ElectronCollection> collHandle;

  event.getByToken(probesToken_, probesHandle);
  event.getByToken(collToken_, collHandle);
  event.getByToken(rhoToken_, rhoHandle);
  event.getByToken(chadToken_, chadHandle);
  event.getByToken(nhadToken_, nhadHandle);
  event.getByToken(phoToken_, phoHandle);
  
  auto rho = static_cast<float>(*rhoHandle);
  const auto &chadMap = static_cast<edm::ValueMap<float> >(*chadHandle);
  const auto &nhadMap = static_cast<edm::ValueMap<float> >(*nhadHandle);
  const auto &phoMap = static_cast<edm::ValueMap<float> >(*phoHandle);
  const auto &probes = static_cast<ElectronRefVector>(*probesHandle);

  std::vector<float> isos(probes.size());

  for(size_t iprobe = 0; iprobe < probes.size(); ++iprobe){
    ElectronRef er = probes[iprobe];
    double absEta = er->superCluster()->position().eta();
    double effectiveArea = effectiveAreas_.getEffectiveArea(absEta);
    double chad = chadMap[er];
    double nhad = nhadMap[er];
    double pho = phoMap[er];

    isos.at(iprobe) = chad + std::max(0., nhad+pho-rho*effectiveArea);
    if(isRelativeIso_) isos.at(iprobe) /= er->pt();
  }

  std::auto_ptr<edm::ValueMap<float> > isosValMap(new edm::ValueMap<float>());
  edm::ValueMap<float>::Filler isosFiller(*isosValMap);
  isosFiller.insert(collHandle, isos.begin(), isos.end());
  isosFiller.fill();
  event.put(isosValMap, "activity");
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(ActivityProducer);
