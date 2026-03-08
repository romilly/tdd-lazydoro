#!/usr/bin/env python3

from tdd_lazydoro.raspi.build import build
from tdd_lazydoro.raspi.mqtt import MQTTMessenger

runner = build(messenger=MQTTMessenger('edgy-hermes'))
runner.run()





