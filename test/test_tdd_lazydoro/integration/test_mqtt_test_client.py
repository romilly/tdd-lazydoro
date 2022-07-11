import unittest
from hamcrest import assert_that, equal_to

from test_tdd_lazydoro.helpers.mqtt_test import MQTTTestClient, mqtt_send


class MQTTTestClientTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = MQTTTestClient('lazytest')

    def tearDown(self) -> None:
        self.client.close()

    def test_something(self):
        assert_that(self.client.queue_is_empty())
        mqtt_send('Hello there!')
        assert_that(len(self.client.messages()), equal_to(1))
        assert_that(self.client.pop(), equal_to(b'Hello there!'))


if __name__ == '__main__':
    unittest.main()
