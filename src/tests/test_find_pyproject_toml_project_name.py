from pathlib import Path
import shutil
import tomllib

import pytest
import tomli_w

from examples.find_pyproject_toml_project_name import find_pyproject_toml

EXAMPLE_PYPROJECT_TOML_ASSET = Path(__file__).parent / "assets" / "pyproject.toml"


def test_find_pyproject_toml_current_wd(tmp_path, monkeypatch):
    pyproject_toml = tmp_path / "pyproject.toml"
    with EXAMPLE_PYPROJECT_TOML_ASSET.open("rb") as fr, pyproject_toml.open("wb") as fw:
        data = tomllib.load(fr)
        data["project"]["name"] = "my-project-name"
        tomli_w.dump(data, fw)

    monkeypatch.chdir(tmp_path)

    assert find_pyproject_toml() == tmp_path


def test_find_pyproject_toml_in_parents(tmp_path, monkeypatch):
    pyproject_toml = tmp_path / "pyproject.toml"
    with EXAMPLE_PYPROJECT_TOML_ASSET.open("rb") as fr, pyproject_toml.open("wb") as fw:
        data = tomllib.load(fr)
        data["project"]["name"] = "my-project-name"
        tomli_w.dump(data, fw)

    subdir = tmp_path / "subdir"
    subdir.mkdir()
    monkeypatch.chdir(tmp_path / "subdir")
    assert find_pyproject_toml() == tmp_path

    subsubdir = subdir / "subsubdir"
    subsubdir.mkdir()
    monkeypatch.chdir(subsubdir)
    assert find_pyproject_toml() == tmp_path


def test_find_pyproject_toml_not_found_different_name(tmp_path, monkeypatch):
    pyproject_toml = tmp_path / "pyproject.toml"
    shutil.copy(EXAMPLE_PYPROJECT_TOML_ASSET, pyproject_toml)

    subdir = tmp_path / "subdir"
    subdir.mkdir()
    monkeypatch.chdir(subdir)
    with pytest.raises(RuntimeError):
        find_pyproject_toml()


def test_find_pyproject_toml_not_found_no_file(tmp_path, monkeypatch):
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    monkeypatch.chdir(subdir)
    with pytest.raises(RuntimeError):
        find_pyproject_toml()
