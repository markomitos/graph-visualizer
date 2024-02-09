import json

import networkx as nx
from models.graph import Graph
from visualizer_api.visualizer_api import VisualizerBase


class SimpleVisualiser(VisualizerBase):
    def __init__(self):
        pass

    def name(self) -> str:
        return 'Simple Visualizer'

    def render(self, data: Graph) -> str:
        html = """
                                <script src="https://d3js.org/d3.v7.min.js"></script>
                                <script src="https://d3js.org/d3-force.v3.min.js"></script>
                                <script>
                                    const width = 928;
                                    const height = 680;


                                    const container = d3.select("#center-graph-g");

                                    // Create the data for the graph
                                    const graphData = """ + json.dumps(data.ids_to_dicts()) + """;

                                    // Define the simulation with a force layout algorithm
                                    const simulation = d3.forceSimulation()
                                        .force("link", d3.forceLink().id(d => d.id).distance(300))
                                        .force("charge", d3.forceManyBody().strength(-500));

                                    // Render the edges
                                    const link = container.append("g")
                                    .selectAll("line")
                                    .data(graphData.links)
                                    .enter().append("line")
                                    .attr("stroke", "#999")
                                    .attr("stroke-opacity", 0.6)
                                    .attr("stroke-width", 2)
                                    .attr("marker-end", d => d.directed ? "url(#arrowhead)" : null); // Add arrowhead marker if directed is true

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

                                     // Append circles to nodes
                                    node.append("circle")
                                        .attr("r", 40)  // Adjust the radius of the circle
                                        .attr("fill", "#1f77b4");

                                    // Append text to nodes
                                    node.append("text")
                                        .style("text-anchor", "middle")
                                        .attr("dy", "0.35em")
                                        .text(d => d.id);  // Display id

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

                                    // Function to calculate the intersection point on the circle
                                    function calculateIntersectionX(source, target) {
                                        const angle = Math.atan2(target.y - source.y, target.x - source.x);
                                        return source.x + (40 * Math.cos(angle));  // 40 is the radius of the circle
                                    }

                                    function calculateIntersectionY(source, target) {
                                        const angle = Math.atan2(target.y - source.y, target.x - source.x);
                                        return source.y + (40 * Math.sin(angle));  // 40 is the radius of the circle
                                    }

                                    // Update the position of nodes and edges on each tick of the simulation
                                    simulation.nodes(graphData.nodes).on("tick", () => {
                                        node.attr("transform", d => `translate(${d.x}, ${d.y})`);

                                        link.attr("x1", d => calculateIntersectionX(d.source, d.target))
                                            .attr("y1", d => calculateIntersectionY(d.source, d.target))
                                            .attr("x2", d => calculateIntersectionX(d.target, d.source))
                                            .attr("y2", d => calculateIntersectionY(d.target, d.source));
                                    });

                                    simulation.force("link").links(graphData.links);
                                </script>
                                """

        return html