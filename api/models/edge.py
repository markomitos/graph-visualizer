class Edge:
    def __init__(self, source, target, is_directed=False, weight=1):
        self.source = source
        self.target = target
        self.is_directed = is_directed
        self.weight = weight

    def __str__(self):
        directed_str = "Directed" if self.is_directed else "Undirected"
        return f"Edge: {self.source} {'->' if self.is_directed else '<->'} {self.target}, {directed_str}, Weight: {self.weight}"

    def is_adjacent(self, vertex):
        return self.source == vertex or (not self.is_directed and self.target == vertex)

    def reverse(self):
        if not self.is_directed:
            raise ValueError("Cannot reverse an undirected edge")
        self.source, self.target = self.target, self.source