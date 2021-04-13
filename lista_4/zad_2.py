import random
import pickle


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
        id = ''.join(random.choice('024') for i in range(10))
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


def table_creator(data):
    head = ['id','type','mass','range','resolution']
    for i in range(len(data)):
        data[i] = [str(j) for j in data[i]]
    draw_line(head)
    for d in data:
        draw_line(d)

def draw_line(data):
    print('|', end='')
    for i in data:
        print(i, end=' ' * (11 - len(i)) + '| ')
    print('\n', '-'*64)

def save_data(data, file):
    with open(file, 'wb') as fp:
        pickle.dump(data, fp)

def read_data(file):
    with open(file, 'rb') as fp:
        return pickle.load(fp)




robots_database = robots()
vector = robots_database.generate_robots(1000)
