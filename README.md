# Pipenv App

Simple reference for `pipenv` usage with dependency links to (private) git repos.

See [`pipenv dependency`](https://github.com/pmlk/pipenv-dependency) (dependency of this project).

## New ([PEP 508](https://www.python.org/dev/peps/pep-0508/)?) way

setup.py

```python
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
```

### Installation

```bash
$ git clone https://github.com/pmlk/pipenv-app.git
$ cd pipenv-app
$ pipenv install -e .
```

Despite an error the package and its sub-dependencies seem to be installed just fine 
(see `$ pipenv graph` output below). However, the `Pipfile.lock` is missing.

```bash
$ pipenv install -e .
Creating a virtualenv for this project…
Pipfile: /Users/<username>/SoftwareDevelopment/pipenv-app/Pipfile
Using /usr/local/Cellar/pipenv/2018.11.26_2/libexec/bin/python3.7 (3.7.2) to create virtualenv…
⠹ Creating virtual environment...Already using interpreter /usr/local/Cellar/pipenv/2018.11.26_2/libexec/bin/python3.7
Using real prefix '/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7'
New python executable in /Users/<username>/.local/share/virtualenvs/pipenv-app-vN89ij2s/bin/python3.7
Also creating executable in /Users/<username>/.local/share/virtualenvs/pipenv-app-vN89ij2s/bin/python
Installing setuptools, pip, wheel...
done.

✔ Successfully created virtual environment!
Virtualenv location: /Users/<username>/.local/share/virtualenvs/pipenv-app-vN89ij2s
Creating a Pipfile for this project…
Installing -e .…
Adding pipenvapp to Pipfile's [packages]…
✔ Installation Succeeded
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
✘ Locking Failed!
[pipenv.exceptions.ResolutionFailure]:   File "/usr/local/Cellar/pipenv/2018.11.26_2/libexec/lib/python3.7/site-packages/pipenv/resolver.py", line 69, in resolve
[pipenv.exceptions.ResolutionFailure]:       req_dir=requirements_dir
[pipenv.exceptions.ResolutionFailure]:   File "/usr/local/Cellar/pipenv/2018.11.26_2/libexec/lib/python3.7/site-packages/pipenv/utils.py", line 726, in resolve_deps
[pipenv.exceptions.ResolutionFailure]:       req_dir=req_dir,
[pipenv.exceptions.ResolutionFailure]:   File "/usr/local/Cellar/pipenv/2018.11.26_2/libexec/lib/python3.7/site-packages/pipenv/utils.py", line 480, in actually_resolve_deps
[pipenv.exceptions.ResolutionFailure]:       resolved_tree = resolver.resolve()
[pipenv.exceptions.ResolutionFailure]:   File "/usr/local/Cellar/pipenv/2018.11.26_2/libexec/lib/python3.7/site-packages/pipenv/utils.py", line 395, in resolve
[pipenv.exceptions.ResolutionFailure]:       raise ResolutionFailure(message=str(e))
[pipenv.exceptions.ResolutionFailure]:       pipenv.exceptions.ResolutionFailure: ERROR: ERROR: Could not find a version that matches pipenvdependency@ git+https://github.com/pmlk/pipenv-dependency.git@master from git+https://github.com/pmlk/pipenv-dependency.git@master
[pipenv.exceptions.ResolutionFailure]:       No versions found
[pipenv.exceptions.ResolutionFailure]: Warning: Your dependencies could not be resolved. You likely have a mismatch in your sub-dependencies.
  First try clearing your dependency cache with $ pipenv lock --clear, then try the original command again.
 Alternatively, you can use $ pipenv install --skip-lock to bypass this mechanism, then run $ pipenv graph to inspect the situation.
  Hint: try $ pipenv lock --pre if it is a pre-release dependency.
ERROR: ERROR: Could not find a version that matches pipenvdependency@ git+https://github.com/pmlk/pipenv-dependency.git@master from git+https://github.com/pmlk/pipenv-dependency.git@master
No versions found
Was https://pypi.org/simple reachable?
[pipenv.exceptions.ResolutionFailure]:       req_dir=requirements_dir
[pipenv.exceptions.ResolutionFailure]:   File "/usr/local/Cellar/pipenv/2018.11.26_2/libexec/lib/python3.7/site-packages/pipenv/utils.py", line 726, in resolve_deps
[pipenv.exceptions.ResolutionFailure]:       req_dir=req_dir,
[pipenv.exceptions.ResolutionFailure]:   File "/usr/local/Cellar/pipenv/2018.11.26_2/libexec/lib/python3.7/site-packages/pipenv/utils.py", line 480, in actually_resolve_deps
[pipenv.exceptions.ResolutionFailure]:       resolved_tree = resolver.resolve()
[pipenv.exceptions.ResolutionFailure]:   File "/usr/local/Cellar/pipenv/2018.11.26_2/libexec/lib/python3.7/site-packages/pipenv/utils.py", line 395, in resolve
[pipenv.exceptions.ResolutionFailure]:       raise ResolutionFailure(message=str(e))
[pipenv.exceptions.ResolutionFailure]:       pipenv.exceptions.ResolutionFailure: ERROR: ERROR: Could not find a version that matches pipenvdependency@ git+https://github.com/pmlk/pipenv-dependency.git@master from git+https://github.com/pmlk/pipenv-dependency.git@master
[pipenv.exceptions.ResolutionFailure]:       No versions found
[pipenv.exceptions.ResolutionFailure]: Warning: Your dependencies could not be resolved. You likely have a mismatch in your sub-dependencies.
  First try clearing your dependency cache with $ pipenv lock --clear, then try the original command again.
 Alternatively, you can use $ pipenv install --skip-lock to bypass this mechanism, then run $ pipenv graph to inspect the situation.
  Hint: try $ pipenv lock --pre if it is a pre-release dependency.
ERROR: ERROR: Could not find a version that matches pipenvdependency@ git+https://github.com/pmlk/pipenv-dependency.git@master from git+https://github.com/pmlk/pipenv-dependency.git@master
No versions found
Was https://pypi.org/simple reachable?
```

### Dependency Graph

In the pipenv-dependency project `numpy` is required just for kicks.

```bash
$ pipenv graph                                                                                                                                                                                                                                                            1 ↵
pipenvapp==0.0.0
  - pipenvdependency [required: Any, installed: 0.0.0]
    - numpy [required: Any, installed: 1.16.2]
```


## Old, now deprecated way

The following used to work for `pip` versions that respected the `--process-dependency-link` flag.

This approach indirectly makes use of the `pip` flag `--process-dependency-links` which is~/was~~ **deprecated**. ~
Read [here](https://github.com/pypa/pip/issues/3939) and [here](https://github.com/pypa/pip/issues/4187) for more information.

````python
from setuptools import setup

setup(
    name='pipenvapp',
    packages=['pipenvapp'],
    version='0.0.0',
    include_package_data=True,
    install_requires=['PipenvDependency==0.0.0'],
    dependency_links=["git+https://github.com/pmlk/pipenv-dependency.git@master#egg=PipenvDependency-0.0.0"],
)
````


### Installation

```bash
# set environment variable for --process-dependency-links
$ export PIP_PROCESS_DEPENDENCY_LINKS=1
$ git clone https://github.com/pmlk/pipenv-app.git
$ cd pipenv-app
$ pipenv install -e .
```
