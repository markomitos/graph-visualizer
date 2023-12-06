from graph_explorer.app_platform.models.node import Node


class Tree:
    def __init__(self):
        self.root = None

    def set_root(self, root_node):
        if not isinstance(root_node, Node):
            raise ValueError("Root should be a Node")
        self.root = root_node

    def get_root(self):
        return self.root

    def depth_first_traversal(self, start_node=None):
        if start_node is None:
            start_node = self.root
        if start_node:
            print(f"Node ID: {start_node.node_id}, Data: {start_node.data}")
            for child in start_node.children:
                self.depth_first_traversal(child)
