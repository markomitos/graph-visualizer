from django.apps import AppConfig
from models.graph import Graph



class PlatformConfig(AppConfig):
    current_workspace = "Default"
    workspaces = {}



