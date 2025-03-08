# Python Project Root Cookbook

Reference code examples to find the root directory of your project using different approaches

## Find pyproject.toml file

```python
from pathlib import Path


def find_pyproject_toml() -> Path:
    """Find the nearest parent directory containing pyproject.toml."""
    current_dir = Path.cwd()
    while current_dir.parent != current_dir:
        if (current_dir / "pyproject.toml").exists():
            return current_dir
        current_dir = current_dir.parent
    raise RuntimeError("pyproject.toml not found in any parent directories.")
```


## Find pyproject.toml file matching project name

```python
from pathlib import Path
import tomllib


def find_pyproject_toml() -> Path:
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


## Find .git directory

```python
from pathlib import Path


def find_git() -> Path:
    """Find the nearest parent directory containing .git."""
    current_dir = Path.cwd()
    while current_dir.parent != current_dir:
        if (current_dir / ".git").exists():
            return current_dir
        current_dir = current_dir.parent
    raise RuntimeError(".git not found in any parent directories.")
```


## Find a specific file containing a specific value

```python
from pathlib import Path


def find_marker() -> Path:
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

