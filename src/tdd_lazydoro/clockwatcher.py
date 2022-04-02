from time import sleep
from tdd_lazydoro.glitch_filter import GlitchFilter
from tdd_lazydoro.pomodoro import Pomodoro
from tdd_lazydoro.rangefinder import RangeFinder


class ClockWatcher:
    def __init__(self, rangefinder: RangeFinder, pomodoro: Pomodoro, speed=1, range_threshold: int=500):
        self.rangefinder = rangefinder
        self.pomodoro = pomodoro
        self.range_threshold = range_threshold
        self.person_was_present = False
        self.glitch_filter = GlitchFilter(11)
        if speed == 1:
            self.snooze_time = 1
        else:
            self.snooze_time = 1 / speed

    def is_person_in_range(self, tof_range: int):
        return tof_range < self.range_threshold

    def tell_pomodoro_if_person_arrives_or_leaves(self, tof_range: int):
        person_present = self.glitch_filter.filter(self.is_person_in_range(tof_range))
        if person_present and not self.person_was_present:
            self.pomodoro.person_arrives()
        if self.person_was_present and not person_present:
            self.pomodoro.person_leaves()
        self.person_was_present = person_present

    def run(self):
        while True:
            self.pomodoro.tick()
            self.tell_pomodoro_if_person_arrives_or_leaves(self.rangefinder.range())
            sleep(self.snooze_time)




