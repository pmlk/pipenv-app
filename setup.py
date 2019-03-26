from setuptools import setup

setup(
    name='pipenvapp',
    packages=['pipenvapp'],
    version='0.0.0',
    include_package_data=True,
    # new way
    install_requires=[
        'pipenvdependency @ git+https://github.com/pmlk/pipenv-dependency.git@master'
    ],

    # old way
    # install_requires=['PipenvDependency==0.0.0'],
    # dependency_links=["git+https://github.com/pmlk/pipenv-dependency.git@master#egg=pipenvdependency-0.0.0"],
)
