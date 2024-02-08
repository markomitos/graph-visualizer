from django.apps import AppConfig
from models.graph import Graph



class PlatformConfig(AppConfig):
    current_workspace = "Default"
    workspaces = {}
    data_filepaths = {
        "XML Data Source": "C:\\Users\\ComTech\\pycharm-projects\\graph-visualizer\\xml_data_source\\xml_data_source\\persons.xml",
        "RDF Data Source": "C:\\Users\\ComTech\\pycharm-projects\\graph-visualizer\\rdf_data_source\\rdf_data_source\\michael_jackson.nt"
    }



