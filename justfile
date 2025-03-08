help:
    just --list

render-readme:
    uv run python src/render_readme.py

test:
    uv run python -m pytest
