import os

import pytest

from pytest_model_lib import skip_unless_env


def test_skip_unless_env_returns_value(monkeypatch):
    monkeypatch.setenv("MY_TEST_VAR", "secret123")
    assert skip_unless_env("MY_TEST_VAR") == "secret123"


def test_skip_unless_env_skips_when_missing():
    os.environ.pop("DEFINITELY_NOT_SET_VAR", None)
    with pytest.raises(pytest.skip.Exception):
        skip_unless_env("DEFINITELY_NOT_SET_VAR")


def test_static_env_vars_fixture(static_env_vars):
    assert static_env_vars.STATIC_DIR and static_env_vars.STATIC_DIR.exists()
    assert static_env_vars.CACHE_DIR and static_env_vars.CACHE_DIR.exists()
    assert os.environ["STATIC_DIR"] == str(static_env_vars.STATIC_DIR)
    assert os.environ["CACHE_DIR"] == str(static_env_vars.CACHE_DIR)
