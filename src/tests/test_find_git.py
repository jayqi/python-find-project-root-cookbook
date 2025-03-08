import pytest

from examples.find_git import find_git


def test_find_git_current_wd(tmp_path, monkeypatch):
    git_dir = tmp_path / ".git"
    git_dir.mkdir()

    monkeypatch.chdir(tmp_path)

    assert find_git() == tmp_path


def test_find_git_in_parents(tmp_path, monkeypatch):
    git_dir = tmp_path / ".git"
    git_dir.mkdir()

    subdir = tmp_path / "subdir"
    subdir.mkdir()
    monkeypatch.chdir(tmp_path / "subdir")
    assert find_git() == tmp_path

    subsubdir = subdir / "subsubdir"
    subsubdir.mkdir()
    monkeypatch.chdir(subsubdir)
    assert find_git() == tmp_path


def test_find_git_not_found(tmp_path, monkeypatch):
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    monkeypatch.chdir(subdir)
    with pytest.raises(RuntimeError):
        find_git()
