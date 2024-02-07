from abc import ABC, abstractmethod
from typing import Any
from models.graph import Graph


class DataSourceBase(ABC):
    """
    Abstract base class for data source plugins.
    """
    def __init__(self, filepath: str):
        self._filepath = filepath

    @property
    def filepath(self) -> str:
        return self._filepath

    @filepath.setter
    def filepath(self, value: str):
        self._filepath = value

    @abstractmethod
    def name(self) -> str:
        pass
    @abstractmethod
    def fetch_data(self) -> Graph:
        """
        Method to fetch data from a specific source and construct a data model.
        """
        pass