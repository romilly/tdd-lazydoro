import unittest

from hamcrest import assert_that, equal_to

from tdd_lazydoro.raspi.build import build
from tdd_lazydoro.colors import *
from tdd_lazydoro.raspi.mqtt import POMODORO_TOPIC

from test_tdd_lazydoro.helpers.mocks import MockDisplay, MockRangeFinder, shows_only, shows_all
from test_tdd_lazydoro.helpers.mqtt_test import MQTTTestClient


class AlmostE2ETestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.rangefinder = MockRangeFinder()
        self.display = MockDisplay()
        self.ticks_per_minute = 60
        self.mqtt_client = MQTTTestClient(POMODORO_TOPIC)
        self.watcher = build(rangefinder=self.rangefinder,
                             display=self.display,
                             speed=100,
                             ticks_per_minute=self.ticks_per_minute)

    def tearDown(self) -> None:
        self.mqtt_client.close()

    def test_tracks_full_pomodoro(self):
        # main success scenario
        self.person_absent()
        self.wait(1)
        self.check_leds_are_off()
        self.person_present()
        self.check_leds_are_off()
        self.wait(seconds=10)
        assert_that(self.display, shows_only(BLUE))
        self.wait(minutes=24)
        self.mqtt_client.wait_for_message()
        assert_that(len(self.mqtt_client.messages()), equal_to(1))
        assert_that(self.display, shows_all(BLUE))
        self.wait(minutes=5)
        assert_that(self.display, shows_all(RED))
        self.person_absent()
        self.wait(seconds=20)
        assert_that(self.display, shows_only(GREEN))
        self.wait(minutes=1)
        assert_that(self.display, shows_only(GREEN, GREEN))
        self.wait(minutes=1)
        assert_that(self.display, shows_only(GREEN, GREEN, GREEN))
        self.wait(minutes=1)
        assert_that(self.display, shows_only(GREEN, GREEN, GREEN, GREEN))
        self.wait(minutes=1)
        assert_that(self.display, shows_only(GREEN, GREEN, GREEN, GREEN, GREEN))
        self.wait(minutes=1)
        self.check_leds_are_off()
        self.person_present()
        self.wait(seconds=20)
        assert_that(self.display, shows_only(BLUE))
        # print(self.mqtt_client.messages())

    # def test_returns_to_working_if_person_returns_early_during_break(self):
    #     self.person_present()
    #     self.wait(26)
    #     self.person_absent()
    #     self.wait(minutes=1)
    #     self.person_present()
    #     self.wait(seconds=20)
    #     assert_that(self.display, shows_only(BLUE))

    def wait(self, minutes=0, seconds=0):
        duration = seconds + minutes * self.ticks_per_minute
        for i in range(duration):
            self.watcher.tick()

    def check_leds_are_off(self):
        for i in range(8):
            assert_that(self.display.led_colors[i], equal_to(OFF))

    def person_absent(self):
        self.rangefinder.person_absent()

    def person_present(self):
        self.rangefinder.person_present()


if __name__ == '__main__':
    unittest.main()
