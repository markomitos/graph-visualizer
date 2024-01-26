from api.data_source_api import DataSourceBase
from api.models.graph import Graph


class AirportDataSource(DataSourceBase):
    def fetch_data(self) -> Graph:
        pass