from observer.observer import Observer
from tdd_lazydoro.pomodoro import Pomodoro


class OutputAdapter(Observer):
    def __init__(self, ui):
        self.ui = ui

    def notify(self, observable, aspect, args):
        if aspect == Pomodoro.TIME_ELAPSED:
            self.ui.clear_leds()
        elif aspect == Pomodoro.STEP:
            self.ui.set_led(args[0], self.ui.RED)
