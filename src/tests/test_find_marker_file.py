import pytest

from examples.find_marker_file import find_marker


def test_find_marker_current_wd(tmp_path, monkeypatch):
    marker_file = tmp_path / ".marker"
    marker_file.write_text("value")

    monkeypatch.chdir(tmp_path)

    assert find_marker() == tmp_path


def test_find_marker_in_parents(tmp_path, monkeypatch):
    marker_file = tmp_path / ".marker"
    marker_file.write_text("value")

    subdir = tmp_path / "subdir"
    subdir.mkdir()
    monkeypatch.chdir(tmp_path / "subdir")
    assert find_marker() == tmp_path

    subsubdir = subdir / "subsubdir"
    subsubdir.mkdir()
    monkeypatch.chdir(subsubdir)
    assert find_marker() == tmp_path


def test_find_marker_not_found_different_value(tmp_path, monkeypatch):
    marker_file = tmp_path / ".marker"
    marker_file.write_text("another value")

    subdir = tmp_path / "subdir"
    subdir.mkdir()
    monkeypatch.chdir(subdir)
    with pytest.raises(RuntimeError):
        find_marker()


def test_find_marker_not_found_no_file(tmp_path, monkeypatch):
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    monkeypatch.chdir(subdir)
    with pytest.raises(RuntimeError):
        find_marker()
