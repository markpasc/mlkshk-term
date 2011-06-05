from setuptools import setup

setup(
    name='mlkshk-term',
    version='1.0',
    packages=[],
    include_package_data=True,
    scripts=['bin/mlkshk'],

    requires=['termtool', 'httplib2', 'poster'],
    install_requires=['termtool', 'httplib2', 'poster'],
)
