import pytest

from examples.read_from_env_var import proj_root_from_env_var


def test_read_from_env_var(tmp_path, monkeypatch):
    monkeypatch.setenv("PROJ_ROOT", str(tmp_path))
    assert proj_root_from_env_var() == tmp_path


def test_read_from_env_var_not_set(monkeypatch):
    monkeypatch.delenv("PROJ_ROOT", raising=False)
    with pytest.raises(RuntimeError):
        proj_root_from_env_var()
