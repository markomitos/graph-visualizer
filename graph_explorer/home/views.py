from django.shortcuts import HttpResponse, render

from app_platform.app_platform import AppPlatform

from xml_data_source.xml_data_source import Counter


# Create your views here.
def home(request):
    platform = AppPlatform()
    dataSource1 = platform.data_source_plugins[1]
    dataSource1.xml_file = "C:\Programiranje\Django\graph-visualizer\\xml_data_source\\xml_data_source\persons.xml"
    dataSource1.counter = Counter()

    dataGraph = dataSource1.fetch_data()


    context = {
        "title": "Graph Visualizer",
        # "graph_data": graph_data,  # Pass the serialized graph data to the template
        "visualization_html": platform.visualizer_plugins[1].render(dataGraph),
        "dataSource1": dataGraph.to_dict()
    }
    return render(request, "index.html", context)

