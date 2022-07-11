import unittest

from hamcrest import assert_that, equal_to

from tdd_lazydoro.display_adapter import DisplayAdapter
from tdd_lazydoro.pomodoro import Pomodoro
from test_tdd_lazydoro.helpers.mocks import MockDisplay


class PomodoroTestCase(unittest.TestCase):
    def test_message_sent_when_pomodoro_session_starts(self):
        mock_display = MockDisplay()
        adapter = DisplayAdapter(mock_display)
        pomodoro = Pomodoro(adapter)
        pomodoro.start_working()
        assert_that(mock_display.message_length(), equal_to(1))


if __name__ == '__main__':
    unittest.main()
