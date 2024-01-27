from api.data_source_api import DataSourceBase
from api.models.graph import Graph
from api.models.edge import Edge
from api.models.node import Node

import xml.etree.ElementTree as ET
from typing import Any, Dict, List


class TrainDataSource(DataSourceBase):
    def __init__(self, data: str):
        self.data = data

    def fetch_data(self) -> Graph:
        graph = Graph()
        print("Print from train_data_source")
        return graph