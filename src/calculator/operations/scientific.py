"""Scientific mathematical operations.

This module provides scientific/trigonometric operations with proper
type hints and error handling.
"""

import math

from calculator.errors import CalculatorError, NegativeSqrtError, OverflowError
from calculator.operations import register_unary


class InvalidInputError(CalculatorError):
    """Raised when input is invalid for the operation."""

    def __init__(self, message: str = "Invalid input") -> None:
        super().__init__(message)


class DomainError(CalculatorError):
    """Raised when input is outside the domain of the function."""

    def __init__(self, message: str = "Value outside function domain") -> None:
        super().__init__(message)


# Trigonometric functions (input in degrees)
@register_unary("sin")
def sin(value: float) -> float:
    """Compute the sine of an angle in degrees.

    Args:
        value: The angle in degrees.

    Returns:
        The sine of the angle.

    Examples:
        >>> sin(0)
        0.0
        >>> sin(90)
        1.0
    """
    radians = math.radians(value)
    result = math.sin(radians)
    # Handle floating point precision for common angles
    if abs(result) < 1e-15:
        return 0.0
    return result


@register_unary("cos")
def cos(value: float) -> float:
    """Compute the cosine of an angle in degrees.

    Args:
        value: The angle in degrees.

    Returns:
        The cosine of the angle.

    Examples:
        >>> cos(0)
        1.0
        >>> cos(90)
        0.0
    """
    radians = math.radians(value)
    result = math.cos(radians)
    if abs(result) < 1e-15:
        return 0.0
    return result


@register_unary("tan")
def tan(value: float) -> float:
    """Compute the tangent of an angle in degrees.

    Args:
        value: The angle in degrees.

    Returns:
        The tangent of the angle.

    Raises:
        DomainError: If the angle is at 90 + n*180 degrees.

    Examples:
        >>> tan(0)
        0.0
        >>> tan(45)
        1.0
    """
    # Check for undefined values (90, 270, -90, etc.)
    normalized = value % 180
    if abs(normalized - 90) < 1e-10:
        raise DomainError("Tangent is undefined at 90°")

    radians = math.radians(value)
    result = math.tan(radians)
    if abs(result) < 1e-15:
        return 0.0
    if math.isinf(result):
        raise OverflowError()
    return result


# Inverse trigonometric functions (output in degrees)
@register_unary("asin")
def asin(value: float) -> float:
    """Compute the arcsine (inverse sine) in degrees.

    Args:
        value: The value (must be between -1 and 1).

    Returns:
        The angle in degrees.

    Raises:
        DomainError: If value is outside [-1, 1].

    Examples:
        >>> asin(0)
        0.0
        >>> asin(1)
        90.0
    """
    if value < -1 or value > 1:
        raise DomainError("asin requires value between -1 and 1")
    result = math.degrees(math.asin(value))
    return result


@register_unary("acos")
def acos(value: float) -> float:
    """Compute the arccosine (inverse cosine) in degrees.

    Args:
        value: The value (must be between -1 and 1).

    Returns:
        The angle in degrees.

    Raises:
        DomainError: If value is outside [-1, 1].

    Examples:
        >>> acos(1)
        0.0
        >>> acos(0)
        90.0
    """
    if value < -1 or value > 1:
        raise DomainError("acos requires value between -1 and 1")
    result = math.degrees(math.acos(value))
    return result


@register_unary("atan")
def atan(value: float) -> float:
    """Compute the arctangent (inverse tangent) in degrees.

    Args:
        value: The value.

    Returns:
        The angle in degrees.

    Examples:
        >>> atan(0)
        0.0
        >>> atan(1)
        45.0
    """
    result = math.degrees(math.atan(value))
    return result


# Logarithmic functions
@register_unary("log")
def log10(value: float) -> float:
    """Compute the base-10 logarithm.

    Args:
        value: The number (must be positive).

    Returns:
        The base-10 logarithm.

    Raises:
        DomainError: If value is not positive.

    Examples:
        >>> log10(10)
        1.0
        >>> log10(100)
        2.0
    """
    if value <= 0:
        raise DomainError("Logarithm requires positive value")
    return math.log10(value)


@register_unary("ln")
def ln(value: float) -> float:
    """Compute the natural logarithm (base e).

    Args:
        value: The number (must be positive).

    Returns:
        The natural logarithm.

    Raises:
        DomainError: If value is not positive.

    Examples:
        >>> ln(1)
        0.0
        >>> ln(math.e)
        1.0
    """
    if value <= 0:
        raise DomainError("Logarithm requires positive value")
    return math.log(value)


# Exponential function
@register_unary("exp")
def exp(value: float) -> float:
    """Compute e raised to the power of value.

    Args:
        value: The exponent.

    Returns:
        e^value.

    Raises:
        OverflowError: If the result is too large.

    Examples:
        >>> exp(0)
        1.0
        >>> exp(1)
        2.718281828459045
    """
    try:
        result = math.exp(value)
        if math.isinf(result):
            raise OverflowError()
        return result
    except OverflowError:
        raise OverflowError() from None


# Factorial
@register_unary("fact")
def factorial(value: float) -> float:
    """Compute the factorial of a non-negative integer.

    Args:
        value: A non-negative integer.

    Returns:
        The factorial (n!).

    Raises:
        InvalidInputError: If value is negative or not an integer.
        OverflowError: If the result is too large.

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if value < 0:
        raise InvalidInputError("Factorial requires non-negative integer")
    if value != int(value):
        raise InvalidInputError("Factorial requires an integer")
    if value > 170:  # math.factorial would overflow
        raise OverflowError()
    return float(math.factorial(int(value)))


# Reciprocal (1/x)
@register_unary("inv")
def reciprocal(value: float) -> float:
    """Compute the reciprocal (1/x).

    Args:
        value: The number.

    Returns:
        1 divided by value.

    Raises:
        InvalidInputError: If value is zero.

    Examples:
        >>> reciprocal(2)
        0.5
        >>> reciprocal(4)
        0.25
    """
    if value == 0:
        raise InvalidInputError("Cannot divide by zero")
    return 1.0 / value


# Square (x²)
@register_unary("sqr")
def square(value: float) -> float:
    """Compute the square of a number.

    Args:
        value: The number.

    Returns:
        value squared.

    Raises:
        OverflowError: If the result is too large.

    Examples:
        >>> square(5)
        25
        >>> square(-3)
        9
    """
    result = value * value
    if math.isinf(result):
        raise OverflowError()
    return result


# Cube root
@register_unary("cbrt")
def cbrt(value: float) -> float:
    """Compute the cube root of a number.

    Args:
        value: The number.

    Returns:
        The cube root.

    Examples:
        >>> cbrt(8)
        2.0
        >>> cbrt(-27)
        -3.0
    """
    if value >= 0:
        return value ** (1 / 3)
    return -((-value) ** (1 / 3))


# Absolute value
@register_unary("abs")
def absolute(value: float) -> float:
    """Compute the absolute value.

    Args:
        value: The number.

    Returns:
        The absolute value.

    Examples:
        >>> absolute(-5)
        5
        >>> absolute(3)
        3
    """
    return abs(value)


# Sign change (+/-)
@register_unary("neg")
def negate(value: float) -> float:
    """Negate a number (change sign).

    Args:
        value: The number.

    Returns:
        The negated value.

    Examples:
        >>> negate(5)
        -5
        >>> negate(-3)
        3
    """
    return -value
