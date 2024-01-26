from setuptools import setup, find_packages

setup(
    name='app_platform',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies required by your platform
    ],
    entry_points={
        'console_scripts': [
            'app_platform = app_platform:main',
        ]
    }
)