# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup

This project uses [mise](https://mise.jdx.dev/) for tool version management and [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
mise install        # install Python 3.11.13 and uv
uv sync --group dev # install all dependencies including dev
```

## Commands

```bash
uv run say_hello          # run the main entry point
uv run pytest             # run all tests with coverage
uv run pytest tests/test_main.py::test_enter_name_and_say_hello  # run a single test
uv run ruff check src tests          # lint
uv run ruff check --fix src tests    # lint and auto-fix
uv run ruff format src tests         # format
```

After making changes, run tests and linting:

```bash
uv run pytest && uv run ruff check src tests
```

## Architecture

- `src/main.py` — sole application module; `main()` is the script entry point (`say_hello` CLI command)
- `tests/test_main.py` — mirrors `src/`, uses `capsys` and `monkeypatch` for I/O testing
- Source and tests are separated (`src/` layout); hatchling is the build backend
- Coverage runs automatically with `pytest` (`--cov=src`), outputting HTML to `htmlcov/`

## Testing

Do not monkeypatch the code under test — only monkeypatch external inputs (e.g. `sys.stdin`, `builtins.input`). Patching the implementation itself defeats the purpose of the test.
