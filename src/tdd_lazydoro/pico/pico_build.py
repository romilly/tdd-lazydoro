from typing import Optional

from tdd_lazydoro.blinkt_adapter import BlinktAdapter
from tdd_lazydoro.clockwatcher import ClockWatcher
from tdd_lazydoro.display import Display
from tdd_lazydoro.pomodoro import Pomodoro
from tdd_lazydoro.rangefinder import RangeFinder


def build(display: Optional[Display] = None,
          rangefinder: Optional[RangeFinder]= None,
          ticks_per_minute=60,
          speed=1,
          duration=25,
          break_time=5): # pragma: no cover
    if display is None: # pragma: no cover
        from tdd_lazydoro.led_display import LedAndBuzzerDisplay
        display = LedAndBuzzerDisplay()
    else: # pragma: no cover
        display = display
    if rangefinder is None: # pragma: no cover
        from tdd_lazydoro.vl53l0x_rangefinder import VL53L0XRangeFinder
        rangefinder =   VL53L0XRangeFinder()
    else:# pragma: no cover
        rangefinder = rangefinder
    pomodoro = Pomodoro(BlinktAdapter(display), ticks_per_minute=ticks_per_minute, duration=duration, break_time=break_time)
    return ClockWatcher(rangefinder, pomodoro, speed=speed)