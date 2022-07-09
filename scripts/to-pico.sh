#!/usr/bin/env bash

# copy the lazydoro code from the `scr` directory to the pico
# using mpremote

mpremote cp pico_runner.py :main.py
mpremote mkdir tdd_lazydoro
cd tdd_lazydoro/
mpremote cp *.py :tdd_lazydoro/
cd pico/
mpremote mkdir tdd_lazydoro/pico
mpremote cp *.py :tdd_lazydoro/pico/
