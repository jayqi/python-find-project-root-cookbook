help:
    just --list

render-readme:
    uv run python src/render_readme.py

lint:
    uv run python -m ruff format --check
    uv run python -m ruff check src

test:
    uv run python -m pytest
