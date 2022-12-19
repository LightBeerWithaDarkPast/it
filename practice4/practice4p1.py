import time
import sys
from threading import Thread

def simpleGeneratorFun():
    a = 0
    while True:
        a = a + 2
        yield a

def printing():
    for i in simpleGeneratorFun():
        time.sleep(1)
        with open('gen.txt', 'a') as gen:
            print(i, file=gen)

def pause():
    programPause = input("Press the <ENTER> key to stop program...")

t1 = Thread(target=pause)
t2 = Thread(target=printing, daemon=True)

t2.start()
t1.start()
