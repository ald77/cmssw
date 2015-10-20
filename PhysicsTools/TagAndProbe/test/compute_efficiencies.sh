#! /bin/bash

cmsRun fitterAdam.py noData=True  &
cmsRun fitterAdam.py noMC=True    &
cmsRun fitterAdam.py noData=True noID=True doEta=True  &
cmsRun fitterAdam.py noMC=True   noID=True doEta=True  &

wait
