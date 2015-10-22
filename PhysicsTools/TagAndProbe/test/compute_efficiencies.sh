#! /bin/bash

eval `scramv1 runtime -sh`
cd $CMSSW_BASE/src/ && scram b -j 15 -k
cd $CMSSW_BASE/src/PhysicsTools/TagAndProbe/test

cmsRun fitterAdam.py noData=True noIso=True &> mc_id.log &
cmsRun fitterAdam.py noMC=True noIso=True &> data_id.log &
cmsRun fitterAdam.py noData=True noID=True doEta=False &> mc_act.log &
cmsRun fitterAdam.py noMC=True noID=True doEta=False &> data_act.log &
cmsRun fitterAdam.py noData=True noID=True doEta=True &> mc_eta.log &
cmsRun fitterAdam.py noMC=True noID=True doEta=True &> data_eta.log &

wait
