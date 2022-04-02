from typing import Optional

from tdd_lazydoro.blinkt_adapter import BlinktAdapter
from tdd_lazydoro.blinkt_display import BlinktDisplay
from tdd_lazydoro.clockwatcher import ClockWatcher
from tdd_lazydoro.display import Display
from tdd_lazydoro.pomodoro import Pomodoro
from tdd_lazydoro.rangefinder import VL53L0XRangeFinder, RangeFinder


def build(display: Optional[Display] = None,
          rangefinder: Optional[RangeFinder]= None,
          seconds=60,
          speed=1,
          duration=25,
          break_time=5):
    display = display if display else BlinktDisplay()
    rangefinder = rangefinder if rangefinder else VL53L0XRangeFinder()
    pomodoro = Pomodoro(BlinktAdapter(display), seconds=seconds, duration=duration, break_time=break_time)
    return ClockWatcher(rangefinder, pomodoro, speed=speed)