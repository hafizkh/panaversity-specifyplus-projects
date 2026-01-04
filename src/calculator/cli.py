"""Command-line interface for the calculator.

This module provides the CLI argument parsing and main entry point
for the calculator application.
"""

import argparse
import sys

import calculator.operations.advanced  # noqa: F401

# Import operations to register them
import calculator.operations.basic  # noqa: F401
from calculator import __version__
from calculator.errors import (
    CalculatorError,
    InvalidNumberError,
    InvalidOperatorError,
    MissingOperandError,
)
from calculator.formatter import format_result
from calculator.operations import (
    get_binary_operation,
    get_unary_operation,
    is_binary_operator,
    is_unary_operator,
)

HELP_TEXT = """Calculator - A command-line calculator

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
"""

USAGE_TEXT = """Usage: calc <operand1> <operator> <operand2>
       calc <operator> <operand>
       calc --help

Examples: calc 5 + 3, calc sqrt 16, calc 2 ^ 8
"""


def parse_number(value: str) -> float:
    """Parse a string as a number.

    Args:
        value: The string to parse.

    Returns:
        The parsed float value.

    Raises:
        InvalidNumberError: If the value cannot be parsed as a number.
    """
    try:
        return float(value)
    except ValueError:
        raise InvalidNumberError(value) from None


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the calculator CLI.

    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog="calc",
        description="A command-line calculator",
        add_help=False,
    )
    parser.add_argument(
        "--help",
        "-h",
        action="store_true",
        dest="show_help",
        help="Show help message and exit",
    )
    parser.add_argument(
        "--version",
        "-v",
        action="store_true",
        dest="show_version",
        help="Show version and exit",
    )
    parser.add_argument(
        "args",
        nargs="*",
        help="Calculation arguments",
    )
    return parser


def execute_calculation(args: list[str]) -> str:
    """Execute a calculation based on the provided arguments.

    Args:
        args: List of calculation arguments (operands and operator).

    Returns:
        The formatted result as a string.

    Raises:
        MissingOperandError: If there are not enough arguments.
        InvalidOperatorError: If the operator is not recognized.
        InvalidNumberError: If an operand cannot be parsed.
        CalculatorError: For any calculation errors.
    """
    if not args:
        raise MissingOperandError(2, 0)

    # Check for unary operation (e.g., sqrt 16)
    if len(args) == 2 and is_unary_operator(args[0]):
        operator = args[0]
        operand = parse_number(args[1])
        operation = get_unary_operation(operator)
        if operation is None:
            raise InvalidOperatorError(operator)
        result_value = operation(operand)
        return format_result(result_value).display_value

    # Check for binary operation (e.g., 5 + 3)
    if len(args) == 3:
        left = parse_number(args[0])
        operator = args[1]
        right = parse_number(args[2])

        if not is_binary_operator(operator):
            raise InvalidOperatorError(operator)

        binary_operation = get_binary_operation(operator)
        if binary_operation is None:
            raise InvalidOperatorError(operator)

        result_value = binary_operation(left, right)
        return format_result(result_value).display_value

    # Check for unary with wrong args
    if len(args) == 1:
        if is_unary_operator(args[0]):
            raise MissingOperandError(2, 1)
        # Might be trying binary with missing args
        raise MissingOperandError(3, 1)

    if len(args) == 2:
        # Could be binary with missing operand
        if is_binary_operator(args[1]):
            raise MissingOperandError(3, 2)
        # Could be invalid unary
        if not is_unary_operator(args[0]):
            raise InvalidOperatorError(args[0])
        raise MissingOperandError(2, len(args))

    raise MissingOperandError(3, len(args))


def main(argv: list[str] | None = None) -> int:
    """Main entry point for the calculator CLI.

    Args:
        argv: Command-line arguments (defaults to sys.argv[1:]).

    Returns:
        Exit code (0 for success, non-zero for errors).
    """
    if argv is None:
        argv = sys.argv[1:]

    parser = create_parser()
    parsed = parser.parse_args(argv)

    # Handle help
    if parsed.show_help:
        print(HELP_TEXT)
        return 0

    # Handle version
    if parsed.show_version:
        print(f"calc {__version__}")
        return 0

    # Handle no arguments
    if not parsed.args:
        print(USAGE_TEXT)
        return 0

    # Execute calculation
    try:
        result = execute_calculation(parsed.args)
        print(result)
        return 0
    except CalculatorError as e:
        print(f"Error: {e}", file=sys.stderr)
        return e.exit_code


if __name__ == "__main__":
    sys.exit(main())
