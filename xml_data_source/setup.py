from setuptools import setup, find_packages

setup(
    name='xml_data_source',
    version='0.1',
    packages=find_packages(),
    namespace_packages=['xml_data_source'],
    install_requires=[
        'visualizer-visualizer_api==0.1',
    ],
    entry_points={
        'data_sources': [
            'xml_data_source = xml_data_source.xml_data_source:XMLDataSource',
        ],
    }
)