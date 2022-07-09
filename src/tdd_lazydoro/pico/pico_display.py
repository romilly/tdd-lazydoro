from tdd_lazydoro.display import Display
from tdd_lazydoro.pico.neo import NeoPixel
from machine import Pin
import time


class PicoDisplay(Display):
    def __init__(self):
        self.np = NeoPixel()
        self.buzzer = Pin(15, Pin.OUT)

    def clear_leds(self):
        self.np.clear()

    def set_led(self, number, rgb):
        self.np.set(number, rgb)

    def buzz(self):
        self.buzzer.value(1)
        time.sleep(2)
        self.buzzer.value(0)