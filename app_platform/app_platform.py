import importlib.metadata

def main():
    print("Loading available plugins...")
    print("Data Source Plugins:")
    data_source_plugins = importlib.metadata.entry_points().get('data_sources', [])
    for plugin in data_source_plugins:
        print(f"- {plugin.name}")

    print("\nVisualizer Plugins:")
    visualizer_plugins = importlib.metadata.entry_points().get('visualizers', [])
    for plugin in visualizer_plugins:
        print(f"- {plugin.name}")

if __name__ == "__main__":
    main()