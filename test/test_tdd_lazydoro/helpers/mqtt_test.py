import subprocess

import paho.mqtt.client as mqtt


class MQTTTestClient:
    def __init__(self, topic, server = 'localhost'):
        self.client = mqtt.Client(client_id='TestClient', clean_session=True)
        self.client.connect(server)
        self.client.loop_start()
        self._messages = []
        self.client.subscribe(topic)
        self.client.on_message = self.message_arrives

    def queue_is_empty(self) -> bool:
        return len(self.messages()) == 0

    def messages(self):
        result = self._messages
        return result

    def message_arrives(self, client, userdata, message):
        self._messages.append(message.payload)

    def pop(self):
        return self._messages.pop()


    def close(self):
        self.client.disconnect()


def mqtt_send(msg: str, topic: str = 'lazytest'):
    subprocess.run(['mosquitto_pub', '-t', topic, '-m', msg])
