from setuptools import setup, find_packages

setup(
    name='block_visualizer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'visualizer-api==0.1',
    ],
    entry_points={
        'visualizers': [
            'block_visualizer = block_visualizer.block_visualizer:BlockVisualiser',
        ],
    }
)