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


#funkcje potrzebne do sortowania pierwotnej listy robotów zależnie od wybranego parametru

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


# główna funkcja wyszukująca zadane wartości, podczas przygotowania zadania korzystałem w głównej mierze ze stronki: https://analityk.edu.pl/wyszukiwanie-binarne/

def binarySort(vector,targets,parameter):       #na wejściu podajemy vector - lista robotów; targets - wartości jakich szukamy, parameter - parametr, który przeszukujemy
    
    for target in targets:           # przechodzimy po każdej wartości w liście szukanych wartości - od najmniejszej do największej

        left = 0                        #początkowy lewy zakres
        right = len(vector)             #początkowy prawy zakres
        index = 0                       #początkowy index, czyli miejsce na którym jest szukana przez nas wartość 

        print('\nSprawdzamy:',target)

        while left < right:                 #pętla zapewnia działanie programu do momentu zrównania się lewego i prawego zakresu
            index = (left + right) // 2     #definiujemy wartość index, którą będzeimy sprawdzać. Wartość ta dzieli listę na dwa zbiory (znak // użyty by nie było watości po przecinku)

            print('Left:', left,'right:',right,'index:', index)

            if vector[index][parameter] == target:      # jeżeli parametr (po którym szukamy) robota o sprawdzanym indeksie jest taki sam jak sprawdzana wartość target 
                return vector[index]                    # to kończymy działanie funkcji zwracając robota, który spełnił warunek
            elif vector[index][parameter] < target:     # jeżeli lewa strona jest mniejsza od sprawdzanej wartości targetu
                left = index + 1                        # to odrzucamy ten przedział, aktualizując lewy zakres na połowę pierwotnego
            else:                                       # jeżeli lewa strona nie jest mniejsza od sprawdzanej wartości targetu
                right = index                           # to odrzucamy prawą stronę

                                                        # czyli początkowy przedział l:0, i:500, r:1000; nasza wartość znajduje się w indeksie 260, więc odrzucamy prawą stronę
                                                        # i mamy wtedy przedział l:0, i:250, r:500, odrzucamy teraz analogicznie lewą stornę i mamy
                                                        # l:250, i:375, r:500  i tak dalej i tak dalej

    return None


random.seed(254279)                                 # ustawienie seed'a żeby zawsze generowały się takie same roboty (pomagało w testowaniu)
robots_database = robots()                          # utworzenie obiektu robot
vector = robots_database.generate_robots(1000)      # wygenerowanie zadanej liczby robotów
targets = [245, 420, 691, 239, 122]                 # wartości, których szukamy
# targets = ['R343Z6J28W','R3Z7Z4J38W','R3Z7Z6J222','R3Z7Z6J28W']
targets.sort()                                      # sortowanie wartości
# parameters :
# 0 - Id
# 1 - Type
# 2 - Mass       <50,2000>
# 3 - Range      <1,1000>
# 4 - Resolution <1,30>     
parameter = 2                                       # wybór parametru w którym szukamy wskazanych wartości
defaultSort(parameter)                              # funkcja sortująca pierwotną listę robotów wg zadanego parametru
print(binarySort(vector,targets,parameter))         # uruchomienie głównej funkcji i wyświetlenie wyników
# print(vector)
