class Vertex:
    def __init__(self, vertex_id, data):
        self.id = vertex_id
        self.data = data

    def __str__(self):
        return {"id": self.id, "data": self.data}

    def to_dict(self):
        return {"id": self.id, "data": self.data}

    def id_to_dict(self):
        return {"id": self.id}

    def add_data(self, key: str, value):
        self.data[key] = value

    def contains(self, query: str) -> bool:
        for key, value in self.data.items():
            if query.lower() in key.lower() or query.lower() in value.lower():
                return True
        return query.lower() in self.id.lower()
