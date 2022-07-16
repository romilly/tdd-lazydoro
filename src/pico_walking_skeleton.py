# A script that checks all the bits of lazydoro are plugged in and working

from machine import Pin
import time

from tdd_lazydoro.pico.neo import NeoPixel
from tdd_lazydoro.pico.pico_rangefinder import PicoRangefinder
from tdd_lazydoro.colors import GREEN, YELLOW, RED, BLUE
rangefinder = PicoRangefinder()


class PicoDisplayAdapter:
    colors = [RED, RED, YELLOW, YELLOW, BLUE, BLUE, GREEN, GREEN, GREEN]

    def __init__(self):
        self.np = NeoPixel()
        self.buzzer = Pin(17, Pin.OUT)

    def show(self, scaled: int):
        self.np.clear()
        for i in range(scaled):
            self.np.set(i, self.colors[i])
        self.np.show()
        if scaled < 2:
            self.buzzer.value(1)
            time.sleep(0.1)
            self.buzzer.value(0)

    def stop(self):
        self.np.clear()
        self.np.show()
        self.buzzer.value(0)


class Skeleton():
    def __init__(self):
        self.display_adapter = PicoDisplayAdapter()

    def run(self):
        while True:
            try:
                distance = rangefinder.distance()
                scaled_distance = min(8,int(distance/50)) # scaled_distance is between 0 and 8
                print(scaled_distance)
                for i in range(scaled_distance):
                    self.display_adapter.show(scaled_distance)
                    time.sleep(0.1)
            finally:
                self.display_adapter.stop()


Skeleton().run()
