from pathlib import Path
from textwrap import dedent
import tomllib

CODE_BLOCK_TEMPLATE = dedent(
    """\
    ```python
    {code}
    ```
    """
)


def find_pyproject_toml() -> Path:
    """Find the nearest parent directory containing pyproject.toml where the project
    name is 'examples'."""
    project_name = "examples"
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


def main():
    project_root = find_pyproject_toml()

    template = (project_root / "src" / "_README.md.template").read_text()

    examples_dir = project_root / "src" / "examples"
    example_files = sorted(
        path for path in examples_dir.glob("*.py") if not path.name.startswith("_")
    )
    examples = {}
    for example_file in example_files:
        example_name = example_file.stem
        examples[example_name] = CODE_BLOCK_TEMPLATE.format(
            code=example_file.read_text().strip()
        )

    rendered = template.format(**examples)
    (project_root / "README.md").write_text(rendered)


if __name__ == "__main__":
    main()
