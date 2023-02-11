# levdict

This module allows to handle dictionaries keys as attributes.
It has four classes:

- ***LevDict***: The base class, it acts as a dictionary but with the added feature of treating
consists of a main class LevDict, which allows to treat dictionaries as attributes.
- ***LevDictJson***: Derived from LevDict, reads and writes ***json*** files
- ***LevDictToml***: Derived from LevDict, reads and writes ***toml*** files (depends on toml)
- ***LevDictYaml***: Derived from LevDict, reads and writes ***yaml*** files (depends on pyyaml)

and three derived classes that allow using respectively toml, json and yaml for configuration purposes.

## Installation

The module is currently in production.

    python -m pip install levdict

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
