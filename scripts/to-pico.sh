#!/usr/bin/env bash

# copy the lazydoro code from the `scr` directory to the pico
# using mpremote

cd ../src
#mpremote cp pico_runner.py :main.py
cp pico_walking_skeleton.py :pico_walking_skeleton.py
mpremote mkdir tdd_lazydoro
cd tdd_lazydoro/
mpremote cp *.py :tdd_lazydoro/
cd pico/
mpremote mkdir tdd_lazydoro/pico
mpremote cp *.py :tdd_lazydoro/pico/
