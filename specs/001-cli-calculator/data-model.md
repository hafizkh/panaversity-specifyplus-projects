# Data Model: CLI Calculator

**Feature**: 001-cli-calculator
**Date**: 2026-01-04

## Overview

This document defines the data structures used in the CLI Calculator. As a stateless CLI application, there is no persistent storage. All entities exist only during request processing.

## Entities

### 1. Expression

Represents a mathematical calculation to be performed.

**Attributes**:
| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| left_operand | float | Yes (binary) | First operand for binary operations |
| operator | str | Yes | Operation symbol (+, -, *, /, ^, %, sqrt) |
| right_operand | float | Yes (binary) | Second operand for binary operations |

**Variants**:
- **BinaryExpression**: Two operands with operator between (e.g., `5 + 3`)
- **UnaryExpression**: Single operand with operator prefix (e.g., `sqrt 16`)

**Validation Rules**:
- Operands must be valid numeric values (int or float)
- Operator must be one of the supported operators
- Binary operations require exactly 2 operands
- Unary operations require exactly 1 operand

### 2. Result

Represents the computed value of an expression.

**Attributes**:
| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| value | float | Yes | Computed numeric result |
| display_value | str | Yes | Formatted string for output |

**Formatting Rules**:
- Whole numbers display without decimal point
- Decimals show up to 10 significant digits
- Trailing zeros are removed
- Very large/small numbers use scientific notation

### 3. CalculatorError

Represents an error condition during parsing or calculation.

**Attributes**:
| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| error_type | str | Yes | Category of error (see hierarchy) |
| message | str | Yes | Human-readable error description |
| exit_code | int | Yes | Unix exit code (1 or 2) |

**Error Hierarchy**:
```
CalculatorError
├── InvalidNumberError (exit_code: 1)
│   └── message: "Invalid number: {value}"
├── InvalidOperatorError (exit_code: 1)
│   └── message: "Invalid operator: {operator}"
├── MissingOperandError (exit_code: 1)
│   └── message: "Missing operand: expected {expected} arguments"
├── DivisionByZeroError (exit_code: 2)
│   └── message: "Division by zero is not allowed"
└── OverflowError (exit_code: 2)
    └── message: "Result exceeds maximum representable value"
```

## Type Definitions (Python)

```python
from typing import Union
from dataclasses import dataclass
from enum import Enum

class Operator(Enum):
    """Supported mathematical operators."""
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    POWER = "^"
    MODULO = "%"
    SQRT = "sqrt"

@dataclass
class BinaryExpression:
    """Binary mathematical expression."""
    left: float
    operator: Operator
    right: float

@dataclass
class UnaryExpression:
    """Unary mathematical expression."""
    operator: Operator
    operand: float

Expression = Union[BinaryExpression, UnaryExpression]

@dataclass
class Result:
    """Calculation result with formatted output."""
    value: float
    display_value: str

class CalculatorError(Exception):
    """Base exception for calculator errors."""
    exit_code: int = 1

class InvalidNumberError(CalculatorError):
    """Raised when operand is not a valid number."""
    pass

class InvalidOperatorError(CalculatorError):
    """Raised when operator is not recognized."""
    pass

class MissingOperandError(CalculatorError):
    """Raised when required operands are missing."""
    pass

class DivisionByZeroError(CalculatorError):
    """Raised when division or modulo by zero attempted."""
    exit_code: int = 2

class OverflowError(CalculatorError):
    """Raised when result exceeds representable limits."""
    exit_code: int = 2
```

## State Transitions

The calculator is stateless. Each invocation follows this flow:

```
[CLI Args] → Parse → [Expression] → Calculate → [Result] → Format → [Output]
                ↓                        ↓
           [ParseError]            [CalcError]
                ↓                        ↓
            [stderr]                 [stderr]
```

## Data Flow

```
Input (argv)
    │
    ├─ "--help" ──────────────────────────────────→ Help text (stdout)
    │
    ├─ No args ───────────────────────────────────→ Usage text (stdout)
    │
    └─ Expression args
           │
           ├─ Invalid number ─────────────────────→ Error (stderr, exit 1)
           ├─ Invalid operator ───────────────────→ Error (stderr, exit 1)
           ├─ Missing operand ────────────────────→ Error (stderr, exit 1)
           │
           └─ Valid expression
                  │
                  ├─ Division by zero ────────────→ Error (stderr, exit 2)
                  ├─ Overflow ────────────────────→ Error (stderr, exit 2)
                  │
                  └─ Success ─────────────────────→ Result (stdout, exit 0)
```

## Relationships

```
┌─────────────────┐
│   CLI Input     │
└────────┬────────┘
         │ parses to
         ▼
┌─────────────────┐
│   Expression    │
│  (Binary/Unary) │
└────────┬────────┘
         │ evaluates to
         ▼
┌─────────────────┐     ┌─────────────────┐
│     Result      │ or  │ CalculatorError │
└─────────────────┘     └─────────────────┘
```
