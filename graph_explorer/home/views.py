import copy

from django.shortcuts import HttpResponse, render

from app_platform.app_platform import AppPlatform


# Create your views here.
def home(request):
    platform = AppPlatform()
    visualized_graph = platform.visualizer_plugins[0].render(None)
    return render(request, "index.html",
                  {"title": "Graph Visualizer",

                   "birdView": copy.copy(visualized_graph),
                   "visualization_html": copy.copy(visualized_graph)})
