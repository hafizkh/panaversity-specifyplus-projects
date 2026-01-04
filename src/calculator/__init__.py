"""Calculator package - A CLI calculator with basic and advanced operations."""

__version__ = "1.0.0"
__author__ = "Calculator Panaversity"

from calculator.errors import (
    CalculatorError,
    DivisionByZeroError,
    InvalidNumberError,
    InvalidOperatorError,
    MissingOperandError,
    NegativeSqrtError,
    OverflowError,
)
from calculator.formatter import Result, format_result

__all__ = [
    "__version__",
    "CalculatorError",
    "InvalidNumberError",
    "InvalidOperatorError",
    "MissingOperandError",
    "DivisionByZeroError",
    "NegativeSqrtError",
    "OverflowError",
    "Result",
    "format_result",
]
