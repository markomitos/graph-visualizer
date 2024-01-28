from visualizer_api.data_source_api import DataSourceBase
from models.graph import Graph


class TrainDataSource(DataSourceBase):
    def __init__(self, data: str):
        self.data = data

    def name(self) -> str:
        return 'Train Data Source'

    def fetch_data(self) -> Graph:
        graph = Graph()
        print("Print from train_data_source")
        return graph