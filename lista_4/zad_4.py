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

def binarySort(vector,targets,parameter):
    
    temp = []

    for target in targets:

        left = 0
        right = len(vector)
        index = 0

        print('\nSprawdzamy:',target)

        while left < right:
            index = (left + right) // 2

            print('Left:', left,'right:',right,'index:', index)

            if vector[index][parameter] == target:
                temp.append(vector[index])
                break
            elif vector[index][parameter] < target:
                left = index + 1
            else:
                right = index

    return temp


random.seed(254279)
robots_database = robots()
vector = robots_database.generate_robots(1000)
targets = [969, 420, 691, 239, 122]
# targets = ['R343Z6J28W','R3Z7Z4J38W','R3Z7Z6J222','R3Z7Z6J28W']
targets.sort()
# parameters :
# 0 - Id
# 1 - Type
# 2 - Mass       <50,2000>
# 3 - Range      <1,1000>
# 4 - Resolution <1,30>
parameter = 3
defaultSort(parameter)
print(binarySort(vector,targets,parameter))
# print(vector)
