import unittest

from hamcrest import assert_that, equal_to

from tdd_lazydoro.build import build
from tdd_lazydoro.display import Display
from test_tdd_lazydoro.helpers.mocks import MockDisplay, MockRangeFinder


class AlmostE2ETestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.rangefinder = MockRangeFinder()
        self.display = MockDisplay()
        self.ticks_per_minute = 60
        self.watcher = build(rangefinder=self.rangefinder,
                             display=self.display,
                             speed=100,
                             ticks_per_minute=self.ticks_per_minute)

    def test_principal_success_scenario(self):
        # main success scenario
        self.person_absent()
        self.wait(1)
        self.check_leds_are_off()
        self.person_present()
        self.check_leds_are_off()
        self.wait(seconds=10)
        assert_that(self.display.led_colors[:2], equal_to([Display.BLUE, Display.OFF]))
        self.wait(minutes=24)
        assert_that(self.display.led_colors, equal_to(8 * [Display.BLUE]))
        self.wait(minutes=5)
        assert_that(self.display.led_colors, equal_to(8 * [Display.RED]))
        self.person_absent()
        self.wait(minutes=0, seconds=20)
        assert_that(self.display.led_colors[:2], equal_to([Display.GREEN, Display.OFF]))

    def wait(self, minutes=0, seconds=0):
        duration = seconds + minutes * self.ticks_per_minute
        for i in range(duration):
            self.watcher.tick()

    def check_leds_are_off(self):
        for i in range(8):
            assert_that(self.display.led_colors[i], equal_to(Display.OFF))

    def person_absent(self):
        self.rangefinder.person_absent()

    def person_present(self):
        self.rangefinder.person_present()


if __name__ == '__main__':
    unittest.main()
