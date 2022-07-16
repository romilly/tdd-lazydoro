#!/usr/bin/env bash

# copy the walking skeleton code to the pico
# using mpremote

cd ..
DIST_DIR='pico-dist'
SRC_DIR='src'
PICO_PKG_DIR='tdd-lazydoro/pico'
TARGET_DIR=$DIST_DIR/$PICO_PKG_DIR

# clear the pico-dist directory
mkdir -p $DIST_DIR
rm -rf $DIST_DIR/*

# copy required files to pico-dist

cp $SRC_DIR/pico_walking_skeleton.py $DIST_DIR
mkdir -p $TARGET_DIR
cd $SRC_DIR/$PICO_PKG_DIR
cp neo.py $TARGET_DIR
cp pico_display.py $TARGET_DIR
cp pico_vl53l0x.py $TARGET_DIR
cp pico_rangefinder.py $TARGET_DIR

## copy files to Pico board

cd DIST_DIR
mpremote cp -r . :




