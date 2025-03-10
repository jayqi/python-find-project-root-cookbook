import pytest

from examples.find_here_file import proj_root_from_here_file


def test_find_here_current_wd(tmp_path, monkeypatch):
    here_path = tmp_path / ".here"
    here_path.touch()

    monkeypatch.chdir(tmp_path)

    assert proj_root_from_here_file() == tmp_path


def test_find_here_in_parents(tmp_path, monkeypatch):
    here_path = tmp_path / ".here"
    here_path.touch()

    subdir = tmp_path / "subdir"
    subdir.mkdir()
    monkeypatch.chdir(tmp_path / "subdir")
    assert proj_root_from_here_file() == tmp_path

    subsubdir = subdir / "subsubdir"
    subsubdir.mkdir()
    monkeypatch.chdir(subsubdir)
    assert proj_root_from_here_file() == tmp_path


def test_find_here_not_found(tmp_path, monkeypatch):
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    monkeypatch.chdir(subdir)
    with pytest.raises(RuntimeError):
        proj_root_from_here_file()
