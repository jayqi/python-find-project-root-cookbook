import os
from pathlib import Path


def proj_root_from_env_var() -> Path:
    """Get the project root directory from an environment variable."""
    proj_root = os.environ.get("PROJ_ROOT")
    if not proj_root:
        raise RuntimeError("PROJ_ROOT environment variable is not set.")
    return Path(proj_root)
