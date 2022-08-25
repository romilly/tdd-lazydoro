from typing import Optional

from tdd_lazydoro.display_adapter import DisplayAdapter
from tdd_lazydoro.clockwatcher import ClockWatcher
from tdd_lazydoro.display import Display
from tdd_lazydoro.pomodoro import Pomodoro
from tdd_lazydoro.rangefinder import RangeFinder


def build(display: Optional[Display] = None,
          messenger = None,
          hostname: str = 'localhost',
          rangefinder: Optional[RangeFinder] = None,
          ticks_per_minute: int = 60,
          speed: int = 1,
          duration: int = 25,
          break_time: int = 5): # pragma: no cover
    if display is None: # pragma: no cover
        from tdd_lazydoro.raspi.led_display import LedAndBuzzerDisplay
        display = LedAndBuzzerDisplay()
    if rangefinder is None: # pragma: no cover
        from tdd_lazydoro.raspi.vl53l0x_rangefinder import VL53L0XRangeFinder
        rangefinder =   VL53L0XRangeFinder()
    if messenger is None:
        from tdd_lazydoro.raspi.mqtt import MQTTMessenger
        messenger = MQTTMessenger(hostname)
    pomodoro = Pomodoro(DisplayAdapter(display, messenger), ticks_per_minute=ticks_per_minute, duration=duration,
                        break_time=break_time)
    return ClockWatcher(rangefinder, pomodoro, speed=speed)