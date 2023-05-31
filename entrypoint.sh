#!/bin/bash

set -m

/iris-main "$@" &

/usr/irissys/dev/Cloud/ICM/waitISC.sh

# set default production
/usr/irissys/bin/irispython -m grongier.pex -d dc.Python.Production

# start production
/usr/irissys/bin/irispython -m grongier.pex -s &

fg %1