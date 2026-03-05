import unittest

import pytest
from hamcrest import assert_that, equal_to

paho = pytest.importorskip("paho.mqtt.client", reason="requires paho-mqtt")

from test_tdd_lazydoro.helpers.mqtt_helper import MQTTTestClient, mqtt_send


class MQTTTestClientTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = MQTTTestClient('lazytest')

    def tearDown(self) -> None:
        self.client.close()

    def test_something(self):
        assert_that(self.client.queue_is_empty())
        mqtt_send('Hello there!')
        self.client.wait_for_message()
        assert_that(self.client.pop(), equal_to(b'Hello there!'))


if __name__ == '__main__':
    unittest.main()
