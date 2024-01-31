from visualizer_api.data_source_api import DataSourceBase
import xml.etree.ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt


class XMLDataSource(DataSourceBase):

    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.counter = Counter()

    def __init__(self):
        pass

    def name(self) -> str:
        return 'XML Data Source'

    def fetch_data(self) -> nx.Graph:
        graph = nx.DiGraph()
        tree = ET.parse(self.xml_file)
        root = tree.getroot()

        self.construct_graph(graph, root)

        return graph

    def construct_graph(self, graph, element, parent_node=None):
        node_attributes = element.attrib

        if len(element) == 0:
            # If it has no children add an attribute to the parent
            if parent_node is not None:
                node = graph.nodes[parent_node]
                node[element.tag] = element.text

                # Handle reference
                reference = node_attributes.get("reference")
                if (reference is not None):
                    index = int(reference.split('[')[1].rstrip(']'))
                    tag = reference.split('[')[0]
                    reference_node_id = f"{index}_{tag}"
                    graph.add_edge(parent_node, reference_node_id)
        else:
            self.counter.increment(element.tag)

            node_id = f"{self.counter[element.tag]}_{element.tag}"
            graph.add_node(node_id, **node_attributes)

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

    # # Visualize the graph
    # plt.figure(figsize=(12, 8))
    # pos = nx.spring_layout(graph)
    # nx.draw(graph, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold")
    # edge_labels = nx.get_edge_attributes(graph, 'distance')
    # nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    # plt.title("XML Graph")
    # plt.show()


    # Test
    print("Number of nodes:", graph.number_of_nodes())
    print("Number of edges:", graph.number_of_edges())

    print("Node Attributes:")
    for node in graph.nodes(data=True):
        print(node)

