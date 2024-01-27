import importlib.metadata
import pkg_resources

from api.visualizer_api import (
    VisualizerBase
)


def main():
    """
        Dinamicko prepoznavanje plagina na osnovu pripadajuce grupe.
        """
    plugins = []
    for ep in pkg_resources.iter_entry_points(group="visualizers"):
        # Ucitavanje plagina.
        p = ep.load()
        print(f"{ep.name} {p}")
        # instanciranje odgovarajuce klase
        plugin = p()
        plugins.append(plugin)
        if issubclass(p, VisualizerBase):
            # Instanciranje odgovarajuce klase
            plugin = p()
            # Poziv metode render() ako postoji
            if hasattr(plugin, 'render'):
                plugin.render(None)
                plugins.append(plugin)
            else:
                print(f"Plugin {ep.name} nema metodu render().")
    return plugins

if __name__ == "__main__":
    main()