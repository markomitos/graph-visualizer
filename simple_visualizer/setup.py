from setuptools import setup, find_packages

setup(
    name='simple_visualiser',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies required by your visualizer plugin
    ],
    entry_points={
        'visualizers': [
            'simple_visualiser = simple_visualiser.simple_visualiser:SimpleVisualiser',
        ],
    }
)