from api.models.graph import Graph
from api.visualizer_api import VisualizerBase


class BlockVisualiser(VisualizerBase):
    def render(self, data: Graph) -> str:
        print("block_visualizer")
        return "block_visualizer"
