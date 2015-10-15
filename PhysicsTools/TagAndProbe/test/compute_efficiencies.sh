#! /bin/bash

cmsRun fitterAdam.py noData=True &> /dev/null &
cmsRun fitterAdam.py noMC=True   &> /dev/null &
cmsRun fitterAdam.py noData=True noID=True doEta=True &> /dev/null &
cmsRun fitterAdam.py noMC=True   noID=True doEta=True &> /dev/null &

wait
