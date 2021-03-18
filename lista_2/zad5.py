import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math

N = 200  # N x K wymiary planszy
K = 200
D = 10  # odległość między rysowanymi punktami
S = 45  # minimalna odleglosc między odwiertami
R = 10  # liczba odwiertów

G = nx.Graph()
VxPoints = np.arange(0, N + 1, D)
VyPoints = np.arange(0, K + 1, D)
count_nodes = math.floor(len(VxPoints) * len(VyPoints))

Gpos = {}
x_index = 0
y_index = 0
for node in range(count_nodes):
    G.add_node(node)
    x = VxPoints[x_index]
    y = VyPoints[y_index]
    x_index += 1
    if x_index == len(VxPoints):
        x_index = 0
        y_index += 1
    Gpos[node] = [x, y]

H = nx.Graph()

for h in range(R):
    H.add_node(h)

nodesArr = []
for node in H.nodes():
    nodesArr.append(node)

Hpos = {}
temp = True


def drillsPositions():
    temp = True
    count_rows = 1
    for node in H.nodes():
        if node == 0:
            x_pos, y_pos = 0, 0
            Hpos[node] = [x_pos, y_pos]
        else:
            y_pos = Hpos[node - 1][1]
            if temp:
                x_pos = Hpos[node - 1][0] + S
                while x_pos % D != 0:
                    x_pos += 1
                if x_pos > N:
                    temp = False
                    count_rows += 1
                    x_pos = 150
                    y_pos += S
                    while y_pos % D != 0:
                        y_pos += 1
            else:
                x_pos = Hpos[node - 1][0] - S
                while x_pos % D != 0:
                    x_pos -= 1
                if x_pos < 0:
                    temp = True
                    count_rows += 1
                    x_pos = 0
                    y_pos += S
                    while y_pos % D != 0:
                        y_pos += 1

            if y_pos > K:
                print("Błąd")
            Hpos[node] = [x_pos, y_pos]
    free_row = []
    for currentRow in range(count_rows - 1):
        yNodesArr = []
        for yNodes in Hpos:
            if Hpos[yNodes][1] not in yNodesArr:
                yNodesArr.append(Hpos[yNodes][1])
        free_row.append(yNodesArr[currentRow])
        for node in reversed(nodesArr):
            if Hpos[node][1] not in free_row:
                Hpos[node][1] += D
                if Hpos[node][1] > K:
                    print('Za duzo odwiertów!')
                    Hpos[node][1] -= D
                    return


drillsPositions()
print(Hpos)
HposFinal = Hpos

nx.draw(G, Gpos, node_size=100, with_labels=False, node_color='brown')
nx.draw(H, HposFinal, node_size=50, with_labels=False, node_color='yellow')
plt.show()
