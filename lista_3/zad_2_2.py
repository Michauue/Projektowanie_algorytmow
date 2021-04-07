import math
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt


def starter(p, xd):
    global tab
    tab = []
    czp(p, xd)
    return tab


def czp(p, xd):
    if p < 2:
        return tab
    tab.append(p)
    for i in range(2, xd + 1):
        if p % i == 0:
            tab.pop()
            tab.append(i)
            czp(int(p / i), xd)
            break
    return tab


def xd(p):
    xd = int(math.floor(math.sqrt(p)))
    return xd


def pczp(a):
    xd_a = xd(a)
    tab_a = czp(a, xd_a)
    return tab_a


def aczp(a, b):
    xd_a = xd(a)
    xd_b = xd(b)
    tab_a = starter(a, xd_a)
    tab_b = starter(b, xd_b)
    len_a = len(tab_a)
    len_b = len(tab_b)
    temp_tab = []
    for i in range(0, len_a):
        for j in range(0, len_b):
            if tab_a[i] == tab_b[j]:
                temp_tab.append(tab_b[j])
                tab_b.remove(tab_b[j])
                len_b -= 1
                break
    result = 1
    for i in range(0, len(temp_tab)):
        result = result * temp_tab[i]

    return result


def aeuc(x, y):
    if y == 0:
        return x
    else:
        return aeuc(y, x % y)


def indeks_merge(a, b):
    x = []
    for i in range(6):
        x.append(a[i] * b[i])
    return np.prod(x)


def time_testing(indeks_merge):
    timelist_aczp = []
    timelist_aeuc = []
    start = timer()
    i = 1
    while timer() - start < 5:
        start_aczp = timer()
        aczp(indeks_merge, i)
        timelist_aczp.append(timer() - start_aczp)

        start_aeuc = timer()
        aeuc(indeks_merge, i)
        timelist_aeuc.append(timer() - start_aeuc)
        i += 1
    return timelist_aczp, timelist_aeuc


def plot_timetable(timelist_aczp, timelist_aeuc):
    plt.subplot(2, 1, 1)
    plt.plot(timelist_aczp, color='r')
    plt.subplot(2, 1, 2)
    plt.plot(timelist_aeuc, color='c')
    plt.show()


indeks1 = [2, 5, 4, 2, 7, 9]
indeks2 = [2, 5, 4, 2, 7, 9]
timelist_aczp, timelist_aeuc = time_testing(indeks_merge(indeks1, indeks2))
plot_timetable(timelist_aczp, timelist_aeuc)
