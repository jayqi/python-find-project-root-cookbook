from pathlib import Path


def proj_root_from_pyproject_toml() -> Path:
    """Find the nearest parent directory containing pyproject.toml."""
    current_dir = Path.cwd()
    while current_dir.parent != current_dir:
        if (current_dir / "pyproject.toml").exists():
            return current_dir
        current_dir = current_dir.parent
    raise RuntimeError("pyproject.toml not found in any parent directories.")
