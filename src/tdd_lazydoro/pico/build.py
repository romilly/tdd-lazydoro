from tdd_lazydoro.clockwatcher import ClockWatcher
from tdd_lazydoro.display_adapter import DisplayAdapter
from tdd_lazydoro.pico.pico_display import PicoDisplay
from tdd_lazydoro.pico.vl53l0x_rangefinder import VL53L0XRangeFinder
from tdd_lazydoro.pomodoro import Pomodoro


def build(ticks_per_minute=60,
          speed=1,
          duration=25,
          break_time=5): # pragma: no cover

    display = PicoDisplay()

    rangefinder =   VL53L0XRangeFinder()
    pomodoro = Pomodoro(DisplayAdapter(display),
                        ticks_per_minute=ticks_per_minute,
                        duration=duration,
                        break_time=break_time)
    return ClockWatcher(rangefinder, pomodoro, speed=speed)