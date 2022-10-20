# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:24:15 2022

@author: Александр
"""

from numpy import array

#%% Задание 1

def triangle(a):
    for i in range(a + 1):
        print(' ' * (a - i) + '*' * (2 * i + 1))

while True:        
    try: a = int(input('Введите число звездочек слева и справа от \
центральноей звездочки на нижней стороне: '))
    except: pass
    else:
        if a >= 0: break
    print('\nВведены неверные данные.\n')
    
triangle(a)

#%% Задание 2

def histDistanve(hist1, hist2):
    return (sum((hist1-hist2)**2))**0.5

while True:
    try: hist1 = array(list(map(float, input('Введите компоненты вектора №1 \
через пробел: ').split())))
    except: print('\nВведены неверные данны.\n')
    else: break

while True:
    try: hist2 = array(list(map(float, input('\nВведите компоненты вектора №2 \
через пробел: ').split())))
    except: pass
    else:
        if len(hist2) == len(hist1): break
    print('\nВведены неверные данные.')

d = histDistanve(hist1, hist2)
print('\nДекартово расстояния между гистограммами:', d)

#%% Задание 3

def printhist():
    f1 = open('hist1.txt', 'w')
    f2 = open('hist2.txt', 'w')
    print(hist1, file = f1)
    print(hist2, file = f2)
    f1.close()
    f2.close()
    
printhist()

#%% Задание 4

def readhist():
    with open('hist1.txt') as f1: print('hist1.txt:', f1.read())
    with open('hist2.txt') as f2: print('hist2.txt:', f2.read())
    
readhist()
