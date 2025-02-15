from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='filter_stations',
    version='0.4.5',
    packages=find_packages(),
    include_package_data=True,
    description='Making it easier to navigate and clean station data',
    author='Austin Kaburia',
    author_email='kaburiaaustin1@gmail.com',
    url='https://github.com/kaburia/Packaging/tree/main/filter_stations',
    install_requires=[
        'pandas',
        'requests',
        'python-dateutil',
        'argparse',
        'haversine',
        'matplotlib',
        'numpy',
        'IPython',
        'folium',
        'datetime',
        'statsmodels',
        'tqdm',
        'geopandas',
        'matplotlib-scalebar'
    ],
    entry_points={
        'console_scripts': [
            'my-script=filter_stations.filter_stations:main'
        ]
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
)
