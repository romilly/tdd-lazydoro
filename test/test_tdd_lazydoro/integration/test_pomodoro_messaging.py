import unittest

from hamcrest import starts_with, assert_that

from tdd_lazydoro.display_adapter import DisplayAdapter
from tdd_lazydoro.pomodoro import Pomodoro
from test_tdd_lazydoro.helpers.mocks import MockDisplay, MockMessenger


class MessageTestCase(unittest.TestCase):
    def test_message_sent_when_pomodoro_session_starts(self):
        display = MockDisplay()
        messenger = MockMessenger()
        adapter = DisplayAdapter(display, messenger)
        pomodoro = Pomodoro(adapter)
        pomodoro.start_working()
        assert_that(messenger.pop(), starts_with('pomodoro started'))


if __name__ == '__main__':
    unittest.main()
