import random
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation


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


def swap(A, i, j):
    if i != j:
        A[i], A[j] = A[j], A[i]

def bubblesort(A):

    if len(A) == 1:
        return
    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            yield A


def quicksort(A, start, end):
    if start >= end:
        return
    pivot = A[end]
    pivotIdx = start
    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap(A, end, pivotIdx)
    yield A

    yield from quicksort(A, start, pivotIdx - 1)
    yield from quicksort(A, pivotIdx + 1, end)


# def quickSort(data):

#     less = []
#     equal = []
#     greater = []

#     if len(data) > 1:
#         pivot = data[0]
#         for x in data:
#             if x < pivot:
#                 less.append(x)
#             elif x == pivot:
#                 equal.append(x)
#             elif x > pivot:
#                 greater.append(x)
#         final = quickSort(less)+equal+quickSort(greater)
#         return final 
#     else:
#         return data


# def sillySort(data):
#     n = len(data)
#     i = 0
#     while i < n - 1:
#         if data[i] > data[i+1]:
#             temp = data[i]
#             data[i] = data[i+1]
#             data[i+1] = temp
#             i = 0
#             continue
#         i += 1
#     return data


random.seed(254279)
robots_database = robots()
vector = robots_database.generate_robots(50)

parameter = 'resolution'

df = pd.DataFrame(vector, columns=['id','type','mass','range','resolution'])
L = df[parameter].tolist()

data = L.copy()
print(L)
# generator_1 = quicksort(data,0,len(data)-1)
generator_2 = bubblesort(data)

# title_1 = 'quick'
title_2 = 'bubble'

fig, ax = plt.subplots()
ax.set_title(title_2)
bar_rects = ax.bar(range(len(data)), data, align="edge")
ax.set_xlim(0, len(data))
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
iteration = [0]
def update_fig(A, rects, iteration):
    for rect, val in zip(rects, A):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text("# of operations: {}".format(iteration[0]))

anim = FuncAnimation(fig, func=update_fig,
    fargs=(bar_rects, iteration), frames=generator_2, interval=1,
    repeat=False)
plt.show()