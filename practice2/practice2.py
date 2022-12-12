from paho.mqtt import client as mqtt_client
import json

def Subscribe():
    brocker = '127.0.0.1'
    port = 1883
    topic = 'botcontrol'
    client_id = 'b1'

    def connect_mqtt():

        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                    print('Connected to MQTT Brocker!')
            else:
                print('Failed to connect, return code %d\n', rc)

        client = mqtt_client.Client(client_id)
        client.on_connect = on_connect
        client.connect(brocker, port)
        return client
    
    def subscribe(client):
        
        def on_message(client, userdata, msg):
            global message_received
            message_received = str(msg.payload.decode())
            print(f"Received '{msg.payload.decode()}' from '{msg.topic}' topic")
        
        client.subscribe(topic)
        client.on_message = on_message
    
    def run():
        client = connect_mqtt()
        subscribe(client)
        client.loop_forever()
    
    if __name__ == '__main__':
        run()

def to_dict():
    message_received_dict = json.loads(message_received)
    #print(message_received_dict)
    return message_received_dict

class bot_model:

    def __init__(self):
        message_received_dict = to_dict()
        self.V = message_received_dict['V']
        self.Valfa = message_received_dict['Valfa']
        self.cmd = message_received_dict['cmd']
        self.val = message_received_dict['val']

    def move(self):
        if self.cmd == 'forward':
            move = 
        if self.cmd == 'back':
        if self.cmd == 'left':
        if self.cmd == 'right':



