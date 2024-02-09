from models.graph import Graph


class Workspace:
    def __init__(self, name: str):
        self.data_source = "XML Data Source"
        self.visualizer = "Simple Visualizer"
        self.current_graph = Graph()
        self.current_filters = []
        self.current_search = []
        self.name = name
        self.data_filepaths = {
            "XML Data Source": "C:\\Users\\ComTech\\pycharm-projects\\graph-visualizer\\xml_data_source\\xml_data_source\\persons.xml",
            "RDF Data Source": "C:\\Users\\ComTech\\pycharm-projects\\graph-visualizer\\rdf_data_source\\rdf_data_source\\beatles.nt"
        }