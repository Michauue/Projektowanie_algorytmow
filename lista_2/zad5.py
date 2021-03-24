import matplotlib.pyplot as plt
import math
import copy
import numpy as np


def e_dist(v, w):
    return math.sqrt((v[0] - w[0]) ** 2 + (v[1] - w[1]) ** 2)


def holes(N, K, D):
    holes = {}
    for d in range(int(K / D) + 1):
        for p in range(int(N / D) + 1):
            holes[(D * d, D * p)] = False
    return holes


def plot_net(N, K, D):
    for y in range(int(K / D) + 1):
        plt.plot([y * D, y * D], [0, N], 'k:')
    for x in range(int(N / D) + 1):
        plt.plot([K, 0], [x * D, x * D], 'k:')


def plot_holes(N, K, D, b):
    for d in range(int(K / D) + 1):
        for p in range(int(N / D) + 1):
            if (D * d, D * p) in b:
                if b[(D * d, D * p)]:
                    plt.plot([D * d], [D * p], 'ro')
                else:
                    plt.plot([D * d], [D * p], 'ko')
            else:
                print("Brak wierzchołka")
    plt.show()


def boreholes(S, R, all_b):
    not_used_b = copy.copy(all_b)
    used_b = [(0, 0)]
    not_used_b.pop((0, 0))
    all_b[0, 0] = True
    counter = 1
    for x in range(R - 1):
        if not_used_b:
            h = max_dist(not_used_b.keys(), used_b, S)
            if h == ():
                break
            used_b.append(h)
            counter += 1
            not_used_b.pop(h)
            all_b[h] = True
        else:
            break
    print(counter)
    return all_b


def max_dist(not_used_b, used_b, S):
    temp_min_dist = 0
    temp_b = ()
    for x in not_used_b:
        temp_dist = []
        control = False
        for z in used_b:
            if e_dist(z, x) < S:
                control = True
                break
            else:
                temp_dist.append(e_dist(z, x))
        if control:
            continue
        temp_min = np.min(temp_dist)
        if temp_min > temp_min_dist:
            temp_min_dist = temp_min
            temp_b = x
    return temp_b


N, K = (100, 60)
D = 4
S = 5
R = 160
all_b = holes(N, K, D)
b = boreholes(S, R, all_b)
plot_net(N, K, D)
plot_holes(N, K, D, b)
