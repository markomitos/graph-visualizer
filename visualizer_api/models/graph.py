from models.edge import Edge
from models.vertex import Vertex
import re


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, vid, data=None):
        vertex = Vertex(vid, data)
        self.vertices.append(vertex)

    def add_edge(self, source_vid, target_vid, is_directed=False, weight=1, value=None):
        source_vertex = None
        target_vertex = None

        for vertex in self.vertices:
            if vertex.id == source_vid:
                source_vertex = vertex
            if vertex.id == target_vid:
                target_vertex = vertex

        if source_vertex is None:
            self.add_vertex(source_vid, {})
            source_vertex = self.get_vertex(source_vid)

        if target_vertex is None:
            self.add_vertex(target_vid, {})
            target_vertex = self.get_vertex(target_vid)

        edge = Edge(source_vertex, target_vertex, is_directed, weight, value)
        self.edges.append(edge)

    def get_neighbors(self, vid):
        neighbors = []
        for edge in self.edges:
            if edge.source.id == vid:
                neighbors.append(edge.target)
            elif not edge.is_directed and edge.target.id == vid:
                neighbors.append(edge.source)
        return neighbors

    def get_pointing_vertexes(self, vid):
        vertexes = []
        for edge in self.edges:
            if edge.source.id == vid:
                vertexes.append(edge.target)
        return vertexes

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
            tree.add_edge(source.id, target.id, weight=weight)

        return tree

    def get_vertex(self, key):
        for vertex in self.vertices:
            if vertex.id == key:
                return vertex
        return None

    def get_vertex_tree_info(self, key):
        info = {
            "vertex": None,
            "connections": []
        }
        for vertex in self.vertices:
            if vertex.id == key:
                info['vertex'] = vertex.to_dict()
        if info['vertex'] is not None:
            info['connections'] = list(map(lambda vertex: vertex.id, self.get_pointing_vertexes(key)))
        return info

    def add_data_to_vertex(self, vid, key, value):
        vertex = self.get_vertex(vid)
        if vertex:
            vertex.add_data(key, value)
        else:
            self.add_vertex(vid, {key: value})

    def search(self, query):
        result_graph = Graph()

        for vertex in self.vertices:
            if vertex.contains(query):
                result_graph.add_vertex(vertex.id, vertex.data)

        for edge in self.edges:
            if edge.source.contains(query) and edge.target.contains(query):
                result_graph.add_edge(edge.source.id, edge.target.id, edge.is_directed, edge.weight)

        return result_graph


    def filter_graph(self, filter_query):
        result_graph = Graph()

        try:
            matches = re.findall(r'<(.+?)>', filter_query)

            attribute, comparator, value = map(str.strip, matches)
            for vertex in self.vertices:
                if vertex.filter(attribute, comparator, value):
                    result_graph.add_vertex(vertex.id, vertex.data)

            for edge in self.edges:
                if (edge.source.filter(attribute, comparator, value)
                        and edge.target.filter(attribute, comparator, value)):
                    result_graph.add_edge(edge.source.id, edge.target.id, edge.is_directed, edge.weight)

        except ValueError:
            print("Invalid filter format. Please use this format: <attribute> <comparator> <value>")

        return result_graph


    def __str__(self):
        return {"nodes": [vertex.to_dict() for vertex in self.vertices], "links": [edge.to_dict() for edge in self.edges]}

    def to_dict(self):
        return {"nodes": [vertex.to_dict() for vertex in self.vertices], "links": [edge.to_dict() for edge in self.edges]}

    def ids_to_dicts(self):
        return {"nodes": [vertex.id_to_dict() for vertex in self.vertices], "links": [edge.to_dict() for edge in self.edges]}
