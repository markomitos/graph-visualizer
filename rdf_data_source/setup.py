from setuptools import setup, find_packages

setup(
    name='rdf_data_source',
    version='0.1',
    packages=find_packages(),
    namespace_packages=['rdf_data_source'],
    install_requires=[
        'visualizer_api==0.1',
    ],
    entry_points={
        'data_sources': [
            'rdf_data_source = rdf_data_source.rdf_data_source:RdfDataSource',
        ],
    }
)