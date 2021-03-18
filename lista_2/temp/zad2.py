import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import numpy as np

random.seed(254279)

G = nx.Graph()
howManyNodes = 10
for x in range(howManyNodes):
    G.add_node(x)

Gpos = {}
for V in G.nodes():
    value = [random.randint(0, 101), random.randint(0, 101)]
    Gpos[V] = value

positions = []
for pos1 in Gpos:
    for pos2 in Gpos:
        pos1x, pos1y = Gpos[pos1][0], Gpos[pos1][1]
        pos2x, pos2y = Gpos[pos2][0], Gpos[pos2][1]
        euklid = pow(pow(pos1x - pos2x, 2) + pow(pos1y - pos2y, 2), 0.5)
        positions.append(euklid)

print(positions)
print(len(positions))
print()

whichV = []
for n in range(0, 91, 10):
    orderInV = []
    partOfPosition = positions[n: n + 10]
    partOfPositionASC = sorted(partOfPosition)
    for j in range(10):
        order = partOfPosition.index(partOfPositionASC[j])
        orderInV.append(order)
    whichV.append(orderInV)

print(whichV)
print('\n')

visitedV = [0]
G.add_edge(0, 0)

edgesToAdding = []

for i in G.nodes():
    if i == 0:
        pass
    else:
        for j in range(9):
            index = whichV[i][j + 1]
            if index in visitedV:
                visitedV.append(i)
                edgesToAdding.append([i, index])
                break

labelsInTime = {}
number = 0


def animate(x):
    global number
    first = edgesToAdding[number][0]
    second = edgesToAdding[number][1]

    G.add_edge(first, second)
    label = str(round(np.sqrt((Gpos[first][0] - Gpos[second][0]) ** 2 + (Gpos[first][1] - Gpos[second][1]) ** 2), 2))
    G.add_weighted_edges_from([(first, second, label)])
    labels = nx.get_edge_attributes(G, 'weight')
    labelsKeys = []
    for elem in labels:
        labelsKeys.append(elem)

    labelIndex = labelsKeys[number]
    labelsInTime[labelIndex] = labels[labelIndex]

    nx.draw(G, Gpos, with_labels=True)
    nx.draw_networkx_edge_labels(G, Gpos, edge_labels=labelsInTime)
    number += 1
    if number == 9:
        number = 0


ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.show()
