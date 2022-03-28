from observer.observer import Observable


class Pomodoro(Observable):
    TIME_ELAPSED = 'Time elapsed'

    def __init__(self):
        Observable.__init__(self)
        self.minute_timer = 0
        self.duration = 25

    def minute_has_passed(self): # a minute has passed
        self.minute_timer += 1
        if self.minute_timer >= self.duration:
            self.changed(self.TIME_ELAPSED)