import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import time


def rand_position():
    return [random.randint(0, 100), random.randint(0, 100)]


def graph(num):
    for i in range(1, num + 1):
        V.append(i)
        v_pos[i] = rand_position()


def E_distance(v1, v2):
    return math.sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2)


def min_distance(conn, v):
    temp_min = math.inf
    min_id = 0
    for i in conn:
        value = E_distance(v_pos[v], v_pos[i])
        if value < temp_min:
            temp_min = value
            min_id = i
    return min_id, round(temp_min,2)


def spanning_tree():
    E.append((V[0], V[0]))
    labels[(V[0], V[0])] = 0
    connected = [V[0]]
    for v in V[1:]:
        e_dist = min_distance(connected, v)
        E.append((v, e_dist[0]))
        labels[(v, e_dist[0])] = e_dist[1]
        connected.append(v)


def fast_draw():
    g.add_nodes_from(V)
    g.add_edges_from(E)
    nx.draw_networkx_nodes(g, v_pos, node_size=600)
    nx.draw_networkx_labels(g, v_pos)
    nx.draw_networkx_edges(g, v_pos)
    nx.draw_networkx_edge_labels(g, v_pos, edge_labels=labels)
    plt.show()


def slow_draw():
    for x in V:
        g.add_node(x)
        nx.draw_networkx_nodes(g, v_pos, node_size=600, node_color='pink')
        nx.draw_networkx_labels(g, v_pos)
        plt.draw()
        plt.pause(0.1)
        plt.clf()
    plt.draw()
    temp_labels = {}
    for y in E:
        temp_labels[y] = labels[y]
        g.add_edge(*y)
        nx.draw_networkx_nodes(g, v_pos, node_size=600, node_color='pink')
        nx.draw_networkx_labels(g, v_pos)
        nx.draw_networkx_edges(g, v_pos)
        nx.draw_networkx_edge_labels(g, v_pos, edge_labels=temp_labels)
        plt.draw()
        plt.pause(0.1)
        plt.clf()
    time.sleep(20)


random.seed(254279)
V = []
E = []
v_pos = {}
labels = {}
num = 20

graph(num)
spanning_tree()
g = nx.Graph()
#slow_draw()  #rysowanie krok po kroku
fast_draw() #rysowanie szybkie