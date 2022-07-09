import time
from machine import Pin
from machine import I2C
import pico_vl53l0x
from tdd_lazydoro.rangefinder import RangeFinder

sda = machine.Pin(0)
scl = machine.Pin(1)
i2c = machine.I2C(0,sda=sda, scl=scl)

# Create a VL53L0X object
tof = pico_vl53l0x.VL53L0X(i2c)

tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 18)

tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 14)


class PicoRangefinder(RangeFinder):
    def distance(self):
    # Start ranging
        tof.start()
        tof.read()
        result = tof.read()
        tof.stop()
        return result
