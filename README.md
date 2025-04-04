# LeanAlgo

A Python project managed with Poetry, using Pydantic for data validation and typing. This project also integrates with QuantConnect Lean for algorithmic trading.

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

# Or use the installed entry point
poetry run leanalgo
```

## Using QuantConnect Lean

This project integrates with QuantConnect Lean for algorithmic trading. The following tools are available:

### Lean CLI

Lean CLI is installed and can be used to create and manage QuantConnect projects:

```bash
# Create a new QuantConnect project
lean project-create

# Run a local Jupyter Lab environment
lean research

# Backtest a project locally using Docker
lean backtest
```

### Example Algorithm

An example algorithm is provided in `leanalgo/algorithm.py`. This is a basic trading algorithm that:

1. Buys AAPL when the price is above the 14-day Simple Moving Average
2. Sells AAPL when the price drops below the 14-day Simple Moving Average

### QuantConnect Autocomplete

For Python autocomplete with QuantConnect, we have installed the `quantconnect-stubs` package.

To use autocomplete in your own files, add this import to the top of your Python file:

```python
from AlgorithmImports import *
```

## Project Structure

- `leanalgo/models.py` - Contains Pydantic data models
- `leanalgo/main.py` - Main application entry point
- `leanalgo/algorithm.py` - Example QuantConnect algorithm

## Using Pydantic

This project uses Pydantic for data validation and type checking. Example usage:

```python
from leanalgo.models import UserData

# Create a validated user object
user = UserData(
    id=1,
    name="John Doe",
    email="john.doe@example.com",
    tags=["user", "premium"]
)

# Access attributes with full type hints
user_name = user.name
```
