from typing import List
from collections import defaultdict

class Graph:
    def __init__(self, vertices: List[int], edges: List[List[int]]):
        self.vertices = vertices
        self.edges = edges
        self.adj_list = defaultdict(list)
        self.fill_adj_list()

    def fill_adj_list(self):
        for u, v in self.edges:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

class Isomorphism:
    def __init__(self, isomorphic_graph: Graph):
        self.isomorphic_graph = isomorphic_graph
        self.general = False

    def change_vertices_names(self, graph: Graph):
        initial_vertices = graph.vertices

        if len(graph.edges) != len(self.isomorphic_graph.edges):
            return
        else:
            for edge in graph.edges:
                edge[0] = self.get_vertex_name(edge[0], initial_vertices)
                edge[1] = self.get_vertex_name(edge[1], initial_vertices)

    def get_vertex_name(self, vertex: int, initial_vertices: List[int]) -> int:
        return self.isomorphic_graph.vertices[initial_vertices.index(vertex)]

    def anti_flex(self, graph: Graph, m: int):
        if m == 0:
            if self.isomorphic_graph.__dict__ == graph.__dict__:
                self.general = True
        else:
            for i in range(m+1):
                self.anti_flex(graph, m-1)
                if i < m:
                    graph.vertices[i], graph.vertices[m] = graph.vertices[m], graph.vertices[i]
                    self.reverse(graph, m-1)

    def reverse(self, graph: Graph, m: int):
        i, j = 0, m
        while i < j:
            graph.vertices[i], graph.vertices[j] = graph.vertices[j], graph.vertices[i]
            i += 1
            j -= 1

def is_isomorphic(graph1: Graph, graph2: Graph) -> bool:
    if len(graph1.vertices) != len(graph2.vertices):
        return False

    isomorphic = Isomorphism(graph2)
    isomorphic.change_vertices_names(graph1)

    if not isomorphic.general:
        isomorphic.anti_flex(graph1, len(graph1.vertices)-1)

    return isomorphic.general

# Example usage
vertices1 = [1, 2, 3, 4]
edges1 = [[1, 2], [2, 3], [3, 4], [4, 1]]
graph1 = Graph(vertices1, edges1)

vertices2 = [5, 6, 7, 8]
edges2 = [[5, 6], [6, 7], [7, 8], [8, 5]]
graph2 = Graph(vertices2, edges2)

print(is_isomorphic(graph1, graph2))  # True, both graphs are isomorphic