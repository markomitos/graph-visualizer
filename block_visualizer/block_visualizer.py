from api.models.graph import Graph
from api.visualizer_api import VisualizerBase


class BlockVisualiser(VisualizerBase):
    def __init__(self):
        pass

    def name(self) -> str:
        return 'Block Visualizer'

    def render(self, data: Graph) -> str:
        print("block_visualizer")
        return "block_visualizer"
