#!/usr/bin/env bash

# copy the walking skeleton code to the pico
# using mpremote

cd ..
DIST_DIR='dist-pico'
SRC_DIR='src'
PICO_PKG_DIR='tdd_lazydoro/pico'
PICO_SRC_DIR=$SRC_DIR/$PICO_PKG_DIR
TARGET_DIR=$DIST_DIR/$PICO_PKG_DIR


# ensure the dist-pico directory exists
if [[ ! -e $DIST_DIR ]]; then
    mkdir $DIST_DIR
fi

# clear the dist-pico directory
rm -rf $DIST_DIR/*

# copy required files to dist-pico directory

cp $SRC_DIR/pico_walking_skeleton.py $DIST_DIR/
mkdir -p $TARGET_DIR

cp $PICO_SRC_DIR/neo.py $TARGET_DIR/
cp $PICO_SRC_DIR/pico_display.py $TARGET_DIR/
cp $PICO_SRC_DIR/pico_vl53l0x.py $TARGET_DIR/
cp $PICO_SRC_DIR/pico_rangefinder.py $TARGET_DIR/
cp $PICO_SRC_DIR/colors.py $TARGET_DIR/

## copy files to Pico board

cd $DIST_DIR
mpremote cp -r . :




