#include "PhysicsTools/SelectorUtils/interface/CutApplicatorWithEventContentBase.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "RecoEgamma/EgammaTools/interface/EffectiveAreas.h"


class GsfEleEffAreaMiniIsoCut : public CutApplicatorWithEventContentBase {
public:
  GsfEleEffAreaMiniIsoCut(const edm::ParameterSet& c);
  
  result_type operator()(const reco::GsfElectronPtr&) const override final;

  void setConsumes(edm::ConsumesCollector&) override final;
  void getEventContent(const edm::EventBase&) override final;

  double value(const reco::CandidatePtr& cand) const override final;

  CandidateType candidateType() const override final { 
    return ELECTRON; 
  }

private:
  // Cut values
  const float _isoCutEBLowPt,_isoCutEBHighPt,_isoCutEELowPt,_isoCutEEHighPt;
  // Configuration
  const float _ptCutOff;
  const float _barrelCutOff;
  bool  _isRelativeIso;
  // Effective area constants
  EffectiveAreas _effectiveAreas;
  // The rho
  edm::Handle< double > _rhoHandle;

  constexpr static char rhoString_     [] = "rho";

  // Isolation
  edm::Handle<edm::ValueMap<float> > _chadIsoHandle;
  edm::Handle<edm::ValueMap<float> > _nhadIsoHandle;
  edm::Handle<edm::ValueMap<float> > _phoIsoHandle;

  constexpr static char chadString_[] = "chadIso";
  constexpr static char nhadString_[] = "nhadIso";
  constexpr static char phoString_[] = "phoIso";
};

constexpr char GsfEleEffAreaMiniIsoCut::rhoString_[];
constexpr char GsfEleEffAreaMiniIsoCut::chadString_[];
constexpr char GsfEleEffAreaMiniIsoCut::nhadString_[];
constexpr char GsfEleEffAreaMiniIsoCut::phoString_[];

DEFINE_EDM_PLUGIN(CutApplicatorFactory,
		  GsfEleEffAreaMiniIsoCut,
		  "GsfEleEffAreaMiniIsoCut");

GsfEleEffAreaMiniIsoCut::GsfEleEffAreaMiniIsoCut(const edm::ParameterSet& c) :
  CutApplicatorWithEventContentBase(c),
  _isoCutEBLowPt(c.getParameter<double>("isoCutEBLowPt")),
  _isoCutEBHighPt(c.getParameter<double>("isoCutEBHighPt")),
  _isoCutEELowPt(c.getParameter<double>("isoCutEELowPt")),
  _isoCutEEHighPt(c.getParameter<double>("isoCutEEHighPt")),
  _ptCutOff(c.getParameter<double>("ptCutOff")),
  _barrelCutOff(c.getParameter<double>("barrelCutOff")),
  _isRelativeIso(c.getParameter<bool>("isRelativeIso")),
  _effectiveAreas( (c.getParameter<edm::FileInPath>("effAreasConfigFile")).fullPath())
{
  
  edm::InputTag rhoTag = c.getParameter<edm::InputTag>("rho");
  edm::InputTag chadTag = c.getParameter<edm::InputTag>("chadIso");
  edm::InputTag nhadTag = c.getParameter<edm::InputTag>("nhadIso");
  edm::InputTag phoTag = c.getParameter<edm::InputTag>("phoIso");

  contentTags_.emplace(rhoString_,rhoTag);
  contentTags_.emplace(chadString_,chadTag);
  contentTags_.emplace(nhadString_,nhadTag);
  contentTags_.emplace(phoString_,phoTag);
}

void GsfEleEffAreaMiniIsoCut::setConsumes(edm::ConsumesCollector& cc) {
  auto rho = cc.consumes<double>(contentTags_[rhoString_]);
  auto chadIso = cc.consumes<edm::ValueMap<float> >(contentTags_[chadString_]);
  auto nhadIso = cc.consumes<edm::ValueMap<float> >(contentTags_[nhadString_]);
  auto phoIso = cc.consumes<edm::ValueMap<float> >(contentTags_[phoString_]);
  contentTokens_.emplace(rhoString_, rho);
  contentTokens_.emplace(chadString_, chadIso);
  contentTokens_.emplace(nhadString_, nhadIso);
  contentTokens_.emplace(phoString_, phoIso);
}

void GsfEleEffAreaMiniIsoCut::getEventContent(const edm::EventBase& ev) {  
  ev.getByLabel(contentTags_[rhoString_],_rhoHandle);
  ev.getByLabel(contentTags_[chadString_],_chadIsoHandle);
  ev.getByLabel(contentTags_[nhadString_],_nhadIsoHandle);
  ev.getByLabel(contentTags_[phoString_],_phoIsoHandle);
}

CutApplicatorBase::result_type 
GsfEleEffAreaMiniIsoCut::
operator()(const reco::GsfElectronPtr& cand) const{  

  // Establish the cut value
  double absEta = std::abs(cand->superCluster()->position().eta());
  const float isoCut =
    ( cand->p4().pt() < _ptCutOff ?
      ( absEta < _barrelCutOff ? _isoCutEBLowPt : _isoCutEELowPt ) 
      :
      ( absEta < _barrelCutOff ? _isoCutEBHighPt : _isoCutEEHighPt ) );

  // Compute the combined isolation with effective area correction
  float  eA = _effectiveAreas.getEffectiveArea( absEta );
  float rho = static_cast<float>(*_rhoHandle); // std::max likes float arguments
  edm::ValueMap<float> chadMap = static_cast<edm::ValueMap<float> >(*_chadIsoHandle);
  edm::ValueMap<float> nhadMap = static_cast<edm::ValueMap<float> >(*_nhadIsoHandle);
  edm::ValueMap<float> phoMap = static_cast<edm::ValueMap<float> >(*_phoIsoHandle);
  float chad = chadMap[cand];
  float nhad = nhadMap[cand];
  float pho = phoMap[cand];

  float iso = chad + std::max(0.0f, nhad + pho - rho*eA);
  
  // Divide by pT if the relative isolation is requested
  if( _isRelativeIso )
    iso /= cand->pt();

  // Apply the cut and return the result
  return iso < isoCut;
}

double GsfEleEffAreaMiniIsoCut::value(const reco::CandidatePtr& cand) const {
  reco::GsfElectronPtr ele(cand);
  // Establish the cut value
  double absEta = std::abs(ele->superCluster()->position().eta());

  // Compute the combined isolation with effective area correction
  float  eA = _effectiveAreas.getEffectiveArea( absEta );
  float rho = static_cast<float>(*_rhoHandle); // std::max likes float arguments
  edm::ValueMap<float> chadMap = static_cast<edm::ValueMap<float> >(*_chadIsoHandle);
  edm::ValueMap<float> nhadMap = static_cast<edm::ValueMap<float> >(*_nhadIsoHandle);
  edm::ValueMap<float> phoMap = static_cast<edm::ValueMap<float> >(*_phoIsoHandle);
  float chad = chadMap[ele];
  float nhad = nhadMap[ele];
  float pho = phoMap[ele];

  float iso = chad + std::max(0.0f, nhad + pho - rho*eA);
  
  // Divide by pT if the relative isolation is requested
  if( _isRelativeIso )
    iso /= ele->pt();

  // Apply the cut and return the result
  return iso;
}
