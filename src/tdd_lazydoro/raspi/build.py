from typing import Optional

from tdd_lazydoro.display_adapter import DisplayAdapter
from tdd_lazydoro.clockwatcher import ClockWatcher
from tdd_lazydoro.display import Display
from tdd_lazydoro.pomodoro import Pomodoro
from tdd_lazydoro.rangefinder import RangeFinder


class MQTTMessenger:
    def __init__(self, hostname):
        pass

    def send(self, message):
        pass


def build(display: Optional[Display] = None,
          messenger = None,
          hostname = None,
          rangefinder: Optional[RangeFinder]= None,
          ticks_per_minute=60,
          speed=1,
          duration=25,
          break_time=5): # pragma: no cover
    if display is None: # pragma: no cover
        from tdd_lazydoro.raspi.led_display import LedAndBuzzerDisplay
        display = LedAndBuzzerDisplay()
    if rangefinder is None: # pragma: no cover
        from tdd_lazydoro.raspi.vl53l0x_rangefinder import VL53L0XRangeFinder
        rangefinder =   VL53L0XRangeFinder()
    if messenger is None:
        messenger = MQTTMessenger(hostname)
    pomodoro = Pomodoro(DisplayAdapter(display, messenger), ticks_per_minute=ticks_per_minute, duration=duration,
                        break_time=break_time)
    return ClockWatcher(rangefinder, pomodoro, speed=speed)