from tdd_lazydoro.blinkt_adapter import BlinktAdapter
from tdd_lazydoro.display import Display


class Pomodoro:
    TIME_ELAPSED = 'Time elapsed'
    WAITING = 'Waiting'
    WORKING = 'Working'
    WORKING_TICK = 'Working tick'
    BREAK_DUE = 'Should start a break'
    ON_BREAK = 'On a break'
    BREAK_TICK = 'Break tick'
    BREAK_OVER = 'Break time over'

    def __init__(self, adapter: BlinktAdapter, duration=25):
        self.adapter = adapter
        self.minute_timer = 0
        self.duration = duration
        self.break_time = 5
        self.state = self.WAITING

    def tick(self): # a minute has passed
        if self.state == self.WORKING:
            self.minute_timer += 1
            if self.minute_timer >= self.duration:
                self.break_due()
            elif 0 ==self.minute_timer % 3:
                self.adapter.show_working_progress(self.minute_timer)
        elif self.state == self.ON_BREAK:
            self.minute_timer += 1
            if self.minute_timer == 5:
                self.adapter.break_over()
            else:
                self.adapter.show_break_progress(self.minute_timer)

    def person_arrives(self):
        if self.state in [self.WAITING, self.ON_BREAK]:
            self.start_working()

    def person_leaves(self):
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
        self.adapter.start_waiting()

    def start_break(self):
        self.state = self.ON_BREAK
        self.minute_timer = 0
        self.adapter.start_break()

