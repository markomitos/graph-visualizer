from models.graph import Graph
from visualizer_api.visualizer_api import VisualizerBase


class SimpleVisualiser(VisualizerBase):
    def __init__(self):
        pass

    def name(self) -> str:
        return 'Simple Visualizer'

    def render(self, data: Graph) -> str:
        print("simple_visualizer")
        return "simple_visualizer"
