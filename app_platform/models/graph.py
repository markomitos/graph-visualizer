from app_platform import Edge
from app_platform import Vertex


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, vid, data=None):
        vertex = Vertex(vid, data)
        self.vertices.append(vertex)

    def add_edge(self, source_vid, target_vid, is_directed=False, weight=1):
        source_vertex = None
        target_vertex = None

        for vertex in self.vertices:
            if vertex.vid == source_vid:
                source_vertex = vertex
            if vertex.vid == target_vid:
                target_vertex = vertex

        if source_vertex is None or target_vertex is None:
            raise ValueError("Source or target vertex not found")

        edge = Edge(source_vertex, target_vertex, is_directed, weight)
        self.edges.append(edge)

    def get_neighbors(self, vid):
        neighbors = []
        for edge in self.edges:
            if edge.source.vid == vid:
                neighbors.append(edge.target)
            elif not edge.is_directed and edge.target.vid == vid:
                neighbors.append(edge.source)
        return neighbors

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(self):
        result = []

        # Sort edges by weight
        sorted_edges = sorted(self.edges, key=lambda edge: edge.weight)

        parent = {}
        rank = {}

        for vertex in self.vertices:
            parent[vertex] = vertex
            rank[vertex] = 0

        i = 0
        e = 0

        while e < len(self.vertices) - 1:
            source, target, weight = sorted_edges[i]
            i += 1

            source_parent = self.find(parent, source)
            target_parent = self.find(parent, target)

            if source_parent != target_parent:
                e += 1
                result.append((source, target, weight))
                self.union(parent, rank, source_parent, target_parent)

        return result

    def convert_to_tree(self):
        tree_edges = self.kruskal()

        tree = Graph()
        for source, target, weight in tree_edges:
            tree.add_edge(source.vid, target.vid, weight=weight)

        return tree

    def __str__(self):
        result = "Vertices:\n"
        for vertex in self.vertices:
            result += f"{vertex.vid}: {vertex.data}\n"

        result += "\nEdges:\n"
        for edge in self.edges:
            result += f"{edge.source.vid} {'->' if edge.is_directed else '<->'} {edge.target.vid}, Weight: {edge.weight}\n"

        return result