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
        self.glitch_filter = GlitchFilter(11) # maybe make 11 an optional parameter
        self.snooze_time = 1 / speed

    def is_person_in_range(self, tof_range: int):
        return tof_range < self.range_threshold

    def check_comings_and_goings(self, person_now_present, person_was_present):
        if person_now_present and not person_was_present:
            self.person_arrives()
        elif person_was_present and not person_now_present:
            self.person_leaves()

    def person_leaves(self):
        self.pomodoro.person_leaves()

    def person_arrives(self):
        self.pomodoro.person_arrives()

    # TODO: move this out to a runner
    def run(self):
        while True: # pragma: no cover
            self.tick()
            sleep(self.snooze_time)

    def tick(self):
        self.pomodoro.tick()
        range = self.rangefinder.range()
        person_now_present = self.glitch_filter.filter(self.is_person_in_range(range))
        self.check_comings_and_goings(person_now_present, self.person_was_present)
        self.person_was_present = person_now_present # ready for next tick




