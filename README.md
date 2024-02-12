# Python cli application reference design

![Static Badge](https://img.shields.io/badge/python-3.8-blue)

This repository contains the skeleton for the CLI Python-based application, designed in accordance with best practice,
including:

* Fully-defined command-line interface
* Modular design
* Usage of common OOP patterns and best practice
* Unit-tests
* Documented API


# Installation

```shell
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

# Testing

```shell
pytest
python3 app.py -o test.txt
```

# Linting

flake8 is a popular linter that comments on the style of code in relation to the PEP 8

```shell
flake8 --config flake8
```

