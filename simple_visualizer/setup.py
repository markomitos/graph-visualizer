from setuptools import setup, find_packages

setup(
    name='simple_visualizer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'visualizer-api==0.1',
    ],
    entry_points={
        'visualizers': [
            'simple_visualizer = simple_visualizer.simple_visualizer:SimpleVisualiser',
        ],
    }
)