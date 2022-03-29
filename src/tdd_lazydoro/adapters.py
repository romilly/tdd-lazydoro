from observer.observer import Observer
from tdd_lazydoro.pomodoro import Pomodoro
from tdd_lazydoro.ui import UI


class OutputAdapter(Observer):
    def __init__(self, ui: UI):
        self.ui = ui

    def notify(self, observable, aspect, args):
        if aspect == Pomodoro.WORKING:
            self.ui.clear_leds()
            self.ui.set_led(0, UI.BLUE)
        elif aspect == Pomodoro.WORKING_TICK:
            self.ui.set_led(args[0], UI.BLUE)
        elif aspect == Pomodoro.BREAK_DUE:
            for i in range(8):
                self.ui.set_led(i, UI.RED)
        elif aspect == Pomodoro.WAITING:
            self.ui.clear_leds()
        elif aspect == Pomodoro.ON_BREAK:
            self.ui.clear_leds()
            self.ui.set_led(0, UI.GREEN)
        elif aspect == Pomodoro.BREAK_TICK:
            self.ui.set_led(args[0], UI.GREEN)
        elif aspect == Pomodoro.BREAK_OVER:
            for i in range(8):
                self.ui.set_led(i, UI.YELLOW)
            self.ui.buzz()


