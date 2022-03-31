from tdd_lazydoro.display import Display


class MockDisplay(Display):
    def __init__(self):
        self.led_colors = None
        self.clear_leds()
        self.buzzing = False

    def clear_leds(self):
        self.led_colors = 8*[Display.OFF]

    def set_led(self, number, rgb):
        self.led_colors[number] = rgb
        self.buzzing = False

    def buzz(self):
        self.buzzing = True