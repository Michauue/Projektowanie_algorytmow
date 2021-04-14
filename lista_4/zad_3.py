import random

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


def hashing(record):
        global N
        return record % N

def hashSearch(vector, record, parameter):
    tab = vector[parameter][hash(record)]
    return record in tab

temp = [12,123 ,14 ,-124,214,12,412, 4,12,532]
random.seed(254279)
robots_database = robots()
vector = robots_database.generate_robots(1000)
N = 10
print(temp[3])
hashing(temp[3])
print(temp[3])
# print(vector)