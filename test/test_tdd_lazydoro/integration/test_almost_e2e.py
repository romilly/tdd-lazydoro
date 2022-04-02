import unittest

from tdd_lazydoro.build import build
from test_tdd_lazydoro.helpers.mocks import MockDisplay, MockRangeFinder


class AlmostE2ETestCase(unittest.TestCase):
    def test_principal_success_scenario(self):
        rangefinder = MockRangeFinder()
        display = MockDisplay()
        watcher = build(rangefinder=rangefinder, display=MockDisplay(), speed=100)
        rangefinder.person_absent()
        self.wait(1)
        self.check_leds_are_off()
        rangefinder.person_present()



if __name__ == '__main__':
    unittest.main()
