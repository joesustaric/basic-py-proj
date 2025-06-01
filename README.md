# basic-py-proj

This is just a hello-world style project to clone from for me to begin small python projects.

## Setup

I use `asdf` to manage versions of things.

This uses a `.tool-versions` file to define the versions of things used. Look there and install them.

Then run:
```bash
poetry install
```

## Development Setup

Ensures you're working in an isolated environment where dependencies won't conflict with other projects or the system Python.
```bash
poetry shell
```

To run the main function.
```bash
poetry run say_hello
```

Run the tests.
```bash
poetry run pytest # -v for verbose
```
>[!NOTE]
> The test configuration setting are in the `project.toml` file.
