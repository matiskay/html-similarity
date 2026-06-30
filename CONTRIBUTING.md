## Setup

This project uses [uv](https://docs.astral.sh/uv/) to manage the Python
version and dependencies. Run the bootstrap script to create a `.venv` and
install the package along with its dev dependencies (pytest, flake8):

```
./bootstrap.sh
```

## Create a new version in PyPI

```
uv build
uv publish
```


## Run tests

```
uv run pytest -v tests/
```


## Run Flake8

```
uv run flake8 html_similarity
```
