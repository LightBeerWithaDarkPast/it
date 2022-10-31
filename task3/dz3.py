from pandas import read_html, read_csv, DataFrame
from numpy import array

def pause():
    programPause = input("Press the <ENTER> key to continue...")

def Parse():
    while True:
        try:
            Iris = read_html('https://ru.wikipedia.org/wiki/%D0%98%D1%80%D0%B8%D1%81%D1%8B_%D0%A4%D0%B8%D1%88%D0%B5%D1%80%D0%B0')[1]
        except:
            print('Не получается подключитсья к сайту или статья удалена')
            pause()
        else: break
    return Iris

def Zapis(Iris):
    L = []
    for i in range(len(Iris.index)): L.append(array([float(Iris.iloc[i, 0]), float(Iris.iloc[i, 1]), float(Iris.iloc[i, 2]), float(Iris.iloc[i, 3])]))
    Iris = DataFrame({
        'Видириса' : Iris['Видириса'], 
        'Массив' : L})
    Iris.to_csv('Iris.csv', sep='\t', header=False, index=False)

def Vvod():
    while True:
        try: par = array(list(map(float, input('Введите длину чашелистика, ширину чашелистика, длину лепестка, ширину лепестка через пробел: ').split())))
        except: pass
        else:
            if len(par) == 4:
                break
        print('\nВведены неверные данны.\n')
    return par


class NNClassifier:
    def __init__(self):
        self.par = [0, 0, 0, 0]
    def classifier(self):
        while True:
            try:
                Iris = read_csv('Iris.csv', sep='\t', header=None)
            except: print('Файл отсутствует или повреждён')
            else: break
            pause()
        dist = []
        for l in range(len(Iris.index)):
            irishist = array(list(map(float, (Iris.iloc[l, 1].strip('[]').split()))))
            d = (sum((irishist-self.par)**2))**0.5
            dist.append(d)
        Iris['2'] = dist
        Iris = Iris.sort_values(by='2')
        self.iris = Iris
        sort = [Iris.iloc[0, 0], Iris.iloc[1, 0], Iris.iloc[2, 0]]
        seto = 0; ver = 0; vir = 0
        for a in sort:
            if a == 'setosa': seto += 1
            if a == 'versicolor': ver += 1
            if a == 'virginica': vir += 1
        if seto > ver and seto > vir: otv = 'setosa'
        elif ver > seto and ver > vir: otv = 'versicolor'
        elif vir > seto and vir > ver: otv = 'virginica'
        else: otv = sort[0]
        self.otv = otv
    def display(self):
        try:
            print(self.otv, self.par, sep='\t')
        except: print('Нет данных')

Zapis(Parse())
k = 1
go = 'y'
while go == 'y':
    exp1 = NNClassifier()
    exp1.par = Vvod()
    exp1.classifier()
    exp1.display()
    while True:
        try:
            go = input('Продолжать? "y" - да, "n" - нет: ')
        except: pass
        else:
            if go == 'y' or go == 'n': break
        print('Введены неправильные данные')