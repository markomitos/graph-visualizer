from models.graph import Graph

def generate_tree_view(dataGraph: Graph):
    style_section = """
    <style>
        #tree-view{
            padding-left: 10px;
            padding-right: 20px;
        }

        #tree-view ul {
            padding-left: 20px;
        }

        .nested-ul {
            /*margin-left: 10px; !* Adjust indentation as needed *!*/
            display: none;
        }

        .vertex-info {
            text-align: left;
            margin-bottom: 10px;
        }

        .list-item-minus {
            list-style-type: none
        }

        .list-item-minus::before {
            content: "-";
            margin-right: 10px;
        }

        .list-item-plus {
            list-style-type: none
        }

        .list-item-plus::before {
            content: "+";
            margin-right: 10px;
        }

        .clickable {
            cursor: pointer;
            color: #356fdb;
        }

        .clickable:hover {
            color: #1a44b4;
        }
    </style>
    """

    # Initialize the HTML content for the tree view
    tree_view_section = "<h3>Tree view</h3><ul id='tree-view'>"

    for vertex in dataGraph.vertices:
        # Add HTML markup for each vertex
        tree_view_section += f"""
            <li class="list-item-plus vertex-info">
                <span class="clickable" onclick="loadVertexInfo(this)">{vertex.id}</span>
            </li>
        """

    # Close the UL tag
    tree_view_section += "</ul>"

    # Add the JavaScript function
    tree_view_section += """
    <script>
        function updateTreeFocusColor(vertexId){
            const liElements = document.querySelectorAll('.vertex-info');
            liElements.forEach(element => {
                let span = element.querySelectorAll('span')[0];
                if(span.textContent === vertexId){
                    span.style.color = 'red';
                    loadVertexInfo(span);
                } else {
                    span.style.color = '#356fdb';
                }
            });
        }
    
    
        const liElements = document.querySelectorAll('.vertex-info');

        // Add click event listener to each main li element
        liElements.forEach(element => {
            element.addEventListener('click', function() {
                let spanForChange = element.querySelectorAll('span')[0];
                updateMainViewFocusColor(spanForChange.textContent);
            
                liElements.forEach(n => {
                    let span = n.querySelectorAll('span')[0];
                    span.style.color = '#356fdb';
                });
    
                spanForChange.style.color = 'red';
            });
        });
    
        function loadVertexInfo(element) {

            var listItem = element.closest('li'); // Find the closest parent li element
            var nestedUl = listItem.querySelector('.nested-ul');

            // Check if the nested UL is already created
            if (!nestedUl) {
                nestedUl = document.createElement('ul');
                nestedUl.classList.add('nested-ul');
                listItem.appendChild(nestedUl);
            }


            if (nestedUl.innerHTML === '' && listItem.classList.contains('list-item-plus')) {
                var vertexId = element.textContent.trim();
                const url = '/get_vertex_info/?vertex_id=' + encodeURIComponent(vertexId);
                fetch(url)
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                        }
                        return response.json();
                    })
                    .then(data => {
                         if (data.vertex !== null) {
                            for (var key in data.vertex.data) {
                                var li = document.createElement('li');
                                li.textContent = key + ': ' + data.vertex.data[key];
                                li.classList.add('list-item-minus');
                                li.style.whiteSpace = 'nowrap';
                                nestedUl.appendChild(li);
                            }
                            nestedUl.style.display = 'block';
                            listItem.classList.remove('list-item-plus');
                            listItem.classList.add('list-item-minus');
                        } else {
                            console.log('Vertex not found');
                        }
                        for (var index in data.connections) {
                            var li = document.createElement('li');
                            var span = document.createElement('span');
                            span.textContent = data.connections[index];
                            span.style.whiteSpace = 'nowrap';
                            span.classList.add('clickable');
                            span.setAttribute('onclick', 'loadVertexInfo(this)');
                            li.appendChild(span);
                            li.classList.add('list-item-plus');
                            nestedUl.appendChild(li);
                        }
                    })
                    .catch(error => console.error('Error:', error));
            } else {
                // Toggle the visibility of the nested UL
                if (nestedUl.style.display === 'none') {
                    nestedUl.style.display = 'block';
                    listItem.classList.remove('list-item-plus');
                    listItem.classList.add('list-item-minus');
                } else {
                    nestedUl.style.display = 'none';
                    // Change the bullet class from '-' to '+'
                    listItem.classList.remove('list-item-minus');
                    listItem.classList.add('list-item-plus');
                }
            }
        }
    </script>
    """

    return style_section, tree_view_section

