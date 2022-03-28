from typing import Tuple

from tdd_lazydoro.ui import UI
from blinkt import set_pixel, set_brightness, show, clear


class HardwareUI(UI):
    def clear_leds(self):
        set_brightness(0.1)
        clear()


    def set_led(self, number, rgb: Tuple[int]):
        set_brightness(0.1)
        set_pixel(number, *rgb)
        show()

