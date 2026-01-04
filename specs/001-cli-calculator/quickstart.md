# Quickstart: CLI Calculator

**Feature**: 001-cli-calculator
**Date**: 2026-01-04

## Prerequisites

- Python 3.11 or higher
- uv package manager

## Installation

### 1. Clone and Setup

```bash
# Clone the repository
git clone <repository-url>
cd calculator_panaversity

# Install uv if not already installed
# See: https://github.com/astral-sh/uv

# Create virtual environment and install dependencies
uv sync
```

### 2. Verify Installation

```bash
# Run the calculator
uv run calc 2 + 2
# Expected output: 4
```

## Usage Examples

### Basic Arithmetic

```bash
# Addition
uv run calc 5 + 3
# Output: 8

# Subtraction
uv run calc 10 - 4
# Output: 6

# Multiplication (note: quote the *)
uv run calc 6 "*" 7
# Output: 42

# Division
uv run calc 20 / 4
# Output: 5
```

### Advanced Operations

```bash
# Power/Exponentiation
uv run calc 2 ^ 8
# Output: 256

# Modulo
uv run calc 17 % 5
# Output: 2

# Square Root
uv run calc sqrt 16
# Output: 4
```

### Floating-Point Numbers

```bash
uv run calc 3.14 "*" 2
# Output: 6.28

uv run calc sqrt 2
# Output: 1.4142135624
```

### Negative Numbers

```bash
# Use -- to separate options from arguments
uv run calc -- -5 + 3
# Output: -2

# Or quote the negative number
uv run calc "-5" + 3
# Output: -2
```

### Help

```bash
uv run calc --help
# Displays usage information and examples
```

## Development

### Run Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src/calculator

# Run specific test file
uv run pytest tests/unit/test_basic_ops.py
```

### Code Quality

```bash
# Format code
uv run ruff format

# Lint code
uv run ruff check

# Type check
uv run mypy src/
```

### Pre-commit (All Checks)

```bash
uv run ruff format && uv run ruff check && uv run mypy src/ && uv run pytest
```

## Common Issues

### Multiplication Not Working

**Problem**: `calc 6 * 7` returns unexpected results or errors.

**Solution**: The shell interprets `*` as a glob. Quote it:
```bash
uv run calc 6 "*" 7
```

### Negative Number as First Argument

**Problem**: `calc -5 + 3` interprets `-5` as a flag.

**Solution**: Use `--` to end option parsing:
```bash
uv run calc -- -5 + 3
```

### Module Not Found

**Problem**: `ModuleNotFoundError: No module named 'calculator'`

**Solution**: Run via `uv run` or ensure the virtual environment is activated:
```bash
uv run calc 5 + 3
# or
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
calc 5 + 3
```

## Next Steps

1. Read the [CLI Interface Contract](contracts/cli-interface.md) for complete documentation
2. Review the [Data Model](data-model.md) for implementation details
3. Check the [Implementation Plan](plan.md) for architecture decisions
