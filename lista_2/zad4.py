import networkx as nx
import matplotlib.pyplot as plt
import random


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

    def delete_repeats(self):
        for g in self.gdict:
            self.gdict[g][0] = list(set(self.gdict[g][0]))

    def add_node(self, node_number):
        if node_number not in self.gdict.keys():
            self.gdict[node_number] = [[], None]
        else:
            print("Istnieje już taki wierzchołek")

    def add_value(self, node, value):
        self.gdict[node][1] = value

    def nodes(self):
        return list(self.gdict.keys())

    def nodes_values(self):
        nodes_values = []
        for n in self.nodes():
            nodes_values.append(str(n) + ' ' + self.gdict[n][1])
        return nodes_values

    def value(self, node):
        return self.gdict[node][1]

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
        g = nx.relabel_nodes(g, dict(zip(g, self.nodes_values())))
        pos = nx.spring_layout(g)

        nx.draw_networkx_nodes(g, pos, node_size=500)
        nx.draw_networkx_labels(g, pos)
        nx.draw_networkx_edges(g, pos)
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


def usl(A):
    if not A:
        return
    else:
        g = A[0]
        for l in L:
            if not conflict(l, g):
                gallery.add_value(g, l)
                return usl(gallery.nodes_no_value())
        return print("Błąd dodania usług")


def conflict(l, node):
    for n in gallery.neighbours(node):
        if gallery.value(n) == l:
            return True
    return False


def rand_graph(num, min_neigh, max_neigh):
    temp_graph = {}
    for r in range(1, num + 1):
        temp_graph[r] = [[], None]
    gallery = graph(temp_graph)
    for x in temp_graph:
        temp_value = random.randint(min_neigh,max_neigh)
        for y in range(temp_value):
            random_value = random.randint(1,num)
            if len(temp_graph[x][0]) < temp_value:
                gallery.add_edge([x, random_value])
    gallery.delete_repeats()
    return gallery


graph_elements = {1: [[2, 3, 4, 5, 6, 7], None],
                  2: [[1, 3, 7], None],
                  3: [[1, 2, 4], None],
                  4: [[1, 3, 5], None],
                  5: [[1, 4, 6], None],
                  6: [[1, 5, 8, 9], None],
                  7: [[1, 2, 8], None],
                  8: [[7, 9], None],
                  9: [[6, 8], None],
                  }

num = 14
min_neigh = 2
max_neigh = 4
gallery = rand_graph(num, min_neigh, max_neigh)
L = ['a', 'b', 'c', 'd']

usl(gallery.nodes())
print(gallery.gdict)
gallery.draw_graph()
