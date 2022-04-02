from typing import Optional

from tdd_lazydoro.blinkt_adapter import BlinktAdapter
from tdd_lazydoro.clockwatcher import ClockWatcher
from tdd_lazydoro.display import Display
from tdd_lazydoro.pomodoro import Pomodoro
from tdd_lazydoro.rangefinder import RangeFinder


def build(display: Optional[Display] = None,
          rangefinder: Optional[RangeFinder]= None,
          seconds=60,
          speed=1,
          duration=25,
          break_time=5):
    if display is None:
        from tdd_lazydoro.blinkt_display import BlinktDisplay
        display = BlinktDisplay()
    else:
        display = display
    if rangefinder is None:
        from tdd_lazydoro.vl53l0x_rangefinder import VL53L0XRangeFinder
        rangefinder =   VL53L0XRangeFinder()
    else:
        rangefinder = rangefinder
    pomodoro = Pomodoro(BlinktAdapter(display), seconds=seconds, duration=duration, break_time=break_time)
    return ClockWatcher(rangefinder, pomodoro, speed=speed)