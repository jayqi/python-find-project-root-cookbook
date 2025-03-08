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
