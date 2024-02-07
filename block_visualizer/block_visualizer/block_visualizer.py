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

        data = Graph()

        data.add_vertex(1, {"name": "Jimmy", "age": 10})
        data.add_vertex(2, {"name": "Tim", "age": 11})
        data.add_vertex(3, {"name": "Johnny", "age": 10})
        data.add_edge(1, 2)

        graph_data = {
            "nodes": [{"id": "Node1"}, {"id": "Node2"}, {"id": "Node3"}],
            "links": [{"source": "Node1", "target": "Node2"}]
        }

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
                                .attr("stroke-width", 2);

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

                            // Append rectangles to nodes
                            node.append("rect")
                                .attr("width", 100)  // Adjust the width of the square
                                .attr("height", 50)  // Adjust the height of the square
                                .attr("fill", "#1f77b4");

                            // Append text to nodes
                            node.append("text")
                                .style("text-anchor", "middle")
                                .attr("dy", "0.35em")
                                .text(d => JSON.stringify(d.data));  // Display name and age

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
