class Vertex:
    def __init__(self, vertex_id, data):
        self.id = vertex_id
        self.data = data

    def __str__(self):
        return f"Vertex ID: {self.id}, Data: {self.data}"