<!-- === DO_NOT_EDIT: pkg-ext header === -->
# __ROOT__

<!-- === OK_EDIT: pkg-ext header === -->

<!-- === DO_NOT_EDIT: pkg-ext symbols === -->
- [`skip_unless_env`](#skip_unless_env_def)
- [`static_env_vars`](#static_env_vars_def)
<!-- === OK_EDIT: pkg-ext symbols === -->

<!-- === DO_NOT_EDIT: pkg-ext symbol_details_header === -->
## Symbol Details
<!-- === OK_EDIT: pkg-ext symbol_details_header === -->

<!-- === DO_NOT_EDIT: pkg-ext skip_unless_env_def === -->
<a id="skip_unless_env_def"></a>

### function: `skip_unless_env`
- [source](../../pytest_model_lib/plugin.py#L7)
> **Since:** unreleased

```python
def skip_unless_env(env_var: str) -> str:
    ...
```

Returns the env var value or skips the test/fixture.

### Changes

| Version | Change |
|---------|--------|
| unreleased | Made public |
<!-- === OK_EDIT: pkg-ext skip_unless_env_def === -->
<!-- === DO_NOT_EDIT: pkg-ext static_env_vars_def === -->
<a id="static_env_vars_def"></a>

### function: `static_env_vars`
- [source](../../pytest_model_lib/plugin.py#L19)
> **Since:** unreleased

```python
def static_env_vars(tmp_path, monkeypatch) -> StaticSettings:
    ...
```

### Changes

| Version | Change |
|---------|--------|
| unreleased | Made public |
<!-- === OK_EDIT: pkg-ext static_env_vars_def === -->