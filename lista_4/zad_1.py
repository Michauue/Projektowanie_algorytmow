import random
import pickle



class robots():
    def __init__(self, par=None):
        if par is None:
            self.database = {'id': [], 'type': [], 'mass': [], 'range': [], 'resolution': []}
        else:
            self.database = {'id': [par[0]], 'type': [par[1]], 'mass': [par[2]], 'range': [par[3]], 'resolution': [par[4]]}

    def add_robot(self, par):
        self.database['id'].append(par[0])
        self.database['type'].append(par[1])
        self.database['mass'].append(par[2])
        self.database['range'].append(par[3])
        self.database['resolution'].append(par[4])

    def generate_robot(self):
        id = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPSTUWXYZ') for i in range(10))
        type = random.choice(['AUV','AFV','AGV'])
        mass = random.randint(50,2000)
        ran = random.randint(1,1000)
        resolution = random.randint(1,30)
        return [id, type, mass, ran, resolution]

    def generate_robots(self, M):
        desc = []
        for m in range(M):
            desc.append(self.generate_robot())
        return desc

def linear_search(vector, category, value):
    id = None
    for x in range(len(vector)):
        if vector[x][category] in (value, int(value)) :
            id = x
            break
    return id
    
def linear_search_vector(vector, search_value):
    id = None
    counter = 0
    for x in range(len(vector)):
        for y in range(len(search_value)):
            if search_value[y] not in (None, vector[x][y]):
                continue
            counter += 1
        if counter == len(search_value):
            id = x
            break
        else:
            counter = 0
    return id

def adv_linear_search_vector(vector, search_value):
    c = 0
    for y in range(len(search_value)):
        if type(search_value[y]) == list:
            c += 1
            for z in range(len(search_value[y])):
                id =adv_linear_search_vector(vector, vector_merge(search_value, z, y))
                if id != None:
                    return id
    if c == 0 and limit_check(search_value):
        id = linear_search_vector(vector, search_value)
        return id
     


def limit_check(search_value):
    limits = {1: [None,'AUV','AFV','AGV'], 2: [50, 2000], 3: [1,1000], 4:[1,30]}
    if search_value[1] in limits[1]:
        if search_value[2] in range(limits[2][0],limits[2][1]) or search_value[2] == None:
            if search_value[3] in range(limits[3][0],limits[3][1])or search_value[3] == None:
                if search_value[4] in range(limits[4][0],limits[4][1])or search_value[4] == None:
                    return True
    print("Błędne dane")
    return False

def vector_merge(search_value, z, y):
    return search_value[:y] + [search_value[y][z]] + search_value[y+1:]


random.seed(254279)
robots_database = robots()
vector = robots_database.generate_robots(100000)


category = int(input("Podaj kategorię: 0.Id 1.Typ 2.Masa 3.Zasięg 4.Rozdzielczość "))
value = input("Podaj wartość: ")
print(linear_search(vector, category, value))

# print(linear_search_vector(vector, [None, 'AFV', None, 173, 13]))
# print(adv_linear_search_vector(vector, [None, None, [550,72,1374,1250,715], [72,578,890,123,364], None]))
# 




