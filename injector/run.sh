#!/bin/bash
#
# Robert Alexander Limas Sierra
#

# ENVIRONMENT VARIABLES
DIR=`pwd`
GPGPUSIM_DIR=${DIR}/gpgpu-sim_distribution
UID=$1
APP_DIR=$2
APP_NAME=$3

# GO TO GPGPUSIM DIR
cd $GPGPUSIM_DIR
# ENABLE THE SIMULATOR IN DEGUB MODE
export CUDA_INSTALL_PATH=/usr/local/cuda
source setup_environment
# GO TO APP DIR
cd $APP_DIR
# CONFIGURE THE APP
ldd $APP_NAME
# EXECUTE APP ON GPGPU-SIM
./$APP_NAME $4 > $APP_DIR/out.txt
