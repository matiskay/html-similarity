## Setup

```
pip install -r requiremets-dev.txt
```

## Create a new version in Pipy

```
python setup.py sdist bdist_wheel
twine upload dist/*
```


## References

* [Twine](https://pypi.python.org/pypi/twine)

