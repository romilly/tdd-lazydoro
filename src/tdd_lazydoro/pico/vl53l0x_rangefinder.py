import board
import busio

from tdd_lazydoro.pico.pico_vl53l0x import VL53L0X
from tdd_lazydoro.rangefinder import RangeFinder


class VL53L0XRangeFinder(RangeFinder):
    def __init__(self):
        self.vl53 = VL53L0X()

    def distance(self) -> int:
        tof_range = self.vl53.read()
        if tof_range == 0:  # sometimes get this when nothing is in range
            tof_range = 8191
        return tof_range
