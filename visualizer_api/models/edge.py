class Edge:
    def __init__(self, source, target, is_directed=False, weight=1, value=None):
        self.source = source
        self.target = target
        self.is_directed = is_directed
        self.weight = weight
        self.value = value

    def __str__(self):
        return {
            "source": self.source.id,
            "target": self.target.id,
            "value": self.value,
            "directed": self.is_directed
        }

    def is_adjacent(self, vertex):
        return self.source == vertex or (not self.is_directed and self.target == vertex)

    def reverse(self):
        if not self.is_directed:
            raise ValueError("Cannot reverse an undirected edge")
        self.source, self.target = self.target, self.source

    def to_dict(self):
        return {
            "source": self.source.id,
            "target": self.target.id,
            "value": self.value,
            "directed": self.is_directed
        }