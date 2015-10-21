#! /bin/bash

eval `scramv1 runtime -sh`
cd $CMSSW_BASE/src/ && scram b -j 15 -k && cd $CMSSW_BASE/src/PhysicsTools/TagAndProbe/test && cmsRun makeTree.py
cd $CMSSW_BASE/src/PhysicsTools/TagAndProbe/test
