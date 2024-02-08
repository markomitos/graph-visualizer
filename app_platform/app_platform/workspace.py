from models.graph import Graph


class Workspace:
    def __init__(self, name: str):
        self.data_source = "XML Data Source"
        self.visualizer = "Simple Visualizer"
        self.current_graph = Graph()
        self.current_filters = []
        self.current_search = []
        self.name = name

