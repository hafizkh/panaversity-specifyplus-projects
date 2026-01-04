# Calculator Panaversity

A modern, feature-rich calculator with both CLI and Web UI interfaces. Built with Python, FastAPI, and vanilla JavaScript.

## Features

- **Dual Interface**: Use via command line or beautiful web UI
- **Basic Operations**: Addition, subtraction, multiplication, division
- **Advanced Operations**: Power, modulo, square root
- **Modern Web UI**: Dark theme, keyboard support, responsive design
- **REST API**: Full API with OpenAPI documentation
- **Type Safe**: Strict type hints with mypy validation
- **Well Tested**: 140+ tests with 88%+ coverage

## Quick Start

### Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd calculator_panaversity

# Install dependencies
uv sync
```

### Usage

#### Command Line Interface

```bash
# Basic arithmetic
uv run calc 5 + 3          # 8
uv run calc 10 - 4         # 6
uv run calc 6 "*" 7        # 42 (quote * to prevent shell expansion)
uv run calc 20 / 4         # 5

# Advanced operations
uv run calc 2 ^ 8          # 256 (power)
uv run calc 17 % 5         # 2 (modulo)
uv run calc sqrt 16        # 4 (square root)

# Negative numbers (use -- separator)
uv run calc -- -5 + 3      # -2

# Help
uv run calc --help
uv run calc --version
```

#### Web UI

```bash
# Start the web server
uv run calc-web

# Open in browser
# http://localhost:8000
```

The web UI features:
- Modern dark theme with accent colors
- Keyboard support (type numbers and operators)
- Click animations and hover effects
- Expression history display
- Error handling with visual feedback
- Responsive design for mobile devices

#### REST API

When the web server is running, you can also use the REST API directly:

```bash
# Calculate
curl -X POST http://localhost:8000/api/calculate \
  -H "Content-Type: application/json" \
  -d '{"operand1": 5, "operator": "+", "operand2": 3}'

# Response: {"success": true, "result": 8, "display": "8"}

# Square root (unary operation)
curl -X POST http://localhost:8000/api/calculate \
  -H "Content-Type: application/json" \
  -d '{"operand1": 16, "operator": "sqrt"}'

# List operators
curl http://localhost:8000/api/operators

# Health check
curl http://localhost:8000/api/health
```

API documentation is available at http://localhost:8000/docs (Swagger UI).

## Project Structure

```
calculator_panaversity/
├── src/
│   ├── calculator/           # Core calculator logic
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── cli.py            # CLI interface
│   │   ├── errors.py         # Custom exceptions
│   │   ├── formatter.py      # Result formatting
│   │   └── operations/       # Math operations
│   │       ├── __init__.py   # Operation registry
│   │       ├── basic.py      # +, -, *, /
│   │       └── advanced.py   # ^, %, sqrt
│   ├── api/                  # REST API backend
│   │   ├── __init__.py
│   │   ├── main.py           # FastAPI application
│   │   ├── routes.py         # API endpoints
│   │   └── schemas.py        # Pydantic models
│   └── frontend/             # Web UI
│       ├── index.html
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── app.js
├── tests/
│   ├── unit/                 # Unit tests
│   ├── integration/          # Integration tests
│   └── api/                  # API tests
├── specs/                    # Feature specifications
├── pyproject.toml            # Project configuration
└── README.md
```

## Supported Operations

| Operator | Type   | Description    | Example           |
|----------|--------|----------------|-------------------|
| `+`      | Binary | Addition       | `5 + 3` → `8`     |
| `-`      | Binary | Subtraction    | `10 - 4` → `6`    |
| `*`      | Binary | Multiplication | `6 * 7` → `42`    |
| `/`      | Binary | Division       | `20 / 4` → `5`    |
| `^`      | Binary | Power          | `2 ^ 8` → `256`   |
| `%`      | Binary | Modulo         | `17 % 5` → `2`    |
| `sqrt`   | Unary  | Square root    | `sqrt 16` → `4`   |

## Error Handling

The calculator provides clear error messages:

| Error               | Exit Code | Example                    |
|---------------------|-----------|----------------------------|
| Invalid number      | 1         | `calc abc + 3`             |
| Invalid operator    | 1         | `calc 5 @ 3`               |
| Missing operand     | 1         | `calc 5 +`                 |
| Division by zero    | 2         | `calc 10 / 0`              |
| Negative square root| 2         | `calc sqrt -4`             |

## Development

### Run Tests

```bash
# All tests
uv run pytest

# With coverage
uv run pytest --cov=src --cov-report=term-missing

# Specific test file
uv run pytest tests/unit/test_basic_ops.py

# API tests only
uv run pytest tests/api/
```

### Code Quality

```bash
# Format code
uv run ruff format

# Lint code
uv run ruff check

# Fix linting issues
uv run ruff check --fix

# Type check
uv run mypy src/

# All checks
uv run ruff format && uv run ruff check && uv run mypy src/ && uv run pytest
```

### Code Standards

- **Type Hints**: Strict typing enforced with mypy
- **Linting**: Ruff with pycodestyle, pyflakes, isort, bugbear, pydocstyle
- **Testing**: pytest with 80%+ coverage requirement
- **Documentation**: Google-style docstrings

## Architecture

### Operation Registry Pattern

Operations are registered using decorators, making it easy to add new operations:

```python
from calculator.operations import register_binary

@register_binary("**")
def double_power(a: float, b: float) -> float:
    """Raise a to the power of b, then square it."""
    return (a ** b) ** 2
```

### Error Hierarchy

```
CalculatorError (base)
├── InvalidNumberError      (exit code 1)
├── InvalidOperatorError    (exit code 1)
├── MissingOperandError     (exit code 1)
├── DivisionByZeroError     (exit code 2)
├── OverflowError           (exit code 2)
└── NegativeSqrtError       (exit code 2)
```

### API Endpoints

| Method | Endpoint          | Description              |
|--------|-------------------|--------------------------|
| GET    | `/`               | Serve web UI             |
| GET    | `/api/health`     | Health check             |
| GET    | `/api/operators`  | List available operators |
| POST   | `/api/calculate`  | Perform calculation      |

## Technologies

- **Python 3.11+**: Core language
- **FastAPI**: REST API framework
- **Uvicorn**: ASGI server
- **Pydantic**: Data validation
- **pytest**: Testing framework
- **mypy**: Static type checking
- **ruff**: Linting and formatting
- **uv**: Package management

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Ensure all checks pass: `uv run ruff format && uv run ruff check && uv run mypy src/ && uv run pytest`
5. Submit a pull request
