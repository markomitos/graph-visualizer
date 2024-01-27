import importlib.metadata
import pkg_resources
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
    return plugins

if __name__ == "__main__":
    main()