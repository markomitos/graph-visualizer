class Vertex:
    def __init__(self, vertex_id, data):
        self.id = vertex_id
        self.data = data

    def __str__(self):
        return {"id": self.id, "data": self.data}

    def to_dict(self):
        return {"id": self.id, "data": self.data}