"""Basic arithmetic operations: add, subtract, multiply, divide.

This module provides the four fundamental arithmetic operations
with proper type hints and error handling.
"""

import math

from calculator.errors import DivisionByZeroError, OverflowError
from calculator.operations import register_binary


@register_binary("+")
def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a: The first operand.
        b: The second operand.

    Returns:
        The sum of a and b.

    Raises:
        OverflowError: If the result exceeds representable limits.

    Examples:
        >>> add(5, 3)
        8
        >>> add(-2.5, 7.5)
        5.0
    """
    result = a + b
    if math.isinf(result):
        raise OverflowError()
    return result


@register_binary("-")
def subtract(a: float, b: float) -> float:
    """Subtract b from a.

    Args:
        a: The first operand (minuend).
        b: The second operand (subtrahend).

    Returns:
        The difference of a minus b.

    Raises:
        OverflowError: If the result exceeds representable limits.

    Examples:
        >>> subtract(10, 4)
        6
        >>> subtract(3, 5)
        -2
    """
    result = a - b
    if math.isinf(result):
        raise OverflowError()
    return result


@register_binary("*")
def multiply(a: float, b: float) -> float:
    """Multiply two numbers.

    Args:
        a: The first operand.
        b: The second operand.

    Returns:
        The product of a and b.

    Raises:
        OverflowError: If the result exceeds representable limits.

    Examples:
        >>> multiply(6, 7)
        42
        >>> multiply(2.5, 4)
        10.0
    """
    result = a * b
    if math.isinf(result):
        raise OverflowError()
    return result


@register_binary("/")
def divide(a: float, b: float) -> float:
    """Divide a by b.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The quotient of a divided by b.

    Raises:
        DivisionByZeroError: If b is zero.
        OverflowError: If the result exceeds representable limits.

    Examples:
        >>> divide(20, 4)
        5.0
        >>> divide(10, 4)
        2.5
    """
    if b == 0:
        raise DivisionByZeroError()
    result = a / b
    if math.isinf(result):
        raise OverflowError()
    return result
