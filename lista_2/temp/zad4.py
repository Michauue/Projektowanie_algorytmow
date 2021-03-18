import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import math

howManyGaleries = 10

G = nx.Graph()
Gpos = {}

for x in range(howManyGaleries):
    G.add_node(x)

for node in G.nodes():
    value = [random.randint(0,101), random.randint(0,101)]
    Gpos[node] = value


def usl(A, B):
    print(f'\nmainA: {mainA}')
    print(f'mainB: {mainB}')
    g = random.choice(A)
    print(f'g: {g}')
    gL = random.choice(L)
    print(f'gL: {gL}')
    neighbors = []
    for elemA in fullMainA:
        xg, yg, xElem, yElem = Gpos[g][0], Gpos[g][1], Gpos[elemA][0], Gpos[elemA][1]
        label = np.sqrt((xg - xElem) ** 2 + (yg - yElem) ** 2)
        print(label)
        if elemA == g:
            label = 100
        if label < neighborDistans and elemA in B:
            neighbors.append(elemA)
    print(f'neighbors: {neighbors}')
    if len(neighbors) != 0:
        print(f'gl with neighbors : {gL}')
        leftL = L.copy()
        for neighbor in neighbors:
            G.add_weighted_edges_from([(g, neighbor, '')])
            if B[neighbor] != gL:
                print(f'Inne   : {B[neighbor]} i {gL} dla {neighbor}')
                if B[neighbor] in leftL:
                    print(f'Bylo {gL} w leftL: {leftL}')
                    try:
                        leftL.remove(B[neighbor])
                    except IndexError:
                        print('IndexError("Cannot choose from an empty sequence") from None')
                        print('Nie da się ułożyć takiego planu dla tej mapy')
                        return 'Nie da się ułożyć takiego planu dla tej mapy'

            if B[neighbor] == gL:
                print(f'To samo: {B[neighbor]} i {gL} dla {neighbor}')
                try:
                    leftL.remove(gL)
                    gL = random.choice(leftL)
                except IndexError:
                    print('IndexError("Cannot choose from an empty sequence") from None')
                    print('Nie da się ułożyć takiego planu dla tej mapy')
                    return False
        mainB[g] = gL
    else:
        print(f'gl without neighbors : {gL}')
        mainB[g] = gL

    mainA.remove(g)

    if len(mainA) != 0:
        usl(mainA, mainB)


L = ['l1', 'l2', 'l3', 'l4']
# L = ['l1', 'l2', 'l3']
mainA = []
for elem in G.nodes():
    mainA.append(elem)
fullMainA = mainA.copy()
mainB = {}
neighborDistans = 40

usl(mainA, mainB)
print(f'\nFinal mainA: {mainA}')
print(f'Final mainB: {mainB}')

color_map = []
if len(mainA) == 0:
    for node in G:
        if mainB[node] == 'l1':
            color_map.append('blue')
        if mainB[node] == 'l2':
            color_map.append('red')
        if mainB[node] == 'l3':
            color_map.append('yellow')
        if mainB[node] == 'l4':
            color_map.append('green')

nx.draw(G, Gpos, with_labels=True, node_color=color_map)
# nx.draw(G, Gpos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, Gpos, edge_labels=labels)
plt.show()