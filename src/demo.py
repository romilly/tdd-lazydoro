#!/usr/bin/env python3

from tdd_lazydoro.raspi.build import build

"""
Run fast for demo purposes
"""


class PrintingMessenger:
    def send(self, message):
        print(message)


runner = build(ticks_per_minute=5, speed=5, messenger=PrintingMessenger())
runner.run()





