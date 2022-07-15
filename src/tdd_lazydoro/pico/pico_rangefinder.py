import time
from machine import Pin, I2C
from tdd_lazydoro.pico.pico_vl53l0x import VL53L0X
from tdd_lazydoro.rangefinder import RangeFinder

sda = Pin(0)
scl = Pin(1)
i2c = I2C(0,sda=sda, scl=scl)

# Create a VL53L0X object
tof = VL53L0X(i2c)


class PicoRangefinder(RangeFinder):
    def distance(self):
        tof.start()
        tof.read()
        tof_range = tof.read()
        tof.stop()
        if tof_range == 0:  # sometimes get this when nothing is in range
            tof_range = 8191
        return tof_range


if __name__ == '__main__':
    p = PicoRangefinder()
    while True:
        try:
            print(p.distance())
        finally:
            tof.stop()
