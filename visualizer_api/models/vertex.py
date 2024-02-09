from datetime import datetime,date

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
            if query.lower() in key.lower() or query.lower() in str(value).lower():
                return True
        return query.lower() in self.id.lower()

    def filter(self, attribute, comparator, filter_value):
        if attribute in self.data:
            return self.apply_filter(self.data[attribute], comparator, filter_value)
        return False

    def apply_filter(self, attribute_value, comparator, filter_value):
        if isinstance(attribute_value, int):
            filter_value = int(filter_value)
        elif isinstance(attribute_value, float):
            filter_value = float(filter_value)
        elif isinstance(attribute_value, date):
            filter_value = datetime.strptime(filter_value, '%Y-%m-%d').date()
        elif isinstance(attribute_value, datetime):
            filter_value = datetime.strptime(filter_value, '%Y-%m-%d')

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
