# CLI Interface Contract: Calculator

**Feature**: 001-cli-calculator
**Date**: 2026-01-04
**Version**: 1.0.0

## Overview

This document defines the command-line interface contract for the calculator application.

## Command Syntax

```bash
calc [OPTIONS] [EXPRESSION]
```

### Options

| Option | Short | Description |
|--------|-------|-------------|
| `--help` | `-h` | Display help message and exit |
| `--version` | `-v` | Display version information and exit |

### Expression Formats

#### Binary Operations

```bash
calc <operand1> <operator> <operand2>
```

| Operator | Symbol | Example | Result |
|----------|--------|---------|--------|
| Addition | `+` | `calc 5 + 3` | `8` |
| Subtraction | `-` | `calc 10 - 4` | `6` |
| Multiplication | `*` | `calc 6 * 7` | `42` |
| Division | `/` | `calc 20 / 4` | `5` |
| Power | `^` | `calc 2 ^ 8` | `256` |
| Modulo | `%` | `calc 17 % 5` | `2` |

#### Unary Operations

```bash
calc <operator> <operand>
```

| Operator | Keyword | Example | Result |
|----------|---------|---------|--------|
| Square Root | `sqrt` | `calc sqrt 16` | `4` |

## Input Specification

### Operands

- **Type**: Numeric (integer or floating-point)
- **Format**: Standard decimal notation or scientific notation
- **Range**: IEEE 754 double precision (-1.7976931348623157e+308 to 1.7976931348623157e+308)
- **Examples**: `5`, `-3.14`, `1e10`, `-2.5e-3`

### Operators

| Symbol | Operation | Arity |
|--------|-----------|-------|
| `+` | Addition | Binary |
| `-` | Subtraction | Binary |
| `*` | Multiplication | Binary |
| `/` | Division | Binary |
| `^` | Exponentiation | Binary |
| `%` | Modulo | Binary |
| `sqrt` | Square root | Unary |

## Output Specification

### Success Output

- **Stream**: stdout
- **Format**: Numeric result only (no labels or units)
- **Precision**: Up to 10 significant decimal digits
- **Trailing zeros**: Removed
- **Newline**: Appended after result

**Examples**:
```
$ calc 5 + 3
8

$ calc 10 / 4
2.5

$ calc sqrt 2
1.4142135624
```

### Error Output

- **Stream**: stderr
- **Format**: `Error: <message>`
- **Newline**: Appended after message

**Examples**:
```
$ calc abc + 3
Error: Invalid number: abc

$ calc 5 @ 3
Error: Invalid operator: @

$ calc 10 / 0
Error: Division by zero is not allowed
```

### Help Output

- **Stream**: stdout
- **Trigger**: `--help` or `-h` flag, or no arguments

```
Calculator - A command-line calculator

Usage:
  calc <operand1> <operator> <operand2>    Perform binary operation
  calc <operator> <operand>                Perform unary operation
  calc --help                              Show this help message

Binary Operators:
  +    Addition         (e.g., calc 5 + 3)
  -    Subtraction      (e.g., calc 10 - 4)
  *    Multiplication   (e.g., calc 6 * 7)
  /    Division         (e.g., calc 20 / 4)
  ^    Power            (e.g., calc 2 ^ 8)
  %    Modulo           (e.g., calc 17 % 5)

Unary Operators:
  sqrt Square root      (e.g., calc sqrt 16)

Notes:
  - Use quotes around * to prevent shell expansion: calc 6 "*" 7
  - For negative first operand, use: calc -- -5 + 3

Examples:
  calc 5 + 3          # Returns: 8
  calc 2 ^ 10         # Returns: 1024
  calc sqrt 144       # Returns: 12
```

## Exit Codes

| Code | Meaning | Trigger |
|------|---------|---------|
| 0 | Success | Valid calculation completed |
| 1 | Input error | Invalid number, operator, or missing operand |
| 2 | Calculation error | Division by zero, overflow |

## Error Messages

| Error Type | Message Format | Exit Code |
|------------|----------------|-----------|
| Invalid number | `Invalid number: {value}` | 1 |
| Invalid operator | `Invalid operator: {operator}` | 1 |
| Missing operand | `Missing operand: expected {n} arguments, got {m}` | 1 |
| Division by zero | `Division by zero is not allowed` | 2 |
| Overflow | `Result exceeds maximum representable value` | 2 |
| Negative sqrt | `Cannot compute square root of negative number: {value}` | 2 |

## Shell Considerations

### Multiplication Operator

The `*` character is interpreted as a glob by most shells. Users must escape or quote it:

```bash
# These work:
calc 6 "*" 7
calc 6 '*' 7
calc 6 \* 7

# This may fail (shell expands * to filenames):
calc 6 * 7
```

### Negative First Operand

The `-` prefix on the first operand may be interpreted as a flag. Use `--` to separate:

```bash
# These work:
calc -- -5 + 3
calc "-5" + 3

# This may fail:
calc -5 + 3
```

## Version Information

```
$ calc --version
calc 1.0.0
```
