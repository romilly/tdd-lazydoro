from observer.observer import Observable


class Pomodoro(Observable):
    TIME_ELAPSED = 'Time elapsed'
    WAITING = 'Waiting'
    WORKING = 'Working'
    WORKING_TICK = 'Working tick'
    BREAK_DUE = 'Should start a break'
    ON_BREAK = 'On a break'
    BREAK_TICK = 'Break tick'
    BREAK_OVER = 'Break time over'

    def __init__(self):
        Observable.__init__(self)
        self.minute_timer = 0
        self.duration = 25
        self.break_time = 5
        self.state = self.WAITING

    def minute_has_passed(self): # a minute has passed
        if self.state == self.WORKING:
            self.minute_timer += 1
            if self.minute_timer >= self.duration:
                self.break_due()
            if 0 ==self.minute_timer % 3:
                blue_index = min(7, self.minute_timer // 3)
                self.changed(self.WORKING_TICK, blue_index)

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
        self.changed(self.WORKING)

    def break_due(self):
        self.state = self.BREAK_DUE
        self.changed(self.BREAK_DUE)

    def start_waiting(self):
        self.state = self.WAITING
        self.changed(self.WAITING)

    def start_break(self):
        self.state = self.ON_BREAK
        self.minute_timer = 0
        self.changed(self.ON_BREAK)


