# A script that checks all the bits of lazydoro are plugged in and working

from machine import Pin, I2C
import time

from pico.mp import ABC, abstractmethod

from pico.neo import NeoPixel
from pico.pico_vl53l0x import VL53L0X
from pico.colors import GREEN, YELLOW, RED, BLUE


class RangeFinder(ABC):
    @abstractmethod
    def distance(self) -> int:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass


class PicoRangeFinder(RangeFinder):
    def __init__(self):
        i2c = I2C(0, sda=(Pin(0)), scl=(Pin(1)))
        self.tof = VL53L0X(i2c)
        self.tof.start()

    def distance(self):
        tof_range = self.tof.read()
        if tof_range == 0:  # sometimes we get this when nothing is in range
            tof_range = 8191
        # scaled_distance is between 0 and 8
        return min(8, int(tof_range / 50))

    def stop(self):
        self.tof.stop()

class DisplayAdapter(ABC):
    @abstractmethod
    def show(self, scaled_distance: int) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass


class PicoDisplayAdapter(DisplayAdapter):
    colors = [RED, RED, YELLOW, YELLOW, BLUE, BLUE, GREEN, GREEN, GREEN]

    def __init__(self):
        self.np = NeoPixel()
        self.buzzer = Pin(17, Pin.OUT)

    def show(self, scaled_distance: int):
        self.np.clear()
        for i in range(scaled_distance):
            self.np.set(i, self.colors[i])
        self.np.show()
        if scaled_distance < 2:
            self.buzzer.value(1)
            time.sleep(0.1)
            self.buzzer.value(0)

    def stop(self):
        self.buzzer.value(0)
        self.np.clear()
        self.np.show()


class Skeleton:
    def __init__(self, rangefinder: RangeFinder, display_adapter: DisplayAdapter):
        self.rangefinder = rangefinder
        self.display_adapter = display_adapter

    def run(self):
        while True:
            try:
                distance = self.rangefinder.distance()
                self.display_adapter.show(distance)
                time.sleep(1)
            finally:
                self.rangefinder.stop()
                self.display_adapter.stop()


skeleton = Skeleton(rangefinder=PicoRangeFinder(),
                    display_adapter= PicoDisplayAdapter())
skeleton.run()

