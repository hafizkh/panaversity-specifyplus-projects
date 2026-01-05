# Calculator Panaversity

A modern, feature-rich calculator with both CLI and Web UI interfaces. Built with Python, FastAPI, and vanilla JavaScript.

## 🌐 Live Demo

**Try it now:** [https://nice-agna-hafizteam-8f05be97.koyeb.app](https://nice-agna-hafizteam-8f05be97.koyeb.app)

## Features

- **Dual Interface**: Use via command line or beautiful web UI
- **Simple & Scientific Modes**: Toggle between basic and advanced calculator
- **Basic Operations**: Addition, subtraction, multiplication, division
- **Scientific Operations**: Trigonometry (sin, cos, tan), logarithms (log, ln), powers, roots, factorial, and more
- **Modern Web UI**: Glassmorphism design, keyboard support, responsive layout
- **REST API**: Full API with OpenAPI documentation
- **Type Safe**: Strict type hints with mypy validation
- **Well Tested**: 140+ tests with 88%+ coverage

## Screenshots

### Simple Mode
- Clean, minimal interface
- Basic arithmetic operations
- AC, CE, and backspace buttons

### Scientific Mode
- 20 scientific functions
- Trigonometric functions (degrees)
- Logarithms, exponentials, factorial
- Constants (π, e)

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

Or visit the live version: [https://nice-agna-hafizteam-8f05be97.koyeb.app](https://nice-agna-hafizteam-8f05be97.koyeb.app)

The web UI features:
- **Mode Toggle**: Switch between Simple and Scientific calculators
- Modern glassmorphism design with animated background
- Keyboard support (type numbers and operators)
- Press **Tab** to toggle between Simple/Scientific modes
- Expression history display
- Error handling with visual feedback
- Responsive design for mobile devices
- Mode preference saved to localStorage

#### REST API

When the web server is running, you can also use the REST API directly:

```bash
# Calculate
curl -X POST https://nice-agna-hafizteam-8f05be97.koyeb.app/api/calculate \
  -H "Content-Type: application/json" \
  -d '{"operand1": 5, "operator": "+", "operand2": 3}'

# Response: {"success": true, "result": 8, "display": "8"}

# Scientific functions
curl -X POST https://nice-agna-hafizteam-8f05be97.koyeb.app/api/calculate \
  -H "Content-Type: application/json" \
  -d '{"operand1": 45, "operator": "sin"}'

# Response: {"success": true, "result": 0.7071067811865476, "display": "0.7071067812"}

# List operators
curl https://nice-agna-hafizteam-8f05be97.koyeb.app/api/operators

# Health check
curl https://nice-agna-hafizteam-8f05be97.koyeb.app/api/health
```

API documentation is available at [https://nice-agna-hafizteam-8f05be97.koyeb.app/docs](https://nice-agna-hafizteam-8f05be97.koyeb.app/docs) (Swagger UI).

## Supported Operations

### Basic Operations

| Operator | Type   | Description    | Example           |
|----------|--------|----------------|-------------------|
| `+`      | Binary | Addition       | `5 + 3` → `8`     |
| `-`      | Binary | Subtraction    | `10 - 4` → `6`    |
| `*`      | Binary | Multiplication | `6 * 7` → `42`    |
| `/`      | Binary | Division       | `20 / 4` → `5`    |
| `^`      | Binary | Power          | `2 ^ 8` → `256`   |
| `%`      | Binary | Modulo         | `17 % 5` → `2`    |

### Scientific Operations

| Operator | Type  | Description         | Example              |
|----------|-------|---------------------|----------------------|
| `sin`    | Unary | Sine (degrees)      | `sin(90)` → `1`      |
| `cos`    | Unary | Cosine (degrees)    | `cos(0)` → `1`       |
| `tan`    | Unary | Tangent (degrees)   | `tan(45)` → `1`      |
| `asin`   | Unary | Arc sine (degrees)  | `asin(1)` → `90`     |
| `acos`   | Unary | Arc cosine (degrees)| `acos(1)` → `0`      |
| `atan`   | Unary | Arc tangent (degrees)| `atan(1)` → `45`    |
| `log`    | Unary | Log base 10         | `log(100)` → `2`     |
| `ln`     | Unary | Natural log         | `ln(e)` → `1`        |
| `exp`    | Unary | e^x                 | `exp(1)` → `2.718`   |
| `sqrt`   | Unary | Square root         | `sqrt(16)` → `4`     |
| `sqr`    | Unary | Square (x²)         | `sqr(5)` → `25`      |
| `cbrt`   | Unary | Cube root           | `cbrt(27)` → `3`     |
| `inv`    | Unary | Reciprocal (1/x)    | `inv(4)` → `0.25`    |
| `abs`    | Unary | Absolute value      | `abs(-5)` → `5`      |
| `neg`    | Unary | Negate (±)          | `neg(5)` → `-5`      |
| `fact`   | Unary | Factorial (n!)      | `fact(5)` → `120`    |

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `0-9` | Input numbers |
| `+`, `-`, `*`, `/`, `^`, `%` | Operators |
| `.` | Decimal point |
| `Enter` or `=` | Calculate |
| `Backspace` | Delete last digit |
| `Escape` | Clear all (AC) |
| `Delete` | Clear entry (CE) |
| `Tab` | Toggle Simple/Scientific mode |
| `s` | sin (Scientific mode) |
| `c` | cos (Scientific mode) |
| `t` | tan (Scientific mode) |
| `l` | log (Scientific mode) |
| `n` | ln (Scientific mode) |
| `r` | sqrt (Scientific mode) |
| `p` | π (Scientific mode) |
| `e` | e constant (Scientific mode) |
| `!` | factorial (Scientific mode) |

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
│   │       ├── advanced.py   # ^, %, sqrt
│   │       └── scientific.py # sin, cos, log, etc.
│   ├── api/                  # REST API backend
│   │   ├── __init__.py
│   │   ├── main.py           # FastAPI application
│   │   ├── routes.py         # API endpoints
│   │   └── schemas.py        # Pydantic models
│   └── frontend/             # Web UI
│       ├── index.html
│       ├── css/
│       │   └── style.css     # Glassmorphism styles
│       └── js/
│           └── app.js        # Calculator logic
├── tests/
│   ├── unit/                 # Unit tests
│   ├── integration/          # Integration tests
│   └── api/                  # API tests
├── app.py                    # Deployment entry point
├── Dockerfile                # Docker configuration
├── Procfile                  # Railway/Heroku config
├── render.yaml               # Render config
├── pyproject.toml            # Project configuration
└── README.md
```

## Error Handling

The calculator provides clear error messages:

| Error               | Exit Code | Example                    |
|---------------------|-----------|----------------------------|
| Invalid number      | 1         | `calc abc + 3`             |
| Invalid operator    | 1         | `calc 5 @ 3`               |
| Missing operand     | 1         | `calc 5 +`                 |
| Division by zero    | 2         | `calc 10 / 0`              |
| Negative square root| 2         | `calc sqrt -4`             |
| Domain error        | 2         | `calc asin 2`              |

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

## Deployment

The app is deployed on Koyeb and can be deployed to other platforms:

### Docker

```bash
docker build -t calculator-panaversity .
docker run -p 8000:8000 calculator-panaversity
```

### Supported Platforms

- **Koyeb** (current): [Live Demo](https://nice-agna-hafizteam-8f05be97.koyeb.app)
- **Render**: Use `render.yaml`
- **Railway**: Use `Procfile`
- **Docker**: Use `Dockerfile`

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
