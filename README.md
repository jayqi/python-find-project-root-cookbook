# Python Find Project Root Cookbook

[![tests](https://github.com/jayqi/reprexlite/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/jayqi/reprexlite/actions/workflows/tests.yml?query=workflow%3Atests+branch%3Amain)

Code examples to find the root directory of your project in different ways. All examples return a [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html) object. This can be useful in projects where you are reading or writing data to directories inside your project directory.

All code in this repository is licensed under the [MIT No Attribution (MIT-0) License](./LICENSE) and can be used without attribution.

If for some reason you prefer a take on a dependency for this functionality instead, see [pyprojroot](https://github.com/chendaniely/pyprojroot).

## Cookbook

Table of contents:

- [Find pyproject.toml file](#find-pyprojecttoml-file)
- [Find pyproject.toml file matching project name](#find-pyprojecttoml-file-matching-project-name)
- [Find .git directory](#find-git-directory)
- [Find a specific file containing a specific value](#find-a-specific-file-containing-a-specific-value)
- [Read from environment variable](#read-from-environment-variable)

### Find pyproject.toml file

```python
from pathlib import Path


def proj_root_from_pyproject_toml() -> Path:
    """Find the nearest parent directory containing pyproject.toml."""
    current_dir = Path.cwd()
    while current_dir.parent != current_dir:
        if (current_dir / "pyproject.toml").exists():
            return current_dir
        current_dir = current_dir.parent
    raise RuntimeError("pyproject.toml not found in any parent directories.")
```


### Find pyproject.toml file matching project name

```python
from pathlib import Path
import tomllib


def proj_root_from_pyproject_toml() -> Path:
    """Find the nearest parent directory containing pyproject.toml where the project
    name is 'my-project-name'."""
    project_name = "my-project-name"
    current_dir = Path.cwd()
    while current_dir.parent != current_dir:
        if (current_dir / "pyproject.toml").exists():
            with (current_dir / "pyproject.toml").open("rb") as f:
                pyproject = tomllib.load(f)
            if pyproject.get("project", {}).get("name") == project_name:
                return current_dir
        current_dir = current_dir.parent
    raise RuntimeError(
        f"pyproject.toml for '{project_name}' not found in any parent directories."
    )
```


> [!TIP]
> [tomllib](https://docs.python.org/3/library/tomllib.html) was added to the Python standard library in 3.11. To support earlier versions of Python, use the [tomli](https://github.com/hukkin/tomli) backport. You can use this dependency specifier:
> ```
> tomli >= 1.1.0 ; python_version < "3.11"
> ```
> and use this code to import it
> ```python
> import sys
>
> if sys.version_info[:2] >= (3, 11):
>     import tomllib
> else:
>     import tomli as tomllib
>
> ```

### Find .git directory

```python
from pathlib import Path


def proj_root_from_git() -> Path:
    """Find the nearest parent directory containing .git."""
    current_dir = Path.cwd()
    while current_dir.parent != current_dir:
        if (current_dir / ".git").exists():
            return current_dir
        current_dir = current_dir.parent
    raise RuntimeError(".git not found in any parent directories.")
```


### Find a specific file containing a specific value

```python
from pathlib import Path


def proj_root_from_marker_file() -> Path:
    """Find the nearest parent directory containing a file '.marker' whose contents are
    'value'."""
    marker_file_name = ".marker"
    marker_contents = "value"
    current_dir = Path.cwd()
    while current_dir.parent != current_dir:
        if (current_dir / marker_file_name).exists():
            if (current_dir / marker_file_name).read_text().strip() == marker_contents:
                return current_dir
        current_dir = current_dir.parent
    raise RuntimeError(
        f"{marker_file_name} containing '{marker_contents}' "
        "not found in any parent directories."
    )
```


### Read from environment variable

```python
import os
from pathlib import Path


def proj_root_from_env_var() -> Path:
    """Get the project root directory from an environment variable."""
    proj_root = os.environ.get("PROJ_ROOT")
    if not proj_root:
        raise RuntimeError("PROJ_ROOT environment variable is not set.")
    return Path(proj_root)
```