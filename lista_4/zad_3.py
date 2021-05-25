import random
import pickle



class robots():
    def __init__(self, par=None):
        if par is None:
            self.database = {'id': [], 'type': [], 'mass': [], 'range': [], 'resolution': []}
        else:
            self.database = {'id': [par[0]], 'type': [par[1]], 'mass': [par[2]], 'range': [par[3]], 'resolution': [par[4]]}


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


# to to w sumie gotowa funkcja jakaś z neta lekko przekształcona

def hash_func(robot, H):
    value = 0
    str_value = 0
    for i in robot: # przechodzimy po elemnentach w danym robocie
        if type(i) == int:  #jeżeli typ to int to ustawiamy odpowiednie zmienne pomocnicze
            temp = 0    
            multiplier = 1
            for digit in str(i):    #przechodzimy po każdej cyfrze i w zalezności od jej wartości i miejsca (jedności, dziesiątki itd) otrzymuje wartość
                temp += int(digit) * multiplier
                multiplier += 1
            value += temp
        else:                       # jezeli wartość to string to 
            str_value += len(i)     # zamianeiam stringa na wartość
    return value * str_value % H    # zwracam jakąś śmieszną wygenerowaną wartość


def hash_vector(vector, H):
    h_vector = [None]*H         #towrzymy pusty wektor

    for n in range(len(vector)):        # przechodzimy po badanym wektorze
        h = hash_func(vector[n], H)     # hashujemy konkretnego robota
        if h_vector[h] is None:         
            h_vector[h] = n             # jeżeli miejsce o numerze jakiego obiekt ma hasha jest wolne to tam go umieszczamy
        else:
            check = 0
            for i in range(h, len(h_vector)-h):     # jak nie to szukamy do końca listy tego miejsca
                if h_vector[h+i] is None:
                    h_vector[h+i] = n
                    check = 1
                    break

            if check == 0:                           # a jak do końca nie będzie to zaczynamy od początku
                for i in range(h):
                    if h_vector[i] is None:
                        h_vector[i] = n
                        break

    return h_vector


def hash_find(search, vector, h_vector, H):
    h = hash_func(search, H)                    # hashujemy wartość szukaną
    n = h_vector[h]                             # sprawdzamy jaka wartość jest wpisana w zhashowanym wektorze na miejscu po zhashoawniu szukanej wartości

    if search == vector[n]:                     # jeżeli szukana zhashowana wartość znajduje się w wektorze na n-tym miejscu to essa
        return True 

    else:   
        for i in range(n, len(vector)):         # jak nie ma to szukamy dalej w prawo 
            if search == vector[i]:
                return True
        for i in range(n):                      # jak nie ma to szukamy dalej od początku
            if search == vector[i]:
                return True
    return False


random.seed(254279)
robots_database = robots()
robot = robots_database.generate_robot()

vector = robots_database.generate_robots(10)
print(vector)

print(hash_func(robot,7))

h_vector = hash_vector(vector, int(len(vector)*1.5))
print(h_vector)

search1 = ['CMTSUFH9B7', 'AFV', 983, 310, 6]
search2 = ['5FYFDG9KLP', 'AUV', 1813, 652, 10]
print(hash_find(search1, vector, h_vector, len(h_vector)))
print(hash_find(search2, vector, h_vector, len(h_vector)))
