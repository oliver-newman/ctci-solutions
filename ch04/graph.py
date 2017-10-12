import random


class Graph:
    def __init__(self, directed=True):
        self.directed = directed
        self._adj_list = {}
        self.vertex_count = 0
        self.edge_count = 0

    def vertices(self):
        return self._adj_list.keys()

    def add_vertex(self, vertex):
        assert vertex not in self._adj_list

        self._adj_list[vertex] = set()
        self.vertex_count += 1

    def add_edge(self, source, dest):
        assert dest in self._adj_list

        self._adj_list[source].add(dest)
        if not self.directed:
            self._adj_list[dest].add(source)

        self.edge_count += 1

    def out_neighbors(self, vertex):
        return self._adj_list[vertex]

    def in_neighbors(self, vertex):
        assert vertex in self._adj_list   

        return {v for v in self._adj_list if vertex in self._adj_list[v]}

    @classmethod
    def random(cls, n=100, p=0.5, directed=True):
        graph = cls(directed)

        for i in range(n):
            graph.add_vertex(i)

        for v1 in graph.vertices():
            for v2 in graph.vertices():
                if random.random() < p:
                    graph.add_edge(v1, v2)

        return graph
