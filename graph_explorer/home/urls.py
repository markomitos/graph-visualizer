from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('get_vertex_info/', views.get_vertex_info, name='get_vertex_info'),
]