from tdd_lazydoro.display_adapter import DisplayAdapter
from tdd_lazydoro.alarm import Alarm


class Pomodoro:
    TIME_ELAPSED = 'Time elapsed'
    WAITING = 'Waiting'
    WORKING = 'Working'
    WORKING_TICK = 'Working tick'
    BREAK_DUE = 'Should start a break'
    ON_BREAK = 'On a break'
    BREAK_TICK = 'Break tick'

    def __init__(self, adapter: DisplayAdapter, duration=25, break_time=5,
                 ticks_per_minute=60):
        self.adapter = adapter
        self.minute_timer = 0
        self.duration = duration
        self.break_time = break_time
        self.state = self.WAITING
        self.alarm = Alarm(ticks_per_minute)
        self.start_waiting()

    def tick(self): # time has passed
        if self.alarm.tick():
            self.tock()

    def tock(self): # lots of time has passed
        if self.state == self.WORKING:
            self.minute_timer += 1
            if self.minute_timer >= self.duration:
                self.break_due()
            elif 0 == self.minute_timer % 3:
                self.adapter.show_working_progress(self.minute_timer)
        elif self.state == self.ON_BREAK:
            self.minute_timer += 1
            if self.minute_timer == 5:
                self.adapter.break_over()
                self.start_waiting()
            else:
                self.adapter.show_break_progress(self.minute_timer)

    def person_arrives(self):
        self.alarm.reset()
        if self.state in [self.WAITING, self.ON_BREAK]:
            self.start_working()

    def person_leaves(self):
        self.alarm.reset()
        if self.state == self.WORKING:
            self.start_waiting()
        elif self.state == self.BREAK_DUE:
            self.start_break()

    def start_working(self):
        self.state = self.WORKING
        self.minute_timer = 0
        self.adapter.start_working()

    def break_due(self):
        self.state = self.BREAK_DUE
        self.adapter.break_due()

    def start_waiting(self):
        self.state = self.WAITING
        self.adapter.ready_to_start()

    def start_break(self):
        self.state = self.ON_BREAK
        self.minute_timer = 0
        self.adapter.start_break()

