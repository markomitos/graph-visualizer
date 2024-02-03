from visualizer_api.data_source_api import DataSourceBase
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

from api.models.graph import Graph


class XMLDataSource(DataSourceBase):

    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.counter = Counter()

    # def __init__(self):
    #     pass

    def name(self) -> str:
        return 'XML Data Source'

    def fetch_data(self) -> Graph:
        graph = Graph()
        tree = ET.parse(self.xml_file)
        root = tree.getroot()

        self.construct_graph(graph, root)

        return graph

    def construct_graph(self, graph, element, parent_node=None):
        node_attributes = element.attrib
        print(node_attributes)

        # If it has no children add an attribute to the parent or handle reference
        if len(element) == 0:

            if parent_node is not None:
                reference = node_attributes.get("reference")

                if (reference is not None):
                    # Handle reference
                    index = int(reference.split('[')[1].rstrip(']'))
                    tag = reference.split('[')[0]
                    reference_node_id = f"{tag}_{index}"
                    graph.add_edge(parent_node, reference_node_id)
                else:
                    # Add an attribute
                    node = graph.get_vertex(parent_node)
                    node.data[element.tag] = element.text

        else:
            self.counter.increment(element.tag)

            node_id = f"{element.tag}_{self.counter[element.tag]}"
            graph.add_vertex(node_id, node_attributes)

            # Recursively process child elements
            for child in element:
                self.construct_graph(graph, child, node_id)

            # Connect the current node to its parent node, if it exists
            if parent_node is not None:
                graph.add_edge(parent_node, node_id)


class Counter:
    """Id counter"""
    def __init__(self):
        self.counts = {}

    def increment(self, tag):
        if tag in self.counts:
            self.counts[tag] += 1
        else:
            self.counts[tag] = 1

    def __getitem__(self, key):
        return self.counts[key]


if __name__ == "__main__":
    data_source = XMLDataSource('persons.xml')
    graph = data_source.fetch_data()

    dict = graph.to_dict()

    # Test
    print("Number of nodes:", graph.number_of_nodes())
    print("Number of edges:", graph.number_of_edges())

    print("Node Attributes:")
    for node in graph.nodes(data=True):
        print(node)

