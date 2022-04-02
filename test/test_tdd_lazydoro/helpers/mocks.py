from tdd_lazydoro.display import Display
from tdd_lazydoro.rangefinder import RangeFinder
from tdd_lazydoro.colors import OFF



class MockDisplay(Display):
    def __init__(self):
        self.led_colors = None
        self.clear_leds()
        self.buzzing = False

    def clear_leds(self):
        self.led_colors = 8*[OFF]

    def set_led(self, number, rgb):
        self.led_colors[number] = rgb
        self.buzzing = False

    def buzz(self):
        self.buzzing = True


class MockRangeFinder(RangeFinder):
    RANGE_WHEN_PERSON_PRESENT = 300
    RANGE_WHEN_PERSON_ABSENT = 8191

    def __init__(self):
        self.current_range = self.RANGE_WHEN_PERSON_ABSENT

    def range(self) -> int:
        return self.current_range

    def person_absent(self):
        self.current_range = self.RANGE_WHEN_PERSON_ABSENT

    def person_present(self):
        self.current_range = self.RANGE_WHEN_PERSON_PRESENT




