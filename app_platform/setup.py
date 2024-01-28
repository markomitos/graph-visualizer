from setuptools import setup, find_packages

setup(
    name='app_platform',
    version='0.1',
    packages=find_packages(),
    namespace_packages=['app_platform'],
    install_requires=[
        'visualizer-visualizer_api==0.1',
    ],
    entry_points={
        'console_scripts': [
            'app_platform = app_platform.app_platform:main',
        ]
    }
)
