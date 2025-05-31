# basic-py-proj

This is just a hello-world style project to clone from for me to begin small python projects.

## Setup
I use `asdf` to manage versions of things. This uses a `.tool-versions` file to define the versions that are used


## Steps to recreate

```bash
poetry install
poetry add --group dev pytest
```

## Commands

```bash
poetry shell
```
Ensures you're working in an isolated environment where dependencies won't conflict with other projects or the system Python.

```bash
poetry run say_hello
```
Runs the main function

```bash
poetry run pytest -v
```
Runs the tests
