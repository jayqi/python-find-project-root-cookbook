import os
from pathlib import Path


def proj_root_from_env_var() -> Path:
    """Get the project root directory from an environment variable. It must be an
    absolute path."""
    proj_root = os.environ.get("PROJ_ROOT")
    if not proj_root:
        raise RuntimeError("PROJ_ROOT environment variable is not set.")
    path = Path(proj_root)
    if not path.is_absolute():
        raise RuntimeError("PROJ_ROOT must be an absolute path.")
    return path
