from pathlib import Path
import shutil

import pytest

from examples.find_pyproject_toml import proj_root_from_pyproject_toml

EXAMPLE_PYPROJECT_TOML_ASSET = Path(__file__).parent / "assets" / "pyproject.toml"


def test_find_pyproject_toml_current_wd(tmp_path, monkeypatch):
    pyproject_toml = tmp_path / "pyproject.toml"
    shutil.copy(EXAMPLE_PYPROJECT_TOML_ASSET, pyproject_toml)

    monkeypatch.chdir(tmp_path)

    assert proj_root_from_pyproject_toml() == tmp_path


def test_find_pyproject_toml_in_parents(tmp_path, monkeypatch):
    pyproject_toml = tmp_path / "pyproject.toml"
    shutil.copy(EXAMPLE_PYPROJECT_TOML_ASSET, pyproject_toml)

    subdir = tmp_path / "subdir"
    subdir.mkdir()
    monkeypatch.chdir(tmp_path / "subdir")
    assert proj_root_from_pyproject_toml() == tmp_path

    subsubdir = subdir / "subsubdir"
    subsubdir.mkdir()
    monkeypatch.chdir(subsubdir)
    assert proj_root_from_pyproject_toml() == tmp_path


def test_find_pyproject_toml_not_found(tmp_path, monkeypatch):
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    monkeypatch.chdir(subdir)
    with pytest.raises(RuntimeError):
        proj_root_from_pyproject_toml()
