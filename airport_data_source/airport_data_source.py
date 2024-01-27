from api.data_source_api import DataSourceBase
from api.models.graph import Graph


class AirportDataSource(DataSourceBase):
    def __init__(self, data: str):
        self.data = data
    def fetch_data(self) -> Graph:
        graph = Graph()
        print("Print from airport_data_source")
        return graph