from abc import ABC, abstractmethod
from typing import Any
from api.models.graph import Graph



class DataSourceBase(ABC):
    """
    Abstract base class for data source plugins.
    """

    @abstractmethod
    def name(self) -> str:
        pass
    @abstractmethod
    def fetch_data(self) -> Graph:
        """
        Method to fetch data from a specific source and construct a data model.
        """
        pass