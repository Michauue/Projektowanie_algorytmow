class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)


    def searchingBFSAlgorithm(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False


    def fordFulkerson(self, source, dest):
        parent = [-1] * (self.ROW)
        max_flow = 0
        all_path = []
        i = 0

        while self.searchingBFSAlgorithm(source, dest, parent):

            path_flow = float("Inf")
            s = dest
            all_path.append([])
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                
                all_path[i].insert(0,s)
                
                s = parent[s]
            all_path[i].insert(0,source)
            all_path[i].append('Path flow: '+str(path_flow))
            i += 1
            
            # Dodanie szukanej ścieżki przepływu
            max_flow += path_flow
            

            # Aktualizowanie wartości krawędzi
            v = dest
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

            summary_flow = 'Summary flow from ' + str(source) + ' to ' + str(dest) + ' is ' + str(max_flow)
        return summary_flow, all_path


graph = [[0, 5, 7, 0, 3, 0],
         [0, 0, 9, 0, 0, 0],
         [0, 5, 0, 0, 7, 4],
         [0, 0, 0, 0, 0, 5],
         [0, 2, 7, 4, 0, 0],
         [0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0
dest = 1
edges = []

for i in range(len(graph)):
    for d in range(len(graph[i])):
        v = graph[i][d]
        if v > 0:
            print(i, '->', d, '=', v)
            edges.append([i,d])
# print(edges)

# random.seed(21)
# G = nx.Graph()
# G.add_nodes_from([0,1,2,3,4,5])
# G.add_edges_from(edges)
# nx.draw(G,with_labels=True)
# uklad=nx.random_layout(G)
# nx.draw_networkx_edge_labels(G, uklad)
# plt.show()

print("Max Flow:",g.fordFulkerson(source, dest))
