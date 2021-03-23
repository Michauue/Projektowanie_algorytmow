from math import sqrt

VV = [1, 2, 3, 4, 5]
WW = [(1, 2), (2, 3), (3, 4), (4, 5), (3, 1), (3, 5)]
Vx = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
Vy = {1: 0, 2: 1, 3: 0, 4: -1, 5: 0}


def dist(v, w):
    list = []
    if (v, w) in WW:
        list.append(v)
        list.append(w)
        return [sqrt((Vx[v] - Vx[w]) ** 2 + (Vy[v] - Vy[w]) ** 2), list]
    else:
        S = []
        for s in VV:
            if (v, s) in WW:
                S.append(s)
        distance = {}
        for s in S:
            dvs = sqrt((Vx[v] - Vx[s]) ** 2 + (Vy[v] - Vy[s]) ** 2)
            temp = (dist(s, w)[1])
            temp.insert(0, v)
            distance[dist(s, w)[0] + dvs] = temp
        return [min(distance), temp]


print(dist(1, 4))
