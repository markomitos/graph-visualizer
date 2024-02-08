import pkg_resources
from app_platform.workspace import Workspace
from typing import Union, List

from visualizer_api.data_source_api import DataSourceBase
from visualizer_api.visualizer_api import VisualizerBase
from app_platform.app_config import PlatformConfig
from app_platform.tree_view import *




class AppPlatform():

    def __init__(self):
        self.data_source_plugins = self.load_plugins("data_sources")
        self.visualizer_plugins = self.load_plugins("visualizers")
        self.create_workspace("Default")
        self.current_data_source.filepath = PlatformConfig.data_filepaths[self.current_data_source.name()]
        self.load_graph()

    def create_workspace(self, name: str):
        if name not in PlatformConfig.workspaces:
            workspace = Workspace(name)
            PlatformConfig.workspaces[name] = workspace
            self.load_graph()

    def set_workspace(self, name):
        for workspace in PlatformConfig.workspaces:
            if workspace == name:
                PlatformConfig.current_workspace = name
                self.load_graph()

    def get_current_workspace(self):
        if PlatformConfig.current_workspace in PlatformConfig.workspaces:
            return PlatformConfig.workspaces[PlatformConfig.current_workspace]
        return None

    def get_workspaces(self):
        workspace_names = []
        for key in PlatformConfig.workspaces.keys():
            workspace_names.append(key)
        return workspace_names

    def get_workspace(self, name):
        for workspace in PlatformConfig.workspaces:
            if workspace == name:
                return workspace
        return None

    def update_current_workspace(self, visualizer_plugin, data_source_plugin, graph):
        current_workspace = self.get_current_workspace()
        if current_workspace:
            # Update attributes of the current workspace
            current_workspace.visualizer = visualizer_plugin
            current_workspace.data_source = data_source_plugin
            current_workspace.graph = graph
            return True
        else:
            return False

    @property
    def current_data_source(self):
        for data_source in self.data_source_plugins:
            if data_source.name() == self.get_current_workspace().data_source:
                return data_source
        return None

    @property
    def current_visualizer(self):
        for visualizer in self.visualizer_plugins:
            if visualizer.name() == self.get_current_workspace().visualizer:
                return visualizer
        return None

    def set_current_data_source(self, name):
        for data_source in self.data_source_plugins:
            if data_source.name() == name:
                self.get_current_workspace().data_source = name
                self.current_data_source.filepath = PlatformConfig.data_filepaths[self.current_data_source.name()]
                self.load_graph()

    def set_current_visualizer(self, name):
        for visualizer in self.visualizer_plugins:
            if visualizer.name() == name:
                self.get_current_workspace().visualizer = name

    def load_graph(self):
        self.get_current_workspace().current_graph = self.current_data_source.fetch_data()
        search_inputs = self.get_current_workspace().current_search
        filters = self.get_current_workspace().current_filters
        for search_input in search_inputs:
            self.get_current_workspace().current_graph = self.get_current_workspace().current_graph.search(search_input)
        for filter in filters:
            self.get_current_workspace().current_graph = self.get_current_workspace().current_graph.filter(filter)


    def get_main_view(self):
        return self.current_visualizer.render(self.get_current_workspace().current_graph)

    def get_tree_view(self) -> [str, str]:
        return generate_tree_view(self.get_current_workspace().current_graph)

    def get_vertex_tree_info(self, vertex_id):
        return self.get_current_workspace().current_graph.get_vertex_tree_info(vertex_id)

    def search(self, search_input: str):
        self.get_current_workspace().current_graph = self.get_current_workspace().current_graph.search(search_input)
        self.get_current_workspace().current_search.append(search_input)

    def add_filter(self, filter):
        self.get_current_workspace().current_graph = self.get_current_workspace().current_graph.filter(filter)
        self.get_current_workspace().current_filters.append(filter)

    def remove_filter(self, filter):
        self.get_current_workspace().current_filters.remove(filter)
        self.load_graph()

    def reset_graph(self):
        self.get_current_workspace().current_search = []
        self.set_current_data_source(self.get_current_workspace().data_source)

    def load_plugins(self, group_name: str) -> list[Union[DataSourceBase, VisualizerBase]]:
        plugins = []
        for ep in pkg_resources.iter_entry_points(group=group_name):
            p = ep.load()
            print(f"{ep.name} {p}")
            if group_name == "data_sources":
                plugin = p("")
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
