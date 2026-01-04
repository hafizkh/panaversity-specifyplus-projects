"""Advanced mathematical operations: power, modulo, sqrt.

This module provides advanced mathematical operations with proper
type hints and error handling.
"""

import math

from calculator.errors import DivisionByZeroError, NegativeSqrtError, OverflowError
from calculator.operations import register_binary, register_unary


@register_binary("^")
def power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent.

    Args:
        base: The base number.
        exponent: The exponent.

    Returns:
        The result of base raised to exponent.

    Raises:
        OverflowError: If the result exceeds representable limits.

    Examples:
        >>> power(2, 8)
        256
        >>> power(10, -2)
        0.01
    """
    result: float = base**exponent
    if math.isinf(result):
        raise OverflowError()
    return result


@register_binary("%")
def modulo(dividend: float, divisor: float) -> float:
    """Compute the remainder of dividend divided by divisor.

    Args:
        dividend: The number to divide.
        divisor: The number to divide by.

    Returns:
        The remainder of the division.

    Raises:
        DivisionByZeroError: If divisor is zero.

    Examples:
        >>> modulo(17, 5)
        2
        >>> modulo(10, 3)
        1
    """
    if divisor == 0:
        raise DivisionByZeroError()
    return dividend % divisor


@register_unary("sqrt")
def sqrt(value: float) -> float:
    """Compute the square root of a number.

    Args:
        value: The number to compute the square root of.

    Returns:
        The square root of the value.

    Raises:
        NegativeSqrtError: If value is negative.
        OverflowError: If the result exceeds representable limits.

    Examples:
        >>> sqrt(16)
        4.0
        >>> sqrt(2)
        1.4142135623730951
    """
    if value < 0:
        raise NegativeSqrtError(value)
    result = math.sqrt(value)
    if math.isinf(result):
        raise OverflowError()
    return result
