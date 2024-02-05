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
                                <style>
                                    #graph-container {
                                        width: 100%;
                                        height: 100%;
                                        overflow: hidden;
                                    }
                                </style>
                                <div id="graph-container"></div>
                                <script>
                                    const width = 928;
                                    const height = 680;

                                    // Create the SVG element
                                    const svg = d3.select("#graph-container")
                                        .append("svg")
                                        .attr("viewBox", `0 0 ${width} ${height}`)
                                        .style("height", "100%")
                                        .call(d3.zoom()
                                              .scaleExtent([1 / 2, 4])
                                              .on("zoom", zoomed));

                                     // Add the arrowhead marker definition
                                    svg.append("defs")
                                        .append("marker")
                                        .attr("id", "arrowhead")
                                        .attr("markerWidth", 10)
                                        .attr("markerHeight", 7)
                                        .attr("refX", 10)
                                        .attr("refY", 3.5)
                                        .attr("orient", "auto")
                                        .append("polygon")
                                        .attr("points", "0 0, 10 3.5, 0 7");

                                    const container = svg.append("g");

                                    function zoomed(event) {
                                        container.attr("transform", event.transform);
                                    }

                                    // Create the data for the graph
                                    const graphData = """ + json.dumps(data.ids_to_dicts()) + """;

                                    // Define the simulation with a force layout algorithm
                                    const simulation = d3.forceSimulation()
                                        .force("link", d3.forceLink().id(d => d.id).distance(300))
                                        .force("charge", d3.forceManyBody().strength(-500))
                                        .force("center", d3.forceCenter(width / 2, height / 2)) // Center force
                                        .force("x", d3.forceX(width / 2).strength(0.1)) // X force towards center
                                        .force("y", d3.forceY(height / 2).strength(0.1)); // Y force towards center

                        
                                    
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
                                              
                                    // Render the edges
                                    const link = container.append("g")
                                    .selectAll("line")
                                    .data(graphData.links)
                                    .enter().append("line")
                                    .attr("stroke", "#999")
                                    .attr("stroke-opacity", 0.6)
                                    .attr("stroke-width", 2)
                                    .attr("marker-end", "url(#arrowhead)"); // Add arrowhead marker

                                     // Append circles to nodes
                                    node.append("circle")
                                        .attr("r", 40)  // Adjust the radius of the circle
                                        .attr("fill", "#1f77b4");

                                    // Append text to nodes
                                    node.append("text")
                                        .style("text-anchor", "middle")
                                        .attr("dy", "0.35em")
                                        .text(d => JSON.stringify(d.data));  // Display id

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
