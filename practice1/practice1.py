import sys
import os
from paho.mqtt import client as mqtt_client
import numpy as np
import time

def arg():
    print('Аргументы командной строки:')
    try:
        print('Файл программы:', sys.argv[0])
        print('IP адрес mqtt брокера:', sys.argv[1])
        print('Номер порта:', sys.argv[2])
        print('Имя топика:', sys.argv[3])
        print('Скорость движения бота (м/с):', sys.argv[4])
        print('Скорость поворота бота (град/с):', sys.argv[5])
        print('Полный путь к файлу координат:', sys.argv[6])
    except:
        print('Отсутствуют необходимые параметны командной строки')
        sys.exit()

def path():
    try:
        File_data = np.loadtxt(sys.argv[6])
    except:
        print('Файл отсутствует или повреждён')
        sys.exit()
    return File_data

def pathprint(File_data):
    print('\nМаршрут:')
    print('x  y')
    print('\n'.join(map(str, File_data)).replace('[','').replace(']',''))

def rastoyanie(File_data, i):
    XY = File_data[i+1]-File_data[i]
    return XY

def ugol(XY):
    if XY[0]==0:
        a = 90
    else:
        a = np.degrees(np.arctan(np.abs(XY[1]/XY[0])))
    return a

def polojenie_v_absolut_koordinat(XY, a):
    if XY[0]>=0 and XY[1]>=0:
        b = a
    elif XY[0]<0 and XY[1]>=0:
        b = 180 - a
    elif XY[0]<0 and XY[1]<0:
        b = 180 + a
    else:
        b = 360 - a
    return b

def delta_povorota(b, alfapre):
    c = b - alfapre
    napr = 1
    if np.abs(c)>90:
        if np.abs(c)>270:
            if c>0:
                c = 360 - c
            else:
                c = 360 + c
        else:
            napr = -1
            if c>0:
                c = c - 180
            else:
                c = 180 + c
    return napr, c


def navig(File_data):
    N = len(File_data)-1
    R = np.zeros(N)
    alfa = np.zeros(N)
    alfapre = 0
    for i in range(N):
        XY = rastoyanie(File_data, i)
        a = ugol(XY)
        b = polojenie_v_absolut_koordinat(XY, a)
        Vsio = delta_povorota(b, alfapre)
        napr = Vsio[0]
        c = Vsio[1]
        alfapre = b
        alfa[i] = c
        R[i] = napr*(sum(XY**2))**0.5
        #print(a,b,c)
    return alfa, R, N

def Skor_i_vrem(alfa, R):
    V = float(sys.argv[4]))
    Valfa = float(sys.argv[5])
    t = R/V
    talfa = alfa/Valfa
    tsum = t + talfa
    return tsum

def Vivod_rasstoyaniya(R):
    print('\nРасстояние:')
    print('\n'.join(map(str, R)))

def Vivod_uglof_povorota(alfa):
    print('\nУгол:')
    print('\n'.join(map(str, alfa)))

def Formirovanie_json(N, alfa, R, tsum):
    for i in range(N):
        json = os.system('{'+('"turn": "{}", "move": "{}"'.format(alfa[i], R[i]))+'}')
        time.sleep(tsum[i]+0.1)
        #print(json)
        return json

def Publish(msg):
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
    
    def publish(client):
        while True:
            result = client.publish(topic, msg)
            status = result[0]
            if status == 0:
                print(f"Send '{msg}' to topic '{topic}'")
            else:
                print(f"Failed to send message to topic {topic}")
    
    def run():
        client = connect_mqtt()
        client.loop_forever()
        publish(client)
    
    if __name__ == '__main__':
        run()



arg()
File_data = path()
pathprint(File_data)
result = navig(File_data)
alfa = result[0]
R = result[1]
N = result[2]
tsum = Skor_i_vrem(alfa, R)
Vivod_rasstoyaniya(R)
Vivod_uglof_povorota(alfa)
json = Formirovanie_json(N, alfa, R, tsum)
Publish(json)