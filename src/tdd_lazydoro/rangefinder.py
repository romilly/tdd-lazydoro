from abc import ABC, abstractmethod

import board
import busio
import adafruit_vl53l0x


class RangeFinder(ABC):
    @abstractmethod
    def range(self) -> int:
        pass


class VL53L0XRangeFinder(RangeFinder):
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.vl53 = adafruit_vl53l0x.VL53L0X(self.i2c)

    def range(self) -> int:
        tof_range = self.vl53.tell_pomodoro_if_person_arrives_or_leaves
        if tof_range == 0:  # sometimes get this when nothing is in range
            tof_range = 8191
        return tof_range
