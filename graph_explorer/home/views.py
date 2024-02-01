from django.shortcuts import HttpResponse, render

from app_platform.app_platform import AppPlatform
# Create your views here.
def home(request):
    platform = AppPlatform()

    return render(request,"index.html",
                  {"title":"Graph Visualizer",
                    "visualization_html":""})

