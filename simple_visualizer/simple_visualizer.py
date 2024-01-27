from api.models.graph import Graph
from api.visualizer_api import VisualizerBase


class SimpleVisualiser(VisualizerBase):
    def render(self, data: Graph) -> str:
        print("simple_visualizer")
        return "simple_visualizer"
