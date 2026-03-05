import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion

POMODORO_TOPIC = 'pomodoro'

class MQTTMessenger:
    def __init__(self, hostname):
        self.client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2, client_id='lazydoro')
        self.client.connect(hostname)

    def send(self, message):
        self.client.publish(POMODORO_TOPIC, message)
