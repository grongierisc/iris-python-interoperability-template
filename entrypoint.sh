#!/bin/bash

set -m

/iris-main "$@" &

/usr/irissys/dev/Cloud/ICM/waitISC.sh

# set default production
iop --default dc.Python.Production

# start production
iop --start &

fg %1