# PipenvApp

Simple reference for `pipenv` usage with dependency links to (private) git repos.

See [`PipenvDependency`](https://github.com/pmlk/pipenv-dependency) (dependency of this project).

## (Un-)Deprecated?

This approach indirectly makes use of the `pip` flag `--process_dependency_links` which is/was **deprecated**. Read [here](https://github.com/pypa/pip/issues/3939) and [here](https://github.com/pypa/pip/issues/4187) for more information.

## Installation

```bash
# set environment variable for --process_dependency_links
$ export PIP_PROCESS_DEPENDENCY_LINKS=1
$ git clone https://github.com/pmlk/pipenv-app.git
$ cd pipenv-app
$ pipenv install -e .
```

### Dependency graph

In the pipenv-dependency project `numpy` is required just for kicks.

```bash
$ pipenv graph
PipenvApp==0.0.0
  - PipenvDependency [required: ==0.0.0, installed: 0.0.0]
    - numpy [required: Any, installed: 1.14.0]
```
