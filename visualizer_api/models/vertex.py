import datetime

class Vertex:
    def __init__(self, vertex_id, data):
        self.id = vertex_id
        self.data = data

    def __str__(self):
        new_data = {}
        for key, value in self.data.items():
            if isinstance(value, datetime.date):
                new_data[key] = value.isoformat()
            else:
                new_data[key] = value
        return {"id": self.id, "data": new_data}

    def to_dict(self):
        new_data = {}
        for key,value in self.data.items():
            if isinstance(value, datetime.date):
                new_data[key] = value.isoformat()
            else:
                new_data[key] = value
        return {"id": self.id, "data": new_data}

    def id_to_dict(self):
        return {"id": self.id}

    def add_data(self, key: str, value):
        self.data[key] = value

    def contains(self, query: str) -> bool:
        for key, value in self.data.items():
            if query.lower() in key.lower() or query.lower() in value.lower():
                return True
        return query.lower() in self.id.lower()

    def filter(self, attribute, comparator, filter_value):
        if attribute in self.data:
            return self.apply_filter(self.data[attribute], comparator, filter_value)
        return False

    def apply_filter(self, attribute_value, comparator, filter_value):
        if comparator == '==':
            return attribute_value == filter_value
        elif comparator == '>':
            return attribute_value > filter_value
        elif comparator == '>=':
            return attribute_value >= filter_value
        elif comparator == '<':
            return attribute_value < filter_value
        elif comparator == '<=':
            return attribute_value <= filter_value
        elif comparator == '!=':
            return attribute_value != filter_value
        else:
            return False

