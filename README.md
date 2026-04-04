# basic-py-proj

This is just a hello-world style project to clone from for me to begin small python projects.

## Setup

I use [mise](https://mise.jdx.dev/) to manage tool versions and [uv](https://docs.astral.sh/uv/) for dependency management.

Install mise, then run:
```bash
mise install        # installs python and uv
uv sync --group dev # installs all dependencies
```

## Development Setup

To run the main function:
```bash
uv run say_hello
```

Run the tests:
```bash
uv run pytest # -v for verbose
```
>[!NOTE]
> The test configuration settings are in the `pyproject.toml` file.

This project uses [Ruff](https://docs.astral.sh/ruff/) as a Python linter and code formatter.

To use it run:
```bash
# Check code
uv run ruff check

# Check code and fix
uv run ruff check --fix

# Format code
uv run ruff format
```

## TODOS:

Run these things in a docker container.
