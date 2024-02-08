from django.http import JsonResponse
from django.shortcuts import HttpResponse, render
from app_platform.app_platform import AppPlatform
from django.views.decorators.csrf import csrf_exempt
from xml_data_source.xml_data_source import Counter
import json

platform: AppPlatform = AppPlatform()


def home(request):
    global platform
    visualization_html = platform.get_main_view()
    tree_view_style, tree_view_html = platform.get_tree_view()

    context = {
        "title": "Graph Visualizer",
        "visualization_html": visualization_html,
        "data_source_plugin_names": platform.get_data_source_plugin_names(),
        "visualizer_plugin_names": platform.get_visualizer_plugin_names(),
        "currentDataSource": platform.current_data_source.name(),
        "currentVisualizer": platform.current_visualizer.name(),
        "currentWorkspace": platform.get_current_workspace().name,
        "tree_view_style": tree_view_style,
        "tree_view_html": tree_view_html,
        'workspaces': [{'name': name} for name in platform.get_workspaces()],
        "current_filters": platform.get_current_workspace().current_filters
    }
    return render(request, "index.html", context)

@csrf_exempt
def change_data_source_plugin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_data_source = data.get('dataSource')
        data_source_plugins = platform.get_data_source_plugin_names()

        if selected_data_source in data_source_plugins:
            platform.set_current_data_source(selected_data_source)

            visualization_html = platform.get_main_view()

            return JsonResponse({'status': 'success', 'visualization_html': visualization_html})
        else:
            return JsonResponse({'status': 'error', 'message': 'Data source plugin not found'})

    else:
        # Return a JSON response indicating failure if request method is not POST
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def change_visualizer_plugin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_visualizer = data.get('visualizer')

        # Update the current data source plugin based on the selected option
        visualizer_plugins = platform.get_visualizer_plugin_names()
        if selected_visualizer in visualizer_plugins:

            platform.set_current_visualizer(selected_visualizer)
            visualization_html = platform.get_main_view()

            return JsonResponse({'status': 'success', 'visualization_html': visualization_html})
        else:
            return JsonResponse({'status': 'error', 'message': 'Data source plugin not found'})

    else:
        # Return a JSON response indicating failure if request method is not POST
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def get_vertex_info(request):
    if request.method == 'GET':
        vertex_id = request.GET.get('vertex_id')
        if vertex_id:
            info = platform.get_vertex_tree_info(vertex_id)
            if info:
                return JsonResponse(info)
            else:
                return JsonResponse({'error': 'Vertex not found'}, status=404)
        else:
            return JsonResponse({'error': 'Invalid request'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def search(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        platform.search(data.get('searchInput'))
        visualization_html = platform.get_main_view()
        return JsonResponse({'status': 'success', 'visualization_html': visualization_html})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def reset(request):
    if request.method == 'POST':
        platform.reset_graph()
        visualization_html = platform.get_main_view()
        return JsonResponse({'status': 'success', 'visualization_html': visualization_html})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def create_workspace(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        workspace_name = data.get('workspace_name')
        platform.create_workspace(workspace_name)
        return JsonResponse({'status': 'success', 'workspace_name': workspace_name})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def switch_workspace(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        workspace_name = data.get('workspace_name')
        platform.set_workspace(workspace_name)
        return JsonResponse({'status': 'success', 'workspace_name': workspace_name})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def add_filter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        filter = data.get('filter')
        platform.add_filter(filter)
        return JsonResponse({'status': 'success', 'filter': filter})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def remove_filter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        filter = data.get('filter')
        platform.remove_filter(filter)
        return JsonResponse({'status': 'success', 'filter': filter})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

