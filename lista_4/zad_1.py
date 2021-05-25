import random
import pickle


class robots:
    def __init__(self, par=None):
        if par is None:
            self.database = {
                "id": [],
                "type": [],
                "mass": [],
                "range": [],
                "resolution": [],
            }
        else:
            self.database = {
                "id": [par[0]],
                "type": [par[1]],
                "mass": [par[2]],
                "range": [par[3]],
                "resolution": [par[4]],
            }

    def add_robot(self, par):
        self.database["id"].append(par[0])
        self.database["type"].append(par[1])
        self.database["mass"].append(par[2])
        self.database["range"].append(par[3])
        self.database["resolution"].append(par[4])

    def generate_robot(self):
        robot_id = "".join(
            random.choice("0123456789ABCDEFGHIJKLMNOPSTUWXYZ") for i in range(10)
        )
        type = random.choice(["AUV", "AFV", "AGV"])
        mass = random.randint(50, 2000)
        ran = random.randint(1, 1000)
        resolution = random.randint(1, 30)
        return [robot_id, type, mass, ran, resolution]

    def generate_robots(self, M):
        desc = []
        for m in range(M):
            desc.append(self.generate_robot())
        return desc


def lineraSearch(vector, category, value):  # podajesz wektor, po jakim parametrze wyszukujemy i jaka wartość jest szukana
    robot_id = None                         # ustawaiamy na none, bo jakby nie było nic do wyszukania, to zwróci None
    for x in range(len(vector)):            # przechodzimy po wektorze 
        if vector[x][category] in (value, int(value)):  #jeśli wektor o indeksie 'x' i zadanej kategorii jest w szukanych wartościach (on może byc albo stringiem, albo intem w zależności od parametru)
            robot_id = x            # jak się zgadza to znaleźliśmy robota
            break                   # więc przerywamy działanie fora
    return robot_id                 # zwracamy id robota


def lineraSearchVector(vector, search_value):       #podajemy wektor i szukaną wartość (może byc to wektor wartości)
    robot_id = None
    counter = 0                                 #licznik potrzebny do 
    for x in range(len(vector)):         
        for y in range(len(search_value)):                   # przechodzmy do wektorze szukanych wartości
            if search_value[y] not in (None, vector[x][y]):  # jeżeli szukana wartość nie jest Nonem, albo w badanym wektorem robotów
                continue                                     # to przechodzimy do kolejnej iteracji
            counter += 1                                     # jak znajdziemy tę wartość to counter wzrasta i przechodzimy do kolejnego parametru
        if counter == len(search_value):                     # jeśli counter wynosi tyle co długość wektora szukanych wartości to
            robot_id = x                                     # wyświetlamy robota o tym id
            break   
        else:
            counter = 0                                      # jeśli nie to zerujemy counter i przeszukujemy kolejny wektor
    return robot_id


def advancedLineraSearchVector(vector, search_value):
    c = 0                                                   # licznik kontrolny do sprawdzania czy badany obiekt nie ma w sobie zagnieżdżonych list
    for y in range(len(search_value)):
        if type(search_value[y]) == list:                   #jeśli typ wartości to lista to 
            c += 1                                          # zwiększamy licznik o 1
            for z in range(len(search_value[y])):           # przechodzimy po elementach wektora z wartościami szukanymi (mogą być wektory w wektorach)
                robot_id = advancedLineraSearchVector(vector, vectorMerge(search_value, z, y))  #rekurencyjnie wywołujemy funkcję póki nie pozbedziemy się wszsytkich zagnieżdżonych wektorów
                if robot_id != None:                        # po znalezieniu pierwszego spełniającego warunki zwracamy go
                    return robot_id
    if c == 0 and limitCheck(search_value):                 # jeśli nie ma zagnieżdżonych wektorów to 
        robot_id = lineraSearchVector(vector, search_value) # wyszukujemy robota poprzednią funkcją i go zwracamy
        return robot_id


# funkcja sprawdza warunkami czy wpisane przez użytkownika wartości mieszczą się w zadanych przedziałach

def limitCheck(search_value):   
    limits = {1: [None, "AUV", "AFV", "AGV"], 2: [50, 2000], 3: [1, 1000], 4: [1, 30]}
    if search_value[1] in limits[1]:
        if (
            search_value[2] in range(limits[2][0], limits[2][1])
            or search_value[2] == None
        ):
            if (
                search_value[3] in range(limits[3][0], limits[3][1])
                or search_value[3] == None
            ):
                if (
                    search_value[4] in range(limits[4][0], limits[4][1])
                    or search_value[4] == None
                ):
                    return True
    print("Błędne dane", search_value)
    return False


# vectorMerge zwraca wektor z wyciętą jedną wartością z wektoru w którym się znajdowała
# lista = [2, 3, 4, [21, 32, 54], 43, [123, 213]]
# chcemy wciąć 32, więc po wykonaniu tej funkcji wektor będzie wyglądał tak:
# lista = [2, 3, 4, 32, 43, [123, 213]]

def vectorMerge(search_value, z, y):
    return search_value[:y] + [search_value[y][z]] + search_value[y + 1 :]


random.seed(254279)
robots_database = robots()
vector = robots_database.generate_robots(1000000)


# category = int(input("Podaj kategorię: 0.robot_id 1.Typ 2.Masa 3.Zasięg 4.Rozdzielczość "))
# value = input("Podaj wartość: ")
# print(lineraSearch(vector, category, value))

# print(lineraSearchVector(vector, [None, 'AFV', None, 420, 13]))

x = advancedLineraSearchVector(vector, [None, None, [22422,221373,221250,42220,420], [67222,12223,32264,42220,420], None])
if x == None:
    print("ERROR, brak robocika")
else:
    print(x, vector[x])
