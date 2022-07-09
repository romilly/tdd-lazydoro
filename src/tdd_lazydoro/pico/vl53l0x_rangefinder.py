from tdd_lazydoro.pico.pico_vl53l0x import VL53L0X
from tdd_lazydoro.rangefinder import RangeFinder

sda = Pin(0)
scl = Pin(1)
i2c = I2C(0,sda=sda, scl=scl)


class VL53L0XRangeFinder(RangeFinder):
    def __init__(self):
        self.vl53 = VL53L0X(i2c)

    def distance(self) -> int:
        tof_range = self.vl53.read()
        if tof_range == 0:  # sometimes get this when nothing is in range
            tof_range = 8191
        return tof_range
