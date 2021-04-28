import random
import pickle
import pandas as pd


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


def counting_sort(L):
    temp_tab = []
    
    print("Tworzenie tablicy pomocniczej")
    for i in range(31):
        temp_tab.append(0);
    
    print("Start zliczania elementów")
    for a in L:
        print("Zliczono element: " + str(a))
        temp_tab[a] = temp_tab[a] + 1
    
    print("Układam posortowaną tablicę")
    k = 0
    for a in range(31):
        for c in range(0,temp_tab[a]):
            L[k] = a
            k = k + 1
    return L


random.seed(254279)
robots_database = robots()
vector = robots_database.generate_robots(80)

df = pd.DataFrame(vector, columns=['id','type','mass','range','resolution'])
L = df['resolution'].tolist()
print('Tablica przed sortowaniem:',L)
L = counting_sort(L)
print('Tablica po posortowaniu:',L)