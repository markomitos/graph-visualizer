from setuptools import setup, find_packages

setup(
    name='train_data_source',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies required by your data source plugin
    ],
    entry_points={
        'data_sources': [
            'train_data_source = train_data_source.train_data_source:TrainDataSource',
        ],
    }
)