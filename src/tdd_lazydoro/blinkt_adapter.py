from tdd_lazydoro.display import Display


class BlinktAdapter:
    def __init__(self, display: Display):
        self.display = display

    def show_break_progress(self, timer):
        self.display.set_led(timer, Display.GREEN)

    def break_over(self):
        for i in range(8):
            self.display.set_led(i, Display.YELLOW)
        self.display.buzz()

    def show_working_progress(self, timer):
        self.display.set_led(min(7, timer // 3), Display.BLUE)

    def start_working(self):
        self.display.clear_leds()
        self.display.set_led(0, Display.BLUE)

    def break_due(self):
        for i in range(8):
            self.display.set_led(i, Display.RED)

    def start_waiting(self):
        self.display.clear_leds()

    def start_break(self):
        self.display.clear_leds()
        self.display.set_led(0, Display.GREEN)

