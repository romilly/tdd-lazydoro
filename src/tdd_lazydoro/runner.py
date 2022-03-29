import board
import busio
import adafruit_vl53l0x
from time import sleep

from tdd_lazydoro.blinkt_display import BlinktDisplay
from tdd_lazydoro.pomodoro import Pomodoro


class Alarm:
    def __init__(self, pomodoro: Pomodoro):
        self.pomodoro = pomodoro
        self.ticks = 0

    def tick(self):
        self.ticks += 1
        if self.ticks >= 60:
            self.pomodoro.minute_has_passed()
            self.reset()

    def reset(self):
        self.ticks = 0


class PersonWatcher:
    def __init__(self, pomodoro: Pomodoro, alarm: Alarm, range_threshold=500):
        self.pomodoro = pomodoro
        self.alarm = alarm
        self.range_threshold = range_threshold
        self.person_was_present = False

    def range(self, tof_range: int):
        person_present = tof_range >= self.range_threshold
        if person_present != self.person_was_present:
            self.alarm.reset()
        if person_present and not self.person_was_present:
            self.person_was_present = True
            self.pomodoro.person_arrives()
        if self.person_was_present and not person_present:
            self.person_was_present = False
            self.pomodoro.person_leaves()


class Runner:
    def __init__(self, alarm: Alarm, watcher: PersonWatcher):
        self.alarm = alarm
        self.watcher = watcher
        self.snooze_time = 1
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.vl53 = adafruit_vl53l0x.VL53L0X(self.i2c)

    def run(self, speed=1):
        if speed == 1:
            self.snooze_time = 1
        else:
            self.snooze_time = 1 / speed
        while True:
            self.alarm.tick()
            self.watcher.range(self.vl53.range)
            sleep(self.snooze_time)


def build():
    display = BlinktDisplay()
    pomodoro = Pomodoro(display)
    alarm = Alarm(pomodoro)
    watcher = PersonWatcher(pomodoro, alarm)
    return Runner(alarm, watcher)





