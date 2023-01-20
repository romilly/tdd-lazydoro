#!/usr/bin/env python3

from tdd_lazydoro.raspi.build import build
from tdd_lazydoro.raspi.printing_messenger import PrintingMessenger

runner = build(messenger=PrintingMessenger())
runner.run()





