import time
from data import *

selected = [0, 0, 0, 0, 0]

e = 0
# ilość krawędzi zawsze będzie o jeden mniejsza niż ilość wierzchołków, więc pierwszą wartość możemy podmienić na TRUE
selected[0] = True
print("\nEdge - Weight")
while (e < V - 1):
    # szukamy najbliższego wierzchołka płączonego z wierzchołkiem początkowym
    minimum = INF
    x = 0
    y = 0
    # ustawione wartości początkowe i przechodzimy po sąsiadach
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):  
                    # jeżeli krawędź istnieje i nie jest już wybrana to działamy dalej sprawdzając minimalną odległość
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x), "<->", str(y), "-", str(G[x][y]))
    time.sleep(0.5)
    selected[y] = True
    e += 1