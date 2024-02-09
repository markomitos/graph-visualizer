from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('change-data-source-plugin/', views.change_data_source_plugin, name='change_data_source_plugin'),
    path('change-visualizer-plugin/', views.change_visualizer_plugin, name='change_visualizer_plugin'),
    path('get_vertex_info/', views.get_vertex_info, name='get_vertex_info'),
    path('search/', views.search, name='search'),
    path('reset/', views.reset, name='reset'),
    path('create_workspace/', views.create_workspace, name='create_workspace'),
    path('delete_workspace/', views.delete_workspace, name='delete_workspace'),
    path('switch_workspace/', views.switch_workspace, name='switch_workspace'),
]
