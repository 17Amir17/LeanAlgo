# LeanAlgo

A Python project managed with Poetry.

## Setup

```bash
# Install dependencies
poetry install

# Activate the virtual environment
poetry env activate
source $(poetry env info --path)/bin/activate
```

## Running the application

After setting up the environment, you can run the application using:

```bash
# Run directly with Python
python -m leanalgo.main

# Or use the installed entry point (after installing with --no-root)
poetry install
poetry run leanalgo
```
