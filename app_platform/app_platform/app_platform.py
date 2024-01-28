import pkg_resources
from typing import Union

from visualizer_api.data_source_api import DataSourceBase
from visualizer_api.visualizer_api import VisualizerBase



def main():
    data_source_plugins = load_plugins("data_sources")
    visualizer_plugins = load_plugins("visualizers")


def load_plugins(group_name : str) -> list[Union[DataSourceBase, VisualizerBase]]:
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=group_name):
        p = ep.load()
        print(f"{ep.name} {p}")
        plugin = p()
        plugins.append(plugin)
    return plugins


if __name__ == "__main__":
    main()