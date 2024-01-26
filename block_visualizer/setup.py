from setuptools import setup, find_packages

setup(
    name='block_visualiser',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies required by your visualizer plugin
    ],
    entry_points={
        'visualizers': [
            'block_visualiser = block_visualiser.block_visualiser:BlockVisualiser',
        ],
    }
)