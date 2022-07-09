#!/usr/bin/env python3

from tdd_lazydoro.raspi.build import build

"""
Run fast for demo purposes
"""
runner = build(ticks_per_minute=5, speed=5)
runner.run()





