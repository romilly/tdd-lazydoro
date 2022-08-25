import paho.mqtt.client as mqtt
from time import sleep

POMODORO_TOPIC = 'pomodoro'

class MQTTMessenger:
    def __init__(self, hostname):
        self.client = mqtt.Client(client_id='lazydoro', clean_session=True)
        self.client.connect(hostname)
        sleep(1.0)

    def send(self, message):
        self.client.publish(POMODORO_TOPIC, message)
