from visualizer_api.data_source_api import DataSourceBase
from models.graph import Graph


class RdfDataSource(DataSourceBase):

    # def __init__(self):
    #     pass
    def __init__(self, rdf_file: str):
        self.rdf_file = rdf_file

    def name(self) -> str:
        return 'RDF Data Source'

    def fetch_data(self) -> Graph:
        graph = Graph()
        self.parse_nt_file(self.rdf_file, graph)
        print("Print from rdf_data_source")
        return graph

    def parse_nt_file(self, file_path: str, graph: Graph):
        with open(file_path, 'r') as file:
            for line in file:
                self.parse_nt_line(line, graph)

    def parse_nt_line(self, line: str, graph: Graph):
        parts = line.strip().split('\t')
        subject = parts[0][1:-1]
        predicate = parts[1][1:-1]
        parts[2] = parts[2].replace(" .", "")
        if parts[2].startswith("<") and parts[2].endswith(">"):
            obj = parts[2][1:-1]
            self.add_triple(subject, predicate, obj, graph)
            return
        elif parts[2].startswith('"') and parts[2].endswith('"'):
            obj = parts[2][1:-1]
        else:
            obj = parts[2]
        graph.add_data_to_vertex(subject, predicate, obj)


    def add_triple(self, subject: str, predicate: str, obj, graph: Graph):
        is_directed = True
        weight = 1

        graph.add_edge(subject, obj, is_directed, weight, predicate)

if __name__ == "__main__":
    a = RdfDataSource("C:\\Users\\marko\\Desktop\\fakultet\\5. semestar\\sok\\projekat\\graph-visualizer\\rdf_data_source\\rdf_data_source\\michael_jackson.nt")
    graph = a.fetch_data()
    dict = graph.to_dict()

    print(dict)
