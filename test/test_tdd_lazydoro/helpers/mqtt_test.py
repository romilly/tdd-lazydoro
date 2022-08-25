import subprocess
import uuid
from time import sleep

import paho.mqtt.client as mqtt


class MQTTTestClient:
    def __init__(self, topic, server = 'localhost'):
        client_id = 'TestClient-%s' % str(uuid.uuid1())
        self.client = mqtt.Client(client_id=client_id, clean_session=True)
        self.client.connect(server)
        self.client.loop_start()
        self._messages = []
        self.client.subscribe(topic)
        self.client.on_message = self.message_arrives

    def queue_is_empty(self) -> bool:
        return len(self.messages()) == 0

    def messages(self):
        return self._messages

    def message_arrives(self, client, userdata, message):
        self._messages.append(message.payload)

    def pop(self):
        return self._messages.pop()

    def close(self):
        self.client.disconnect()

    def message_count(self):
        return len(self.messages())

    def wait_for_message(self, tries = 100, interval = 0.01):
        for i in range(tries):
            if len(self.messages()) > 0:
                return
            sleep(interval)
        raise ValueError('waiting for message - timed out')


def mqtt_send(msg: str, topic: str = 'lazytest'):
    subprocess.run(['mosquitto_pub', '-t', topic, '-m', msg])
