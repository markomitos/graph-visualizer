from setuptools import setup, find_packages

setup(
    name='airport_data_source',
    version='0.1',
    packages=find_packages(),
    namespace_packages=['airport_data_source'],
    install_requires=[
        'visualizer_api==0.1',
    ],
    entry_points={
        'data_sources': [
            'airport_data_source = airport_data_source.airport_data_source:AirportDataSource',
        ],
    }
)