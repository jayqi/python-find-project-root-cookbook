from pathlib import Path


def proj_root_from_here_file() -> Path:
    """Find the nearest parent directory containing a file '.here'."""
    current_dir = Path.cwd()
    while current_dir.parent != current_dir:
        if (current_dir / ".here").exists():
            return current_dir
        current_dir = current_dir.parent
    raise RuntimeError("'.here' file not found in any parent directories.")
