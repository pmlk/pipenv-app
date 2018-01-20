from setuptools import setup

setup(
    name='PipenvApp',
    packages=['PipenvApp'],
    version='0.0.0',
    include_package_data=True,
    install_requires=['PipenvDependency==0.0.0'],
    dependency_links=["git+https://github.com/pmlk/pipenv-dependency.git@master#egg=PipenvDependency-0.0.0"],
)
