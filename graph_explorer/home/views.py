from django.http import JsonResponse
from django.shortcuts import HttpResponse, render
from app_platform.app_platform import AppPlatform
from xml_data_source.xml_data_source import Counter
import json
platform = None
graph = None


def home(request):
    global platform
    global graph
    platform = AppPlatform()
    data_source = platform.current_data_source
    graph = data_source.fetch_data().search("")
    visualization_html = platform.current_visualizer.render(graph)

    context = {
        "title": "Graph Visualizer",
        # "graph_data": graph_data,  # Pass the serialized graph data to the template
        "visualization_html": visualization_html,
        "data_source_plugin_names": platform.get_data_source_plugin_names(),
        "visualizer_plugin_names": platform.get_visualizer_plugin_names(),
        "dataGraph": graph,
        "currentDataSource": platform.current_data_source.name(),
        "currentVisualizer": platform.current_visualizer.name()
    }
    return render(request, "index.html", context)


def change_data_source_plugin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_data_source = data.get('dataSource')
        data_source_plugins = platform.get_data_source_plugin_names()

        if selected_data_source in data_source_plugins:
            platform.set_current_data_source(selected_data_source)
            data_source = platform.current_data_source

            data_graph = data_source.fetch_data()
            visualization_html = platform.current_visualizer.render(data_graph)

            return JsonResponse({'status': 'success', 'visualization_html': visualization_html})
        else:
            return JsonResponse({'status': 'error', 'message': 'Data source plugin not found'})

    else:
        # Return a JSON response indicating failure if request method is not POST
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def change_visualizer_plugin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_visualizer = data.get('visualizer')

        # Update the current data source plugin based on the selected option
        visualizer_plugins = platform.get_visualizer_plugin_names()
        if selected_visualizer in visualizer_plugins:
            platform.set_current_visualizer(selected_visualizer)

            data_source = platform.current_data_source
            data_graph = data_source.fetch_data()
            visualization_html = platform.current_visualizer.render(data_graph)

            return JsonResponse({'status': 'success', 'visualization_html': visualization_html})
        else:
            return JsonResponse({'status': 'error', 'message': 'Data source plugin not found'})

    else:
        # Return a JSON response indicating failure if request method is not POST
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def get_vertex_info(request):
    if request.method == 'GET':
        vertex_id = request.GET.get('vertex_id')
        if vertex_id and graph:  # Check if graph is not None
            info = graph.get_vertex_tree_info(vertex_id)
            if info:
                return JsonResponse(info)
            else:
                return JsonResponse({'error': 'Vertex not found'}, status=404)
        else:
            return JsonResponse({'error': 'Invalid request'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
