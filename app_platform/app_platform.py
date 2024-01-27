import importlib.metadata
import pkg_resources

from api.data_source_api import DataSourceBase
from api.visualizer_api import (
    VisualizerBase
)


def main():
    plugins = []
    for ep in pkg_resources.iter_entry_points(group="visualizers"):
        p = ep.load()
        print(f"{ep.name} {p}")
        plugin = p()
        plugins.append(plugin)
        if issubclass(p, VisualizerBase):
            plugin = p()
            if hasattr(plugin, 'render'):
                plugin.render(None)
                plugins.append(plugin)
            else:
                print(f"Plugin {ep.name} nema metodu render().")

    xml_data = """
                    <trains>
                        <train id="1">
                            <name>Express</name>
                            <route>New York to Chicago</route>
                        </train>
                        <train id="2">
                            <name>Local</name>
                            <route>Chicago to San Francisco</route>
                        </train>
                    </trains>
                    """

    for ep in pkg_resources.iter_entry_points(group="data_sources"):
        p = ep.load()
        print(f"{ep.name} {p}")
        plugin = p(xml_data)
        plugins.append(plugin)
        if issubclass(p, DataSourceBase):
            plugin = p(xml_data)
            if hasattr(plugin, 'fetch_data'):
                plugin.fetch_data()
                plugins.append(plugin)
            else:
                print(f"Plugin {ep.name} nema metodu render().")
    return plugins

if __name__ == "__main__":
    main()