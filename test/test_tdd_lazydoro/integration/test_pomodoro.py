import unittest

from tdd_lazydoro.adapters import OutputAdapter
from tdd_lazydoro.pomodoro import Pomodoro
from tdd_lazydoro.ui import UI


class MockUI(UI):
    def __init__(self):
        self.led_colors = 8*[None]

    def clear_leds(self):
        self.led_colors = 8*[None]

    def set_led(self, number, color):
        self.led_colors[number] = color



class PomodoroTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.pomodoro = Pomodoro()
        self.ui = MockUI()
        self.output_adapter = OutputAdapter(self.ui)
        self.pomodoro.add_observer(self.output_adapter)

    def test_pomodoro_alerts_when_25_minutes_are_up(self):
        self.pomodoro.person_arrives()
        for i in range(24):
            self.pomodoro.minute_has_passed()
            self.assertFalse(self.ui.alert)
        self.ui.tick()
        self.assertTrue(self.ui.alert)


if __name__ == '__main__':
    unittest.main()
