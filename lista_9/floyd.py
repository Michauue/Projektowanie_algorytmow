from data import *

def floyd_warshall(G, a, b):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    for k in range(V):
        for i in range(V):
            for j in range(V):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print(distance[a][b])


floyd_warshall(G, 0, 4)