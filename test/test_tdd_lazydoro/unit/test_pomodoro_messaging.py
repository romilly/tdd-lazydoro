import unittest

from hamcrest import assert_that, equal_to

from tdd_lazydoro.display_adapter import DisplayAdapter
from tdd_lazydoro.pomodoro import Pomodoro
from test_tdd_lazydoro.helpers.mocks import MockDisplay


class MockMessenger:
    def message_count(self):
        return 1


class PomodoroMessagingTestCase(unittest.TestCase):
    def test_sends_message_when_pomodoro_session_starts(self):
        display = MockDisplay()
        messenger = MockMessenger()
        adapter= DisplayAdapter(display, messenger)
        pomodoro = Pomodoro(adapter)
        pomodoro.start_working()
        assert_that(messenger.message_count(), equal_to(1))



if __name__ == '__main__':
    unittest.main()
