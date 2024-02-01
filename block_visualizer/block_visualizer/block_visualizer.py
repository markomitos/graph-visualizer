import json

from models.graph import Graph
from visualizer_api.visualizer_api import VisualizerBase


class BlockVisualiser(VisualizerBase):
    def __init__(self):
        pass

    def name(self) -> str:
        return 'Block Visualizer'

    def render(self, data: Graph) -> str:
        # Create a simple graph with 3 nodes and one link
        graph_data = {
            "nodes": [{"id": "Node1"}, {"id": "Node2"}, {"id": "Node3"}],
            "links": [{"source": "Node1", "target": "Node2"}]
        }

        # Construct the HTML for the graph visualization using D3.js
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
            // Create the SVG element
            const svg = d3.select("#graph-container")
                .append("svg")
                .attr("width", "100%")
                .attr("height", "100%");

            // Create the data for the graph
            const graphData = """ + json.dumps(graph_data) + """;

            // Define the simulation with a force layout algorithm
            const simulation = d3.forceSimulation()
                .force("link", d3.forceLink().id(d => d.id))
                .force("charge", d3.forceManyBody().strength(-100))
                .force("center", d3.forceCenter(window.innerWidth / 2, window.innerHeight / 2));

            // Render the edges
            const link = svg.append("g")
                .selectAll("line")
                .data(graphData.links)
                .enter().append("line")
                .attr("stroke", "#999")
                .attr("stroke-opacity", 0.6)
                .attr("stroke-width", 2);

            // Render the nodes
            const node = svg.append("g")
                .selectAll("circle")
                .data(graphData.nodes)
                .enter().append("circle")
                .attr("r", 10)
                .attr("fill", "#1f77b4")
                // Enable drag behavior
                .call(d3.drag()
                      .on("start", dragstarted)
                      .on("drag", dragged)
                      .on("end", dragended));

            // Add labels to the nodes
            node.append("title")
                .text(d => d.id);

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
                link.attr("x1", d => d.source.x)
                    .attr("y1", d => d.source.y)
                    .attr("x2", d => d.target.x)
                    .attr("y2", d => d.target.y);

                node.attr("cx", d => d.x)
                    .attr("cy", d => d.y);
            });

            simulation.force("link").links(graphData.links);
        </script>
        """

        return html
