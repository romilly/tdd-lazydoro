from observer.observer import Observer
from tdd_lazydoro.pomodoro import Pomodoro


class OutputAdapter(Observer):
    def __init__(self, ui):
        self.ui = ui


    def notify(self, observable, aspect, args):
        if aspect == Pomodoro.TIME_ELAPSED:
            self.ui.set_led(7, self.ui.RED)
