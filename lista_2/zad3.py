import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import copy


class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def add_edge(self, edge):
        if edge[0] == edge[1]:
            return
        edge = set(edge)
        (v1, v2) = tuple(edge)
        if v1 in self.gdict and v2 in self.gdict:
            self.gdict[v1][0].append(v2)
            self.gdict[v2][0].append(v1)
        elif v1 in self.gdict:
            self.gdict[v1][0].append(v2)
            self.gdict[v2] = [[v1], None]
        elif v2 in self.gdict:
            self.gdict[v2][0].append(v1)
            self.gdict[v1] = [[v2], None]

    def add_node(self, node):
        if node not in self.gdict.keys():
            self.gdict[node] = [[], rand_position()]
        else:
            print("Istnieje już taki wierzchołek")

    def remove_node(self, node):
        self.gdict[node][0] = []
        for g in self.gdict:
            self.gdict[g][0] = list(set(self.gdict[g][0]) - {node})

    def delete_repeats(self):
        for g in self.gdict:
            self.gdict[g][0] = list(set(self.gdict[g][0]))

    def change_position(self, node, value):
        self.gdict[node][1] = value

    def nodes(self):
        return list(self.gdict.keys())

    def node_position(self, node):
        return self.gdict[node][1]

    def position(self):
        position = {}
        for n in self.gdict:
            position[n] = self.node_position(n)
        return position

    def edges(self):
        edges = []
        for keys in self.gdict:
            for values in self.gdict[keys][0]:
                if {values, keys} not in edges:
                    edges.append({values, keys})
        return edges

    def neighbours(self, node):
        return self.gdict[node][0]

    def draw_graph(self):
        g = nx.Graph()
        g.add_nodes_from(self.nodes())
        g.add_edges_from(self.edges())
        nx.draw_networkx_nodes(g, self.position(), node_size=500)
        nx.draw_networkx_labels(g, self.position())
        nx.draw_networkx_edges(g, self.position())
        plt.show()

    def nodes_no_value(self):
        nodes = []
        for v in self.gdict:
            if self.gdict[v][1] is None:
                nodes.append(v)
        return nodes

    def nodes_with_value(self):
        nodes = []
        for v in self.gdict:
            if self.gdict[v][1] is not None:
                nodes.append(v)
        return nodes


def rand_position():
    return [random.randint(0, 25), random.randint(0, 25)]


def rand_graph(num, min_neigh, max_neigh):
    temp_graph = {}
    for r in range(1, num + 1):
        temp_graph[r] = [[], rand_position()]
    gallery = graph(temp_graph)
    for x in temp_graph:
        temp_value = random.randint(min_neigh, max_neigh)
        for y in range(temp_value):
            random_value = random.randint(1, num)
            if len(temp_graph[x][0]) < temp_value:
                gallery.add_edge([x, random_value])
    gallery.delete_repeats()
    return gallery


def e_dist(v, w):
    return math.sqrt((v[0] - w[0]) ** 2 + (v[1] - w[1]) ** 2)


def dist(v, w, g):
    if w in g.neighbours(v):
        path = [v, w]
        return e_dist(g.node_position(v), g.node_position(w)), path
    else:
        temp_neighbours = g.neighbours(v)
        if not temp_neighbours:
            return math.inf , []
        temp_position = g.node_position(v)
        counter = {}
        g.remove_node(v)
        for n in temp_neighbours:
            ndist = dist(n, w, g)
            totaldist = e_dist(temp_position, g.node_position(n)) + ndist[0]
            path = [v] + ndist[1]
            counter[totaldist] = path
        return [min(counter), counter[min(counter)]]


graph_elements = {1: [[2, 3, 4, 5, 6, 7], [0, 10]],
                  2: [[1, 3, 7], [7, 16]],
                  3: [[1, 2, 4], [5, 21]],
                  4: [[1, 3, 5], [1, 3]],
                  5: [[1, 4, 6], [7, 10]],
                  6: [[1, 5, 8, 9], [12, 2]],
                  7: [[1, 2, 8], [15, 15]],
                  8: [[7, 9], [5, 5]],
                  9: [[6, 8], [0, 0]],
                  }

random.seed(254295)
num = 10
min_neigh = 1
max_neigh = 3

g = rand_graph(num, min_neigh, max_neigh)
# g = graph(graph_elements)



print(dist(8, 1, copy.deepcopy(g)))
g.draw_graph()
