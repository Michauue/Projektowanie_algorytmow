from data import *
import random
import time

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def vertexUnion(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruksalAlgorithm(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        print("\nEdge - Weight")
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            # parent - tablica wierzchołków
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.vertexUnion(parent, rank, x, y)
        for u, v, weight in result:
            print(u, '<->', v, '-', weight)
            time.sleep(0.5)

random.seed(254279)
r = 3*V
g = Graph(V)
comp_tab = []
comp_tab_a = []
comp_tab_b = []
for z in range(0,r):
    a = random.randint(0,V-1)
    b = random.randint(0,V-1)
    while a == b:
        b = random.randint(0,V-1)
    c = random.randint(1,2*V)
    if [a,b] not in comp_tab and [b,a] not in comp_tab:
        g.add_edge(a, b, c)
        comp_tab.append([a,b])

print(comp_tab)
print(g.graph)
g.kruksalAlgorithm()