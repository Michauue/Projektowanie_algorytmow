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

def binarySort(vector,target,parameter,left,right,index):

    print('\nSprawdzamy:',target)
    while left <= index and index <= right:
        index = (left + right) // 2

        if left == index == right:
            break
        
        print('Left:', left,'right:',right,'index:', index)

        if vector[index][parameter] == target:
            if vector[index] in temp1:
                break
            temp1.append(vector[index])
            temp2.append(index)
            if left == index and index == right:
                break
            binarySort(vector,target,parameter,left,index,(left + index)//2)
            if left == index and index == right:
                break
            binarySort(vector,target,parameter,index,right,(right + index)//2)
        elif vector[index][parameter] < target:
            left = index + 1
            index += 1
        else:
            right = index
        
    return temp2

def startingFunction(vector,targets,parameter,left,right,index):
    
    global temp1
    global temp2
    temp1 = []
    temp2 = []

    for target in targets:
        x = binarySort(vector,target,parameter,left,right,index)
        x.sort()
    return x


random.seed(254279)
robots_database = robots()
vector = robots_database.generate_robots(1000)
left = 0
right = len(vector)
index = 1
target_min = 420
target_max = 430
targets = []
for i in range(target_min,target_max+1):
    targets.append(i)
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
print(startingFunction(vector,targets,parameter,left,right,index))
# print(vector)
