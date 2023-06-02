#!/bin/bash

set -m

/iris-main "$@" &

/usr/irissys/dev/Cloud/ICM/waitISC.sh

# set default production
iop -d dc.Python.Production

# start production
iop grongier.pex -s &

fg %1