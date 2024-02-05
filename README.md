# graph-visualizer
A modular graph visualizer written in python using Django


### Follow these steps when starting the application for the first time:
1. Create seperate run configuration for each plugin.
   - Go to `Run` -> `Edit Configurations`.
   - Create a new Python configuration.
   - In the Script field, select setup.py module.
   - In the Script parameters field, enter install.
   - Make sure to deselect the options:
     - Add content roots to PYTHONPATH
     - Add source roots to PYTHONPATH
   - Repeat these steps for all setup.py scripts present in the project.
2. Run each created configuration in this order:
   1. API
   2. Platform
   3. Rest of the plugins
3. Run these shell scripts
   - `./setup.sh` (Optional) 
   - `./clean.sh`
   - `./run.sh`


### Data source plugins
1. XML Data source parser
   - Requires a path to a file as a parameter
   - Turns any XML file into a graph
   - Supports cyclic and acyclic data
   - Reference usage:
    `<ref reference="Tag[num]"/>`
2. RDF Data source parser
   - Requires a path to a file as a parameter
   - Turns any RDF file into a graph
   - Supports cyclic and acyclic data