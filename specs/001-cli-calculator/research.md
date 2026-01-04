# Research: CLI Calculator

**Feature**: 001-cli-calculator
**Date**: 2026-01-04
**Status**: Complete

## Overview

This document captures research findings and technical decisions for the CLI Calculator implementation.

## Technology Decisions

### 1. CLI Argument Parsing

**Decision**: Use `argparse` from Python standard library

**Rationale**:
- Part of Python standard library (no external dependencies)
- Mature, well-documented, battle-tested
- Native support for `--help` flag generation
- Handles positional and optional arguments cleanly
- Constitution Principle V (Simplicity) compliance

**Alternatives Considered**:
| Alternative | Why Rejected |
|-------------|--------------|
| click | External dependency; overkill for simple CLI |
| typer | External dependency; requires type hint magic |
| sys.argv parsing | More error-prone; reinventing the wheel |

### 2. Mathematical Operations

**Decision**: Use Python standard library (`math` module + operators)

**Rationale**:
- Built-in operators (`+`, `-`, `*`, `/`, `**`, `%`) for basic math
- `math.sqrt()` for square root with proper error handling
- `math.isinf()` and `math.isnan()` for overflow detection
- IEEE 754 double precision is Python's native float behavior

**Alternatives Considered**:
| Alternative | Why Rejected |
|-------------|--------------|
| decimal.Decimal | Overhead not justified; float precision sufficient |
| numpy | Heavy dependency for simple operations |
| sympy | Symbolic math not needed |

### 3. Error Handling Strategy

**Decision**: Custom exception hierarchy with structured error messages

**Rationale**:
- Clear error types enable specific handling
- Structured messages support both human and machine parsing
- Exit codes follow Unix conventions
- Constitution Principle IV (CLI-First) compliance

**Error Types**:
```
CalculatorError (base)
├── InvalidNumberError    # Non-numeric operand
├── InvalidOperatorError  # Unknown operator symbol
├── MissingOperandError   # Insufficient arguments
├── DivisionByZeroError   # Division/modulo by zero
└── OverflowError         # Result exceeds float limits
```

**Exit Codes**:
| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Invalid input (number, operator, or missing operand) |
| 2 | Mathematical error (division by zero, overflow) |

### 4. Result Formatting

**Decision**: Smart formatting with trailing zero removal

**Rationale**:
- Integer results display without decimal (e.g., `8` not `8.0`)
- Float results show up to 10 decimal places
- Trailing zeros removed for cleaner output
- Scientific notation for very large/small numbers

**Format Rules**:
1. If result is whole number → display as integer
2. If result has decimals → up to 10 significant digits
3. If result > 1e15 or < 1e-10 → scientific notation

### 5. Package Structure

**Decision**: Flat package with operations subpackage

**Rationale**:
- Single package `calculator` for simple installation
- Operations grouped in subpackage for modularity
- Clear separation: CLI → Operations → Errors
- Constitution Principle III (Modular Design) compliance

**Import Structure**:
```python
from calculator import calculate  # Main entry point
from calculator.operations import add, subtract, multiply, divide
from calculator.operations import power, modulo, sqrt
from calculator.errors import CalculatorError
```

### 6. Testing Strategy

**Decision**: Layered testing with pytest

**Rationale**:
- Unit tests for individual operations
- Integration tests for CLI end-to-end
- Parameterized tests for comprehensive coverage
- Constitution Principle II (TDD) compliance

**Test Categories**:
| Category | Purpose | Location |
|----------|---------|----------|
| Unit | Individual function correctness | tests/unit/ |
| Integration | CLI argument parsing + output | tests/integration/ |
| Edge Cases | Boundary conditions, errors | Both |

**Coverage Target**: 80% minimum (per constitution)

### 7. Development Tooling

**Decision**: uv + ruff + mypy + pytest

**Rationale**:
- `uv`: Fast, modern Python package manager (per constitution)
- `ruff`: All-in-one linter/formatter (replaces black, isort, flake8)
- `mypy`: Static type checking with strict mode
- `pytest`: Industry standard test framework

**Configuration**: All tools configured in `pyproject.toml`

## Implementation Notes

### Operator Mapping

```python
OPERATORS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '^': power,
    '**': power,  # Alternative syntax
    '%': modulo,
}

UNARY_OPERATORS = {
    'sqrt': sqrt,
}
```

### CLI Syntax

```bash
# Binary operations
calc <operand1> <operator> <operand2>
calc 5 + 3          # → 8
calc 10 / 4         # → 2.5
calc 2 ^ 8          # → 256

# Unary operations
calc <operator> <operand>
calc sqrt 16        # → 4

# Help
calc --help         # Show usage
calc                # Show brief usage
```

### Negative Number Handling

Negative numbers as first operand require special handling to distinguish from flags:
- Use `--` to separate options from arguments: `calc -- -5 + 3`
- Or enclose in quotes on some shells: `calc "-5" + 3`

## Open Questions (Resolved)

| Question | Resolution |
|----------|------------|
| How to handle `*` shell expansion? | Document in help: use quotes `"*"` or escape `\*` |
| Support expression parsing? | Out of scope; only single operation per invocation |
| Support interactive mode? | Out of scope; batch CLI only per spec |

## References

- Python argparse documentation: https://docs.python.org/3/library/argparse.html
- Python math module: https://docs.python.org/3/library/math.html
- IEEE 754 floating point: https://en.wikipedia.org/wiki/IEEE_754
