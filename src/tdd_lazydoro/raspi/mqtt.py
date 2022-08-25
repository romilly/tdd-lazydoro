import paho.mqtt.client as mqtt

POMODORO_TOPIC = 'pomodoro'

class MQTTMessenger:
    def __init__(self, hostname):
        self.client = mqtt.Client(client_id='lazydoro', clean_session=True)
        self.client.connect(hostname)

    def send(self, message):
        self.client.publish(POMODORO_TOPIC, message)
