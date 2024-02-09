from datetime import datetime

from visualizer_api.data_source_api import DataSourceBase
from models.graph import Graph
import re


class RdfDataSource(DataSourceBase):

    # def __init__(self):
    #     pass
    def __init__(self, filepath: str):
        super().__init__(filepath)

    def name(self) -> str:
        return 'RDF Data Source'

    def fetch_data(self) -> Graph:
        graph = Graph()
        self.parse_nt_file(self.filepath, graph)
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

        predicate = self.parse_property(predicate)
        obj = self.parse_xml_schema_type(obj)
        graph.add_data_to_vertex(subject, predicate, obj)


    def add_triple(self, subject: str, predicate: str, obj, graph: Graph):
        is_directed = True
        weight = 1

        graph.add_edge(subject, obj, is_directed, weight, predicate)

    def parse_xml_schema_type(self, value):
        match = re.match(r'"([^"]+)"\^\^<http://www\.w3\.org/2001/XMLSchema#(\w+)>', value)
        if match:
            value_str, type_str = match.groups()
            if type_str == 'string':
                return value_str
            elif type_str == 'integer':
                return int(value_str)
            elif type_str == 'nonNegativeInteger':
                return int(value_str)
            elif type_str == 'float':
                return float(value_str)
            elif type_str == 'date':
                return datetime.strptime(value_str, '%Y-%m-%d').date()
            elif type_str == 'dateTime':
                return datetime.strptime(value_str, '%Y-%m-%dT%H:%M:%S')
        else:
            return value

    def parse_property(self,property):
        property = property.replace("http://dbpedia.org/property/","")
        property = property.replace("http://dbpedia.org/ontology/","")
        return property

if __name__ == "__main__":
    a = RdfDataSource("C:\\Users\\marko\\Desktop\\fakultet\\5. semestar\\sok\\projekat\\graph-visualizer\\rdf_data_source\\rdf_data_source\\michael_jackson.nt")
    graph = a.fetch_data()
    dict = graph.to_dict()

    print(dict)
