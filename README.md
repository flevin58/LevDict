# levdict

This module consists of a main class LevDict, which allows to treat dictionaries as attributes,
and three derived classes that allow using respectively toml, json and yaml for configuration purposes.

## Project Status

The module is currently in alfa release.
It is published in PyPi test repository.

## Installation

For the moment use this command:

    python -m pip install -i https://test.pypi.org/project/ levdict

## Usage

Please read the examples for an introduction.

## Project Tree Structure

    .
    ├── LICENSE
    ├── Makefile
    ├── README.md
    ├── examples
    │   ├── example1.py
    │   ├── example2.ini
    │   ├── example2.py
    │   ├── example3.py
    │   ├── example3.toml
    │   └── example3_mod.toml
    ├── pyproject.toml
    ├── src
    │   └── levdict
    │       ├── __init__.py
    │       ├── levdict_base.py
    │       ├── levdict_json.py
    │       ├── levdict_toml.py
    │       └── levdict_yaml.py
    └── tests
        ├── __init__.py
        ├── examples
        │   ├── example.toml
        │   ├── example1.toml
        │   └── nando.toml
        ├── test_basic.py
        └── test_levdict.py
