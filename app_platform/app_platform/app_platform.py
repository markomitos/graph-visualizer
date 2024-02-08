import pkg_resources
from typing import Union, List

from visualizer_api.data_source_api import DataSourceBase
from visualizer_api.visualizer_api import VisualizerBase
from app_platform.app_config import PlatformConfig
from app_platform.tree_view import *


class Workspace:
    def __init__(self, name: str):
        self.name = name
        self.data_source = None
        self.visualizer = None
        self.graph = None

class AppPlatform():

    def __init__(self):
        self.data_source_plugins = self.load_plugins("data_sources")
        self.visualizer_plugins = self.load_plugins("visualizers")
        self.current_data_source.filepath = PlatformConfig.data_filepaths[self.current_data_source.name()]
        self.load_graph()
        self.workspaces: List[Workspace] = []

    def create_workspace(self, name: str, visualizer_plugin, data_source_plugin, graph):
        if name not in [ws.name for ws in self.workspaces]:
            workspace = Workspace(name)
            workspace.visualizer = visualizer_plugin
            workspace.data_source = data_source_plugin
            workspace.graph = graph
            self.workspaces.append(workspace)

    def set_workspace(self, name):
        for workspace in self.workspaces:
            if workspace.name == name:
                PlatformConfig.workspace = name

    def current_workspace(self):
        for workspace in self.workspaces:
            if workspace.name == PlatformConfig.workspace:
                return workspace
        return None

    def get_workspaces(self):
        workspace_names = [workspace.name for workspace in self.workspaces]
        return workspace_names

    def get_workspace(self, name):
        for workspace in self.workspaces:
            if workspace.name == name:
                return workspace
        return None

    def update_current_workspace(self, visualizer_plugin, data_source_plugin, graph):
        current_workspace = self.current_workspace()
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
            if data_source.name() == PlatformConfig.data_source:
                return data_source
        return None

    @property
    def current_visualizer(self):
        for visualizer in self.visualizer_plugins:
            if visualizer.name() == PlatformConfig.visualizer:
                return visualizer
        return None

    def set_current_data_source(self, name):
        for data_source in self.data_source_plugins:
            if data_source.name() == name:
                PlatformConfig.data_source = name
                self.current_data_source.filepath = PlatformConfig.data_filepaths[self.current_data_source.name()]
                self.load_graph()

    def set_current_visualizer(self, name):
        for visualizer in self.visualizer_plugins:
            if visualizer.name() == name:
                PlatformConfig.visualizer = name

    def load_graph(self):
        PlatformConfig.current_graph = self.current_data_source.fetch_data()

    def get_main_view(self):
        return self.current_visualizer.render(PlatformConfig.current_graph)

    def get_tree_view(self) -> [str, str]:
        return generate_tree_view(PlatformConfig.current_graph)

    def get_vertex_tree_info(self, vertex_id):
        return PlatformConfig.current_graph.get_vertex_tree_info(vertex_id)

    def search(self, search_input: str):
        PlatformConfig.current_graph = PlatformConfig.current_graph.search(search_input)

    def reset_graph(self):
        self.set_current_data_source(PlatformConfig.data_source)

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
