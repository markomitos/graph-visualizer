from setuptools import setup, find_packages

setup(
    name='train_data_source',
    version='0.1',
    packages=find_packages(),
    namespace_packages=['train_data_source'],
    install_requires=[
        'visualizer-visualizer_api==0.1',
    ],
    entry_points={
        'data_sources': [
            'train_data_source = train_data_source.train_data_source:TrainDataSource',
        ],
    }
)