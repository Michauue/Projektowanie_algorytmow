import random
import pickle
import copy
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


def takeId(parameter):
    return parameter[0]

def takeType(parameter):
    return parameter[1]

def takeMass(parameter):
    return parameter[2]

def takeRange(parameter):
    return parameter[3]

def takeResolution(parameter):
    return parameter[4]

def defaultSort(parameter):
    if parameter == 0:
        return vector.sort(key=takeId)
    elif parameter == 1:
        return vector.sort(key=takeType)
    elif parameter == 2:
        return vector.sort(key=takeMass)
    elif parameter == 3:
        return vector.sort(key=takeRange)
    elif parameter == 4:
        return vector.sort(key=takeResolution)


def suppVectors(vector):
    all_vectors = []
    for i in range(5):
        all_vectors.append([])
    for i in range(5):
        defaultSort(i)
        x = vector.copy()
        all_vectors[i] = x
    return all_vectors


def alternative(vector):
    df = pd.DataFrame(vector, columns=['id','type','mass','range','resolution'])
    x = df.index.tolist()
    print('Default:',x)

    df = df.sort_values('id')
    x = df.index.tolist()
    print('Id:',x)
    id_vector = x

    x = df.index.tolist()
    df = df.sort_values('type')
    print('Type:',x)
    type_vector = x

    x = df.index.tolist()
    df = df.sort_values('mass')
    print('Mass:',x)
    mass_vector = x

    x = df.index.tolist()
    df = df.sort_values('range')
    print('Range:',x)
    range_vector = x

    x = df.index.tolist()
    df = df.sort_values('resolution')
    print('Resolution:',x)
    resolution_vector = x

    return id_vector,type_vector,mass_vector,range_vector,resolution_vector


random.seed(254279)
robots_database = robots()
vector = robots_database.generate_robots(6)
# parameter = 2
# defaultSort(parameter)
# print(generateAllVectors(vector))
# print(suppVectors(vector))
alternative(vector)
