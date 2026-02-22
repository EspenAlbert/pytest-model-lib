# pytest-model-lib

[![PyPI](https://img.shields.io/pypi/v/pytest-model-lib)](https://pypi.org/project/pytest-model-lib/)
[![GitHub](https://img.shields.io/github/license/EspenAlbert/pytest-model-lib)](https://github.com/EspenAlbert/pytest-model-lib)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://espenalbert.github.io/pytest-model-lib/)

Pytest plugin for [model-lib](https://github.com/EspenAlbert/model-lib) providing reusable fixtures and test utilities.

## Installation

```bash
pip install pytest-model-lib
```

The plugin is auto-discovered by pytest via the `pytest11` entry point -- no `conftest.py` registration needed.

## Fixtures

### `static_env_vars`

Creates a `StaticSettings` instance backed by a temporary directory and sets `STATIC_DIR` / `CACHE_DIR` environment variables via `monkeypatch`.

```python
def test_something(static_env_vars):
    assert static_env_vars.STATIC_DIR.exists()
    assert static_env_vars.CACHE_DIR.exists()
```

## Helpers

### `skip_unless_env`

Returns the value of an environment variable, or skips the test if it is not set.

```python
from pytest_model_lib import skip_unless_env

@pytest.fixture
def api_key():
    return skip_unless_env("API_KEY")
```

## Documentation

Full documentation: [espenalbert.github.io/pytest-model-lib](https://espenalbert.github.io/pytest-model-lib/)
