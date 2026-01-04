"""Operations package - Mathematical operation registry.

This module provides the Operator enum and operation registry for
dispatching calculations to the appropriate functions.
"""

from collections.abc import Callable
from enum import Enum


class Operator(Enum):
    """Supported mathematical operators.

    Each operator has a symbol used in the CLI and maps to an operation function.
    """

    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    POWER = "^"
    MODULO = "%"
    SQRT = "sqrt"


# Type alias for operation functions
BinaryOperation = Callable[[float, float], float]
UnaryOperation = Callable[[float], float]

# Operation registries - will be populated by basic.py and advanced.py
BINARY_OPERATIONS: dict[str, BinaryOperation] = {}
UNARY_OPERATIONS: dict[str, UnaryOperation] = {}


def register_binary(symbol: str) -> Callable[[BinaryOperation], BinaryOperation]:
    """Decorator to register a binary operation.

    Args:
        symbol: The operator symbol (e.g., '+', '-', '*', '/').

    Returns:
        A decorator that registers the function and returns it unchanged.

    Example:
        >>> @register_binary('+')
        ... def add(a: float, b: float) -> float:
        ...     return a + b
    """

    def decorator(func: BinaryOperation) -> BinaryOperation:
        BINARY_OPERATIONS[symbol] = func
        return func

    return decorator


def register_unary(symbol: str) -> Callable[[UnaryOperation], UnaryOperation]:
    """Decorator to register a unary operation.

    Args:
        symbol: The operator symbol (e.g., 'sqrt').

    Returns:
        A decorator that registers the function and returns it unchanged.

    Example:
        >>> @register_unary('sqrt')
        ... def sqrt(x: float) -> float:
        ...     return x ** 0.5
    """

    def decorator(func: UnaryOperation) -> UnaryOperation:
        UNARY_OPERATIONS[symbol] = func
        return func

    return decorator


def get_binary_operation(symbol: str) -> BinaryOperation | None:
    """Get the binary operation function for a symbol.

    Args:
        symbol: The operator symbol.

    Returns:
        The operation function, or None if not found.
    """
    return BINARY_OPERATIONS.get(symbol)


def get_unary_operation(symbol: str) -> UnaryOperation | None:
    """Get the unary operation function for a symbol.

    Args:
        symbol: The operator symbol.

    Returns:
        The operation function, or None if not found.
    """
    return UNARY_OPERATIONS.get(symbol)


def is_binary_operator(symbol: str) -> bool:
    """Check if a symbol is a registered binary operator.

    Args:
        symbol: The operator symbol to check.

    Returns:
        True if the symbol is a registered binary operator.
    """
    return symbol in BINARY_OPERATIONS


def is_unary_operator(symbol: str) -> bool:
    """Check if a symbol is a registered unary operator.

    Args:
        symbol: The operator symbol to check.

    Returns:
        True if the symbol is a registered unary operator.
    """
    return symbol in UNARY_OPERATIONS


def get_all_operators() -> list[str]:
    """Get all registered operator symbols.

    Returns:
        A list of all operator symbols (binary and unary).
    """
    return list(BINARY_OPERATIONS.keys()) + list(UNARY_OPERATIONS.keys())
