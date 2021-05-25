from collections import deque, namedtuple


inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    # sprawdzenie poprawności wpisanych krawędzi, muszą mieć długość 2 lub 3,
    # jeśli sperłniają warunek to tworzymy krawędź, jeśli nie to zwracamy błąd
    def __init__(self, edges):
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Niewłaściwe krawędzie: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    # wierzchołki naszego grafu, używamy set, ponieważ nie dopuszcza powtarzających się wartosci
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Źródło nie istnieje'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path


graph = Graph([
    (1, 2, 7),  (1, 3, 9),  (1, 6, 14), (2, 3, 10),
    (2, 4, 2), (3, 4, 11), (3, 6, 2),  (4, 5, 6),
    (5, 6, 9)])

print(graph.dijkstra(1, 5))