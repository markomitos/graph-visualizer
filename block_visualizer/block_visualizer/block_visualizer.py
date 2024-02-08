import json

import networkx as nx
from models.graph import Graph
from visualizer_api.visualizer_api import VisualizerBase


class BlockVisualiser(VisualizerBase):
    def __init__(self):
        pass

    def name(self) -> str:
        return 'Block Visualizer'

    def render(self, data: Graph) -> str:
        # Create a simple graph with 3 nodes and one link

        # data = Graph()

        # data.add_vertex(1, {"name": "Jimmy", "age": 10})
        # data.add_vertex(2, {"name": "Tim", "age": 11})
        # data.add_vertex(3, {"name": "Johnny", "age": 10})
        # data.add_edge(1, 2)

        # graph_data = {
        #     "nodes": [{"id": "Node1"}, {"id": "Node2"}, {"id": "Node3"}],
        #     "links": [{"source": "Node1", "target": "Node2"}]
        # }

        # Construct the HTML for the graph visualization using D3.js
        html = """
                        <script src="https://d3js.org/d3.v7.min.js"></script>
                        <script src="https://d3js.org/d3-force.v3.min.js"></script>
                        <script>
                            const width = 928;
                            const height = 680;
                            const container = d3.select("#center-graph-g");

                            // Create the data for the graph
                            const graphData = """ + json.dumps(data.to_dict()) + """;

                            // Define the simulation with a force layout algorithm
                            const simulation = d3.forceSimulation()
                                .force("link", d3.forceLink().id(d => d.id).distance(200))
                                .force("charge", d3.forceManyBody().strength(-300)); // Y force towards center

                            // Render the edges
                            const link = container.append("g")
                                .selectAll("line")
                                .data(graphData.links)
                                .enter().append("line")
                                .attr("stroke", "#999")
                                .attr("stroke-opacity", 0.6)
                                .attr("stroke-width", 2)
                                .attr("marker-end", "url(#arrowhead)"); 

                            // Render the nodes
                            const node = container.append("g")
                                .selectAll("g")
                                .data(graphData.nodes)
                                .enter().append("g")
                                .attr("class", "node")
                                .call(d3.drag()
                                      .on("start", dragstarted)
                                      .on("drag", dragged)
                                      .on("end", dragended));

                            node.append("rect")
                                .attr("width", 200)  // Adjust the width of the rectangle
                                .attr("height", function(d) {
                                    // Calculate the height based on the number of attributes
                                    const attributesCount = Object.keys(d.data).length;
                                    return 50 + attributesCount * 25;  // Assuming each attribute has a height of 50 units
                                })
                                .attr("fill", "#1f77b4");
                            node.append("rect")
                                .attr("width", 200)  // Adjust the width of the rectangle
                                .attr("height", 50)
                                .attr("fill", "#75d1f0");
                            // Append text to nodes
                            node.append("text").
                                attr("y", "25").
                                attr("x", "5").
                                text(d => "# "+d.id);    
                            // Append text to nodes
                            node.append("text")
                                .attr("y", "50")
                                .each(function(d) {
                                    const textElement = d3.select(this);
                                    
                                    // Convert JSON object to an array of key-value pairs
                                    const attributes = Object.entries(d.data);
                                    
                                    // Append a <tspan> for each attribute
                                    attributes.forEach((attr, i) => {
                                        textElement.append("tspan")
                                            .attr("x", 5)
                                            .attr("dy", 1.2 + "em") // Adjust the spacing between lines as needed
                                            .text(`+ ${attr[0]}: ${attr[1]}`);
                                    });
                                });
                            // Define drag behavior functions
                            function dragstarted(event, d) {
                                if (!event.active) simulation.alphaTarget(0.3).restart();
                                d.fx = d.x;
                                d.fy = d.y;
                            }

                            function dragged(event, d) {
                                d.fx = event.x;
                                d.fy = event.y;
                            }

                            function dragended(event, d) {
                                if (!event.active) simulation.alphaTarget(0);
                                d.fx = null;
                                d.fy = null;
                            }

                            // Update the position of nodes and edges on each tick of the simulation
                            simulation.nodes(graphData.nodes).on("tick", () => {
                                node.attr("transform", d => `translate(${d.x}, ${d.y})`);
                                link.attr("x1", d => d.source.x)
                                    .attr("y1", d => d.source.y)
                                    .attr("x2", d => d.target.x)
                                    .attr("y2", d => d.target.y);
                            });

                            simulation.force("link").links(graphData.links);
                        </script>
                        """

        return html
