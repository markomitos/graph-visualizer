from abc import ABC, abstractmethod
from typing import Any
from models.graph import Graph
from datetime import datetime


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

    @staticmethod
    def parse_string_to_fit_type(value: str) -> Any:
        # Try parsing into date
        try:
            date_value = datetime.strptime(value, '%Y-%m-%d')
            return date_value.date()
        except ValueError:
            pass

        # Try parsing into integer
        try:
            int_value = int(value)
            return int_value
        except ValueError:
            pass

        # Try parsing into float
        try:
            float_value = float(value)
            return float_value
        except ValueError:
            pass

        # If not date or float, return original string
        return value