from pathlib import Path


def proj_root_from_git() -> Path:
    """Find the nearest parent directory containing .git."""
    current_dir = Path.cwd()
    while current_dir.parent != current_dir:
        if (current_dir / ".git").exists():
            return current_dir
        current_dir = current_dir.parent
    raise RuntimeError(".git not found in any parent directories.")
