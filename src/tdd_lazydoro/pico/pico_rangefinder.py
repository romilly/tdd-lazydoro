import time
from machine import Pin, I2C
from tdd_lazydoro.pico.pico_vl53l0x import VL53L0X

sda = Pin(0)
scl = Pin(1)
i2c = I2C(0,sda=sda, scl=scl)


class PicoRangefinder:
    def __init__(self):
        self.tof = VL53L0X(i2c)
        self.tof.start()

    def distance(self):
        tof_range = self.tof.read()
        if tof_range == 0:  # sometimes get this when nothing is in range
            tof_range = 8191
        return tof_range

    def stop(self):
        self.tof.stop()


