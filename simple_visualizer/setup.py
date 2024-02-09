from setuptools import setup, find_packages

setup(
    name='simple_visualizer',
    version='0.1',
    packages=find_packages(),
    namespace_packages=['simple_visualizer'],
    install_requires=[
        'visualizer_api==0.1',
    ],
    entry_points={
        'visualizers': [
            'simple_visualizer = simple_visualizer.simple_visualizer:SimpleVisualiser',
        ],
    }
)