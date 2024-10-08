# Python 3.11.x + Makefile template

## Pre-requisites
* `Python 3.11.x`

### Initial setup

We will use python 3.11.x for all code.

To setup virtual environment and install all required dependencies use:
```bash
make setup
```

#### Freeze dependencies

Run the following command to freeze all dependencies:

```bash
pip freeze > requirements.txt
```

### Run Flask 

To run flaks server locally execute the following command:
```bash
make run
```


### Code Formatter

[Black](https://github.com/psf/black) will be used as a default code formatter.

To format current folder use:

```bash
make code_format
```

### Linter

As a linter we will use [Flake8](https://flake8.pycqa.org/en/latest/)

To run linter use:

```bash
make lint
```

### Unit tests

For unit tests we will use [pytest](https://docs.pytest.org/en/8.2.x/)
For code coverage we will use [coverage]().

To run all unit-tests with code coverage use:

```bash
make test
```
