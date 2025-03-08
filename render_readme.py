from pathlib import Path
from textwrap import dedent

CODE_BLOCK_TEMPLATE = dedent(
    """\
    ```python
    {code}
    ```
    """
)


def main():
    template = Path("_README.md.template").read_text()

    examples_dir = Path("examples")
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
    Path("README.md").write_text(rendered)


if __name__ == "__main__":
    main()
