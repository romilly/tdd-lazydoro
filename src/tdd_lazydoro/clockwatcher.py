import board
import busio
import adafruit_vl53l0x
from time import sleep

from tdd_lazydoro.blinkt_adapter import BlinktAdapter
from tdd_lazydoro.blinkt_display import BlinktDisplay
from tdd_lazydoro.pomodoro import Pomodoro

i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)


class Alarm:
    def __init__(self, pomodoro: Pomodoro, alarm_time=60):
        self.pomodoro = pomodoro
        self.alarm_time = alarm_time
        self.ticks = 0

    def tick(self):
        # print('tick %d' % self.ticks)
        self.ticks += 1
        if self.ticks >= self.alarm_time:
            self.pomodoro.tick()
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
        if tof_range == 0:  # sometimes get this when nothing is in range
            tof_range = 8191
        person_present = tof_range < self.range_threshold
        if person_present != self.person_was_present:
            self.alarm.reset()
        if person_present and not self.person_was_present:
            self.pomodoro.person_arrives()
        if self.person_was_present and not person_present:
            self.pomodoro.person_leaves()
        self.person_was_present = person_present


class ClockWatcher:
    def __init__(self, alarm: Alarm, watcher: PersonWatcher):
        self.alarm = alarm
        self.watcher = watcher
        self.snooze_time = 1

    def run(self, speed=1, alarm_time=60, duration=25):
        self.alarm.alarm_time = alarm_time
        self.alarm.pomodoro.duration = duration
        if speed == 1:
            self.snooze_time = 1
        else:
            self.snooze_time = 1 / speed
        while True:
            self.alarm.tick()
            self.watcher.range(vl53.range)
            sleep(self.snooze_time)


def build():
    display = BlinktDisplay()
    pomodoro = Pomodoro(BlinktAdapter(display))
    alarm = Alarm(pomodoro)
    watcher = PersonWatcher(pomodoro, alarm)
    return ClockWatcher(alarm, watcher)





