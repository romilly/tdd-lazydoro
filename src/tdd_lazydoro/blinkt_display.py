from time import sleep
from typing import Tuple

from tdd_lazydoro.display import Display
from blinkt import set_pixel, set_brightness, show, clear

from gpiozero import TonalBuzzer
from gpiozero.tones import Tone


class BlinktDisplay(Display):
    def __init__(self):
        set_brightness(0.6)

    def clear_leds(self):
        clear()
        show()

    def set_led(self, number, rgb: Tuple[int]):
        print('setting led %d %s' % (number, rgb))
        set_pixel(number, *rgb)
        show()

    def buzz(self):
        b = TonalBuzzer(6)
        b.play(Tone('A4'))
        sleep(0.4)
        b.stop()



