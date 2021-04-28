import random
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation


class robots():
    def __init__(self, parameter=None):
        if parameter is None:
            self.database = {'id': [], 'type': [], 'mass': [], 'range': [], 'resolution': []}
        else:
            self.database = {'id': [parameter[0]], 'type': [parameter[1]], 'mass': [parameter[2]], 'range': [parameter[3]], 'resolution': [parameter[4]]}

    def add_robot(self, parameter):
        self.database['id'].append(parameter[0])
        self.database['type'].append(parameter[1])
        self.database['mass'].append(parameter[2])
        self.database['range'].append(parameter[3])
        self.database['resolution'].append(parameter[4])

    def generate_robot(self):
        id = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPRSQTUVWXYZ') for i in range(10))
        type = random.choice(['AUV','AFV','AGV'])
        mass = random.randint(50,2000)
        ran = random.randint(1,1000)
        resolution = random.randint(1,30)
        return [id, type, mass, ran, resolution]

    def generate_robots(self, M):
        description = []
        for m in range(M):
            description.append(self.generate_robot())
        return description


def quickSort(data):

    less = []
    equal = []
    greater = []

    if len(data) > 1:
        pivot = data[0]
        for x in data:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        final = quickSort(less)+equal+quickSort(greater)
        return final 
    else:
        return data


def draw(quick):
    tab_1 = []
    print(len(quick))
    for i in quick:
        tab_1.append(i)
        plt.plot(tab_1)
        plt.draw()
        plt.csl()
    print(tab_1)


def sillySort(data):
    n = len(data)
    i = 0
    while i < n - 1:
        if data[i] > data[i+1]:
            temp = data[i]
            data[i] = data[i+1]
            data[i+1] = temp
            i = 0
            continue
        i += 1
    return data


random.seed(254279)
robots_database = robots()
vector = robots_database.generate_robots(40)

count = 0
parameter = 'resolution'

df = pd.DataFrame(vector, columns=['id','type','mass','range','resolution'])
L = df[parameter].tolist()

data_1 = L.copy()
data_2 = L.copy()
print(L)
print(quickSort(data_1))
print(sillySort(data_2))