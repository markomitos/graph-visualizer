from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('change-data-source-plugin/', views.change_data_source_plugin, name='change_data_source_plugin'),
    path('change-visualizer-plugin/', views.change_visualizer_plugin, name='change_visualizer_plugin'),
]
