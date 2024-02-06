from django.shortcuts import render
from app_platform.app_platform import AppPlatform
from xml_data_source.xml_data_source import Counter
from django.http import JsonResponse

graph = None 

def home(request):
    global graph
    platform = AppPlatform()
    dataSource1 = platform.data_source_plugins[1]
    dataSource1.xml_file = "C:\\Programiranje\\Django\\graph-visualizer\\xml_data_source\\xml_data_source\\persons.xml"
    dataSource2 = platform.data_source_plugins[0]
    dataSource2.rdf_file = "C:\\Programiranje\\Django\\graph-visualizer\\rdf_data_source\\rdf_data_source\\michael_jackson.nt"

    # dataGraph = dataSource1.fetch_data()
    dataGraph = dataSource2.fetch_data()
    dataGraph = dataGraph.search("")

    graph = dataSource1.fetch_data()
    graph = graph.search("")

    context = {
        "title": "Graph Visualizer",
        "visualization_html": platform.visualizer_plugins[0].render(graph),
        "dataGraph": graph
    }
    return render(request, "index.html", context)


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
