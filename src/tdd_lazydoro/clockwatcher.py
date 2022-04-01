import board
import busio
import adafruit_vl53l0x
from time import sleep

from tdd_lazydoro.alarm import Alarm
from tdd_lazydoro.blinkt_adapter import BlinktAdapter
from tdd_lazydoro.blinkt_display import BlinktDisplay
from tdd_lazydoro.glitch_filter import GlitchFilter
from tdd_lazydoro.pomodoro import Pomodoro

i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)


class ClockWatcher:
    def __init__(self, pomodoro: Pomodoro, range_threshold=500):
        self.pomodoro = pomodoro
        self.range_threshold = range_threshold
        self.person_was_present = False
        self.glitch_filter = GlitchFilter(5)
        self.snooze_time = 1

    def run(self, speed=1): # change this for a speeded-up demo
        if speed == 1:
            self.snooze_time = 1
        else:
            self.snooze_time = 1 / speed
        while True:
            self.pomodoro.tick()
            self.range(vl53.range)
            sleep(self.snooze_time)

    def range(self, tof_range: int):
        person_present = self.glitch_filter.filter(self.is_person_in_range(tof_range))
        if person_present and not self.person_was_present:
            self.pomodoro.person_arrives()
        if self.person_was_present and not person_present:
            self.pomodoro.person_leaves()
        self.person_was_present = person_present

    def is_person_in_range(self, tof_range):
        if tof_range == 0:  # sometimes get this when nothing is in range
            tof_range = 8191
        return tof_range < self.range_threshold




