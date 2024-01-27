from abc import ABC, abstractmethod
from typing import Any
from api.models.graph import Graph


class VisualizerBase(ABC):
    """
    Abstract base class for visualizer plugins.
    """

    @abstractmethod
    def render(self, data: Graph) -> str:
        """
        Method to render visualization of data.

        Args:
            data: Data to be visualized.
        """
        pass