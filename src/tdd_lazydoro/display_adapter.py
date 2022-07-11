from tdd_lazydoro.colors import *
from tdd_lazydoro.display import Display


class DisplayAdapter:
    def __init__(self, display: Display):
        self.display = display

    def show_break_progress(self, timer):
        self.display.set_led(timer, GREEN)

    def break_over(self):
        self.display.buzz()

    def start_working(self):
        self.display.clear_leds()
        self.display.set_led(0, BLUE)
        self.display.send_message('starting pomodoro')

    def show_working_progress(self, timer):
        self.display.set_led(min(7, timer // 3), BLUE)

    def ready_to_start(self):
        self.display.clear_leds()

    def break_due(self):
        for i in range(8):
            self.display.set_led(i, RED)

    def start_break(self):
        self.display.clear_leds()
        self.display.set_led(0, GREEN)

