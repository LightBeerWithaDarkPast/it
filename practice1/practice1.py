import sys
import os
import numpy as np
import time

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

try:
    File_data = np.loadtxt(sys.argv[6])
except:
    print('Файл отсутствует или повреждён')
    sys.exit()

print('\nМаршрут:')
print('x  y')
print('\n'.join(map(str, File_data)).replace('[','').replace(']',''))

N = len(File_data)-1
R = np.zeros(N)
alfa = np.zeros(N)
alfapre = 0
for i in range(N):
    XY = File_data[i+1]-File_data[i]
    if XY[0]==0:
        a = 90
    else:
        a = np.degrees(np.arctan(np.abs(XY[1]/XY[0])))
    if XY[0]>=0 and XY[1]>=0:
        b = a
    elif XY[0]<0 and XY[1]>=0:
        b = 180 - a
    elif XY[0]<0 and XY[1]<0:
        b = 180 + a
    else:
        b = 360 - a
    c = b - alfapre
    if np.abs(c)>180:
        if c>=0:
           c = 360 - c
        else:
           c = 360 + c
    alfapre = b
    alfa[i] = c
    R[i] = (sum(XY**2))**0.5
    #print(a,b,c)

V = float(sys.argv[4])
Valfa = float(sys.argv[5])
t = R/V
talfa = alfa/Valfa
tsum = t + talfa

print('\nРасстояние:')
print('\n'.join(map(str, R)))

print('\nУгол:')
print('\n'.join(map(str, alfa)))

for i in range(N):
    json = os.system('{'+('"turn": "{}", "move": "{}"'.format(alfa[i], R[i]))+'}')
    time.sleep(tsum[i]+0.1)
    #print(json)



