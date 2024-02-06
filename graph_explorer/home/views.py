from django.http import JsonResponse
from django.shortcuts import HttpResponse, render

from app_platform.app_platform import AppPlatform

from xml_data_source.xml_data_source import Counter
import json
visualization_html = None
platform = None
# Create your views here.
def home(request):
    global visualization_html
    global platform
    platform = AppPlatform()
    data_source = platform.current_data_source
    data_source.xml_file = "C:\\Users\\ComTech\\pycharm-projects\\graph-visualizer\\xml_data_source\\xml_data_source\\persons.xml"
    data_graph = data_source.fetch_data().search("")
    visualization_html = platform.current_visualizer.render(data_graph)
    print(visualization_html)
    # dataSource1 = platform.data_source_plugins[0]
    # dataSource1.xml_file = "C:\\Users\\ComTech\\pycharm-projects\\graph-visualizer\\xml_data_source\\xml_data_source\\persons.xml"
    # dataSource1.counter = Counter()
    # dataSource2 = platform.data_source_plugins[1]
    # dataSource2.rdf_file = "C:\\Users\\ComTech\\pycharm-projects\\graph-visualizer\\rdf_data_source\\rdf_data_source\\michael_jackson.nt"
    #
    # dataGraph = dataSource1.fetch_data()
    # #dataGraph = dataSource2.fetch_data()
    # dataGraph = dataGraph.search("")


    context = {
        "title": "Graph Visualizer",
        # "graph_data": graph_data,  # Pass the serialized graph data to the template
        "visualization_html": visualization_html,
        "data_source_plugin_names": platform.get_data_source_plugin_names(),
        "visualizer_plugin_names": platform.get_visualizer_plugin_names()
    }
    return render(request, "index.html", context)


def change_data_source_plugin(request):
    global visualization_html
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_data_source = data.get('dataSource')

        # Update the current data source plugin based on the selected option
        data_source_plugins = platform.get_data_source_plugin_names()
        if selected_data_source in data_source_plugins:
            index = data_source_plugins.index(selected_data_source)
            platform.set_current_data_source(index)
            print(selected_data_source)
            if (selected_data_source == "RDF Data Source"):
                data_source = platform.current_data_source
                data_source.rdf_file = "C:\\Users\\ComTech\\pycharm-projects\\graph-visualizer\\rdf_data_source\\rdf_data_source\\michael_jackson.nt"
                data_graph = data_source.fetch_data().search("")
                visualization_html = platform.current_visualizer.render(data_graph)
            else:
                data_source = platform.current_data_source
                data_source.xml_file = "C:\\Users\\ComTech\\pycharm-projects\\graph-visualizer\\xml_data_source\\xml_data_source\\persons.xml"
                data_graph = data_source.fetch_data().search("")
                visualization_html = platform.current_visualizer.render(data_graph)
                print("YES")
                print(visualization_html)

            # Fetch data from the newly selected data source plugin
            # data_graph = platform.current_data_source.fetch_data().search("")

            # Render the graph with the updated data


            return JsonResponse({'status': 'success', 'visualization_html': visualization_html})
        else:
            return JsonResponse({'status': 'error', 'message': 'Data source plugin not found'})

    else:
        # Return a JSON response indicating failure if request method is not POST
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def change_visualizer_plugin(request):
    global visualization_html
    global platform
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_visualizer = data.get('visualizer')

        # Update the current data source plugin based on the selected option
        visualizer_plugins = platform.get_visualizer_plugin_names()
        if selected_visualizer in visualizer_plugins:
            index = visualizer_plugins.index(selected_visualizer)
            platform.set_current_visualizer(index)
            print(selected_visualizer)

            data_source = platform.current_data_source
            data_source.xml_file = "C:\\Users\\ComTech\\pycharm-projects\\graph-visualizer\\xml_data_source\\xml_data_source\\persons.xml"
            data_graph = data_source.fetch_data().search("")
            visualization_html = platform.current_visualizer.render(data_graph)

            # Fetch data from the newly selected data source plugin
            # data_graph = platform.current_data_source.fetch_data().search("")

            # Render the graph with the updated data


            return JsonResponse({'status': 'success', 'visualization_html': visualization_html})
        else:
            return JsonResponse({'status': 'error', 'message': 'Data source plugin not found'})

    else:
        # Return a JSON response indicating failure if request method is not POST
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})