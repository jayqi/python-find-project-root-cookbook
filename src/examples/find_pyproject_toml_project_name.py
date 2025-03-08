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
