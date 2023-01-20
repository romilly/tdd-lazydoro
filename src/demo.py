#!/usr/bin/env python3

from tdd_lazydoro.raspi.build import build
from tdd_lazydoro.raspi.printing_messenger import PrintingMessenger

"""
Run fast for demo purposes
"""



runner = build(ticks_per_minute=5, speed=5, messenger=PrintingMessenger())
runner.run()





