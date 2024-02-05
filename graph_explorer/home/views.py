from django.shortcuts import HttpResponse, render

from app_platform.app_platform import AppPlatform

from xml_data_source.xml_data_source import Counter


# Create your views here.
def home(request):
    platform = AppPlatform()
    dataSource1 = platform.data_source_plugins[0]
    dataSource1.xml_file = "C:\\Users\\ComTech\\pycharm-projects\\graph-visualizer\\xml_data_source\\xml_data_source\\persons.xml"
    dataSource1.counter = Counter()
    dataSource2 = platform.data_source_plugins[1]
    dataSource2.rdf_file = "C:\\Users\\ComTech\\pycharm-projects\\graph-visualizer\\rdf_data_source\\rdf_data_source\\michael_jackson.nt"

    dataGraph = dataSource1.fetch_data()
    #dataGraph = dataSource2.fetch_data()
    dataGraph = dataGraph.search("")


    context = {
        "title": "Graph Visualizer",
        # "graph_data": graph_data,  # Pass the serialized graph data to the template
        "visualization_html": platform.visualizer_plugins[0].render(dataGraph),
        "dataSource1": dataGraph.to_dict(),
        "data_source_plugin_names" : platform.get_data_source_plugin_names(),
        "visualizer_plugin_names": platform.get_visualizer_plugin_names()
    }
    return render(request, "index.html", context)

