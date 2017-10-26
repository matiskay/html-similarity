## Setup

```
pip install -r requirements-dev.txt
```

## Create a new version in Pipy

```
python setup.py sdist bdist_wheel
twine upload dist/*
```


## Run tests

```
nosetests -v tests/
```


## Run Flake8

```
flake8 html_similarity
```


## References

* [Twine](https://pypi.python.org/pypi/twine)
* [How to publish your own Python Package on PyPi](
https://medium.freecodecamp.org/how-to-publish-a-pyton-package-on-pypi-a89e9522ce24)
