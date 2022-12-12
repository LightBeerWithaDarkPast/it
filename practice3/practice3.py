from paho.mqtt import client as mqtt_client
import pygame

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

def game():
    successes, failures = pygame.init()
    print("{0} successes and {1} failures".format(successes, failures))
    screen = pygame.display.set_mode((720, 480))
    clock = pygame.time.Clock()
    FPS = 60
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    rect = pygame.Rect((0, 0), (32, 32))
    image = pygame.Surface((32, 32))
    image.fill(WHITE)
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.key == pygame.QUIT:
                quit()
        