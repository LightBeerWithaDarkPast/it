# -*- coding: utf-8 -*-

import time
import random

#%% Задание 2

def calcHist(tdata):
    hist = [0]*10
    for i in tdata:
        hist[i//100] += 1
    return hist

'''
# Проверка
data = [0]*1000000
a = calcHist(data)
print(a)
'''

#%% Задание 1

def initListWithRandomNumbers():
    rand_list=[]
    n = int(1e6)
    for i in range(n):
        rand_list.append(random.randint(0,999))
    return rand_list

#%% Задание 3

def calcSumm(arr):
    summ = 0
    for val in arr:
        summ = summ + val
    return summ

Time_list = []
a = initListWithRandomNumbers()
for k in range(100):
    start = time.time()
    calcHist(a)
    end = time.time()
    Time_list.append(end-start)
print('max t =', max(Time_list))
print('average t =', calcSumm(Time_list)/100)
print('min t =', min(Time_list))
