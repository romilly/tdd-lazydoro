import unittest

from hamcrest import assert_that, equal_to

from tdd_lazydoro.adapters import OutputAdapter
from tdd_lazydoro.pomodoro import Pomodoro
from tdd_lazydoro.ui import UI


class MockUI(UI):
    def __init__(self):
        self.led_colors = None
        self.clear_leds()

    def clear_leds(self):
        self.led_colors = 8*[UI.OFF]

    def set_led(self, number, rgb):
        self.led_colors[number] = rgb


class PomodoroTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.pomodoro = Pomodoro()
        self.ui = MockUI()
        self.output_adapter = OutputAdapter(self.ui)
        self.pomodoro.add_observer(self.output_adapter)

    def test_display_is_clear_at_start(self):
        for i in range (8):
            assert_that(self.ui.led_colors[i], equal_to(UI.OFF))

    def test_one_led_is_blue_when_working_starts(self):
        self.pomodoro.person_arrives()
        assert_that(self.ui.led_colors[:2], equal_to([UI.BLUE, UI.OFF]))

    def test_eight_leads_are_blue_just_before_pomodoro_over(self):
        self.pomodoro.person_arrives()
        for i in range(24):
            self.pomodoro.minute_has_passed()
        assert_that(self.ui.led_colors, equal_to(8*[UI.BLUE]))

    def test_eight_leda_are_red_when_pomodoro_over(self):
        self.pomodoro.person_arrives()
        for i in range(25):
            self.pomodoro.minute_has_passed()
        assert_that(self.ui.led_colors, equal_to(8*[UI.RED]))






    # def test_pomodoro_alerts_when_25_minutes_are_up(self):
    #     self.pomodoro.person_arrives()
    #     for i in range(24):
    #         self.pomodoro.minute_has_passed()
    #         self.assertFalse(self.ui.alert)
    #     self.ui.tick()
    #     self.assertTrue(self.ui.alert)


if __name__ == '__main__':
    unittest.main()
