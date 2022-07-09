from time import sleep
from typing import Tuple

from tdd_lazydoro.display import Display
import blinkt

from gpiozero import TonalBuzzer
from gpiozero.tones import Tone


class LedAndBuzzerDisplay(Display):
    def __init__(self):
        blinkt.set_brightness(0.6)

    def clear_leds(self):
        blinkt.clear()
        blinkt.show()

    def set_led(self, number, rgb: Tuple[int, int, int]):
        blinkt.set_pixel(number, *rgb)
        blinkt.show()

    def buzz(self):
        buzzer = TonalBuzzer(6)
        buzzer.play(Tone('A4'))
        sleep(0.4)
        buzzer.stop()



