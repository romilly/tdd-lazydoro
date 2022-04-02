import unittest

from hamcrest import assert_that, equal_to

from tdd_lazydoro.blinkt_adapter import BlinktAdapter
from test_tdd_lazydoro.helpers.mocks import MockDisplay
from tdd_lazydoro.pomodoro import Pomodoro
from tdd_lazydoro.display import Display


class PomodoroTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.display = MockDisplay()
        self.pomodoro = Pomodoro(BlinktAdapter(self.display), ticks_per_minute=4) # short minutes for testing

    def wait(self, minutes=1): # short minutes for tests
        for i in range(4*minutes):
            self.pomodoro.tick()

    # def test_display_is_off_at_start(self):
    #     self.check_leds_are_off()
    #
    # def check_leds_are_off(self):
    #     # main success scenario
    #     for i in range(8):
    #         assert_that(self.display.led_colors[i], equal_to(Display.OFF))
    #
    # def test_one_led_is_blue_when_working_starts(self):
    #     # main success scenario
    #     self.pomodoro.person_arrives()
    #     assert_that(self.display.led_colors[:2], equal_to([Display.BLUE, Display.OFF]))
    #
    # def test_eight_leads_are_blue_just_before_pomodoro_over(self):
    #     # main success scenario
    #     self.pomodoro.person_arrives()
    #     self.wait(24)
    #     assert_that(self.display.led_colors, equal_to(8 * [Display.BLUE]))
    #
    # def test_eight_leds_are_red_when_pomodoro_over(self):
    #     # main success scenario
    #     self.pomodoro.person_arrives()
    #     self.wait(25)
    #     assert_that(self.display.led_colors, equal_to(8 * [Display.RED]))
    #     self.pomodoro.tick()
    #     assert_that(self.display.led_colors, equal_to(8 * [Display.RED]))
    #
    # def test_goes_back_to_waiting_if_someone_leaves_early(self):
    #     self.pomodoro.person_arrives()
    #     self.wait(24)
    #     self.pomodoro.person_leaves()
    #     self.check_leds_are_off()
    #     assert_that(self.pomodoro.state, equal_to(Pomodoro.WAITING))
    #
    # def test_shows_green_led_when_person_leaves_during_break(self):
    #     self.takes_break()
    #     assert_that(self.display.led_colors[:2], equal_to([Display.GREEN, Display.OFF]))
    #
    # def test_returns_to_working_if_person_returns_early_during_break(self):
    #     self.takes_break()
    #     self.wait()
    #     self.pomodoro.person_arrives()
    #     assert_that(self.display.led_colors[:2], equal_to([Display.BLUE, Display.OFF]))
    #
    # def takes_break(self):
    #     self.pomodoro.person_arrives()
    #     self.wait(26)
    #     self.pomodoro.person_leaves()
    #
    # def test_extra_green_led_show_for_each_minute_of_a_break(self):
    #     self.takes_break()
    #     self.wait(4)
    #     assert_that(self.display.led_colors[:5], equal_to(5 * [Display.GREEN]))
    #
    # def test_break_leds_go_yellow_after_5_minutes_and_buzzer_sounds(self):
    #     self.takes_break()
    #     self.wait(5)
    #     self.check_leds_are_off()
    #     self.assertTrue(self.display.buzzing)
    #
    # def test_allows_breaks_longer_than_5_minutes(self):
    #     self.takes_break()
    #     self.wait(10)
    #     self.check_leds_are_off()


if __name__ == '__main__':
    unittest.main()
