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
    # wierzchołki naszego grafu, używamy set, ponieważ nie dopuszcza powtarzających się wartości
    def vertices(self):
        return set(sum(([edge.start, edge.end] for edge in self.edges), []))

    @property
    def neighbours(self):
        # ustawiamy sąsiadów dla każdego wierzchołka
        neighbours = {vertex: set() for vertex in self.vertices}
        # jeżeli istnieje połączenie między wierzchołkami to zapisujemy go w tablicy sąsiadów z odpowiadającym mu kosztem
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))
        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Źródło nie istnieje'
        # ustawiamy odległośc jako inf dla każdego wierzchołka
        distances = {vertex: inf for vertex in self.vertices}
        # zaczynamy od zerwoania odwiedzonych wierzchołków
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        # początkowy dystans
        distances[source] = 0
        vertices = self.vertices.copy()
        while vertices:
            # szukamy wierzchołka do którego mamy połącznie i koszt jest najmniejszy i usuwamy go, ponieważ użyliśmy go do zbudowania naszej drogi
            current_vertex = min(vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            # jeśli dystans wynosi inf to przerywamy działanie pętli
            if distances[current_vertex] == inf:
                break
            # przechodzimy po sąsiadach badanego obecnie wierzchołka i szukamy alternatywnej ścieżki
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                # jeżeli ścieżka taka istnieje i jest krótsza od obecnie badanej to ją podmieniamy
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    # zmieniamy None na obecny węzeł jako poprzednie węzły
                    previous_vertices[neighbour] = current_vertex
        # tworzymy ścieżkę którą później wyświetlamy jako efekt działania programu (dest to wierzchołek, do którego chcemy dojść)
        path, current_vertex = deque(), dest
        # przechodzimy po zapisanych wierzchołkach, póki nie mają wartości None
        while previous_vertices[current_vertex] is not None:
            # jeżeli mamy zapisany wierzchołek to dodajemy go do ścieżki i zmieniamy badany wierzchołek na nowy - kolejny na naszej liście
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        # jeżeli ścieżka istnieje to dopisujemy ostatni wierzchołek (ten z którego droga ma startować)
        if path:
            path.appendleft(current_vertex)
        # odczytywanie sumarycznego dystansu między wierzchołkami
        route = list(path)
        dist = 0
        for i in range(len(route)-1):
            for j in range(len(self.edges)):
                if self.edges[j].start == route[i] and self.edges[j].end == route[i+1]:
                    dist += self.edges[j].cost
        return route, dist


graph = Graph([
    (1, 2, 7),  (1, 3, 9),  (1, 6, 14), (2, 3, 10),
    (2, 4, 2), (3, 4, 11), (3, 6, 2),  (4, 5, 6),
    (5, 6, 9), (4, 2, 4)])

print('([Path], distance)\n',graph.dijkstra(4,3))