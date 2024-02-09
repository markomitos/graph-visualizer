class Node:
    def __init__(self, node_id, data=None):
        self.node_id = node_id
        self.data = data
        self.children = []

    def add_child(self, child_node):
        if not isinstance(child_node, Node):
            raise ValueError("Child should be a Node")
        self.children.append(child_node)

    def remove_child(self, child_node):
        if child_node in self.children:
            self.children.remove(child_node)
        else:
            raise ValueError("Node not found in children")

    def get_children(self):
        return self.children

    def __str__(self):
        return f"Node ID: {self.node_id}, Data: {self.data}, Children: {[child.node_id for child in self.children]}"
