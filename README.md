# Graph Visualizer

Graph Visualizer is a modular graph visualization tool written in Python using Django.

## Getting Started

Follow these steps when starting the application for the first time:

1. **Create Separate Run Configurations for Each Plugin:**
   - Go to `Run` -> `Edit Configurations`.
   - Create a new Python configuration.
   - In the "Script" field, select `setup.py` module.
   - In the "Script parameters" field, enter `install`.
   - Make sure to deselect the options:
     - Add content roots to PYTHONPATH
     - Add source roots to PYTHONPATH
   - Repeat these steps for all `setup.py` scripts present in the project.

2. **Run Each Created Configuration in This Order:**
   1. API
   2. Platform
   3. Rest of the plugins

3. **Run These Shell Scripts:**
   - `./setup.sh` (Optional) 
   - `./clean.sh`
   - `./run.sh`

## Data Source Plugins

### 1. XML Data Source Parser

- **Description**: Parses XML files into graphs.
- **Parameters**: Requires a file path as input.
- **Functionality**: Supports both cyclic and acyclic data structures.
- **Usage**: `<ref reference="Tag[num]"/>`

### 2. RDF Data Source Parser

- **Description**: Parses RDF files into graphs.
- **Parameters**: Requires a file path as input.
- **Functionality**: Supports both cyclic and acyclic data structures.

## Visualizers Plugins

### 1. Blocked Visualizer

- **Description**: Generates vertices and edges, connecting them based on specified source, destination, and directedness.
- **Parameters**: Requires a graph parameter of type `model.Graph`.
- **Functionality**: Implements logic for creating various types of graphs, including directed, undirected, cyclic, and acyclic graphs.
- **Attribute Representation**: Parses each attribute from the nodes of the graph and represents them in blocks.
- **Vertex Identification**: Each block header displays the ID of the corresponding vertex.

### 2. Simple Visualizer

- **Description**: Generates vertices and edges, connecting them based on specified source, destination, and directedness.
- **Parameters**: Requires a graph parameter of type `model.Graph`.
- **Functionality**: Implements logic for creating various types of graphs, including directed, undirected, cyclic, and acyclic graphs.
- **Attribute Representation**: Parses only the IDs from the nodes of the graph and represents them in circular nodes.
- **Vertex Identification**: Each node displays the ID of the corresponding vertex.

### Django

The Django module serves as the frontend framework for the Graph Visualizer application. It provides the user interface and handles client-side interactions. Django facilitates the presentation of data visualizations and enables users to interact with various features, including:
- Force layout tree view
- Bird view
- Filtering
- Search
- Workspaces

The module is responsible for rendering the graphical elements and ensuring a responsive and intuitive user experience.

### API

The API module contains interfaces for both visualizers and data sources. It defines the contracts and methods that need to be implemented by various plugins in order to integrate with the Graph Visualizer application. By providing a standardized set of interfaces, the API module enables seamless communication and interoperability between different components of the system, facilitating modular development and extensibility.

### App Platform

The App Platform module is responsible for orchestrating the data flow within the Graph Visualizer application. It utilizes data sources to fetch raw data and visualizers to transform and render that data into graphical representations. The platform then integrates these visualizations into the frontend GUI, providing users with access to features such as force layout tree view, bird view, filtering, and workspaces. By managing the data processing pipeline and user interactions, the App Platform module ensures a cohesive and interactive user experience.


## Team Members

| Name            | Role              | Index     |
|-----------------|-------------------|-----------|
| Ilija Bešlin    | XML Data Source   | SV71/2021 |
| Marko Mitošević | RDF Data Source   | SV56/2021 |
| Branko Marić    | Simple Visualizer | SV70/2021 |
| Ognjen Gligorić | Block Visualizer  | SV79/2021 |