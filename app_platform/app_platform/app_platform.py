import pkg_resources
from typing import Union

from visualizer_api.data_source_api import DataSourceBase
from visualizer_api.visualizer_api import VisualizerBase

class AppPlatform():

    def __init__(self):
        self.data_source_plugins = self.load_plugins("data_sources")
        self.visualizer_plugins = self.load_plugins("visualizers")
        self._current_data_source_index = 0
        self._current_visualizer_index = 0

    @property
    def current_data_source(self):
        if self.data_source_plugins:
            return self.data_source_plugins[self._current_data_source_index]
        return None

    @property
    def current_visualizer(self):
        if self.visualizer_plugins:
            return self.visualizer_plugins[self._current_visualizer_index]
        return None

    def test(self):
        return "test"

    def load_plugins(self, group_name: str) -> list[Union[DataSourceBase, VisualizerBase]]:
        plugins = []
        for ep in pkg_resources.iter_entry_points(group=group_name):
            p = ep.load()
            print(f"{ep.name} {p}")
            if group_name == "data_sources":
                plugin = p("persons.xml")
            else:
                plugin = p()
            plugins.append(plugin)
        return plugins

    def get_data_source_plugin_names(self):
        plugins = []
        for plugin in self.data_source_plugins:
            plugins.append(plugin.name())
        return plugins

    def get_visualizer_plugin_names(self):
        plugins = []
        for plugin in self.visualizer_plugins:
            plugins.append(plugin.name())
        return plugins

if __name__ == "__main__":
    app = AppPlatform()
