"""Custom exception types for the calculator.

This module defines a hierarchy of exceptions for handling various error
conditions that can occur during calculation operations.
"""


class CalculatorError(Exception):
    """Base exception for all calculator errors.

    Attributes:
        message: Human-readable error description.
        exit_code: Unix exit code to return (1 for input errors, 2 for calc errors).
    """

    exit_code: int = 1

    def __init__(self, message: str) -> None:
        """Initialize the calculator error.

        Args:
            message: Human-readable error description.
        """
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        """Return the error message.

        Returns:
            The error message string.
        """
        return self.message


class InvalidNumberError(CalculatorError):
    """Raised when an operand is not a valid number.

    Examples:
        >>> raise InvalidNumberError("abc")
        InvalidNumberError: Invalid number: abc
    """

    def __init__(self, value: str) -> None:
        """Initialize the invalid number error.

        Args:
            value: The invalid value that could not be parsed as a number.
        """
        super().__init__(f"Invalid number: {value}")
        self.value = value


class InvalidOperatorError(CalculatorError):
    """Raised when an operator is not recognized.

    Examples:
        >>> raise InvalidOperatorError("@")
        InvalidOperatorError: Invalid operator: @
    """

    def __init__(self, operator: str) -> None:
        """Initialize the invalid operator error.

        Args:
            operator: The unrecognized operator symbol.
        """
        super().__init__(f"Invalid operator: {operator}")
        self.operator = operator


class MissingOperandError(CalculatorError):
    """Raised when required operands are missing.

    Examples:
        >>> raise MissingOperandError(3, 2)
        MissingOperandError: Missing operand: expected 3 arguments, got 2
    """

    def __init__(self, expected: int, got: int) -> None:
        """Initialize the missing operand error.

        Args:
            expected: Number of arguments expected.
            got: Number of arguments actually received.
        """
        super().__init__(f"Missing operand: expected {expected} arguments, got {got}")
        self.expected = expected
        self.got = got


class DivisionByZeroError(CalculatorError):
    """Raised when division or modulo by zero is attempted.

    This error has exit_code 2 as it's a calculation error, not an input error.

    Examples:
        >>> raise DivisionByZeroError()
        DivisionByZeroError: Division by zero is not allowed
    """

    exit_code: int = 2

    def __init__(self) -> None:
        """Initialize the division by zero error."""
        super().__init__("Division by zero is not allowed")


class OverflowError(CalculatorError):
    """Raised when the result exceeds representable limits.

    This error has exit_code 2 as it's a calculation error, not an input error.

    Examples:
        >>> raise OverflowError()
        OverflowError: Result exceeds maximum representable value
    """

    exit_code: int = 2

    def __init__(self) -> None:
        """Initialize the overflow error."""
        super().__init__("Result exceeds maximum representable value")


class NegativeSqrtError(CalculatorError):
    """Raised when square root of a negative number is attempted.

    This error has exit_code 2 as it's a calculation error, not an input error.

    Examples:
        >>> raise NegativeSqrtError(-4)
        NegativeSqrtError: Cannot compute square root of negative number: -4
    """

    exit_code: int = 2

    def __init__(self, value: float) -> None:
        """Initialize the negative sqrt error.

        Args:
            value: The negative value for which sqrt was attempted.
        """
        super().__init__(f"Cannot compute square root of negative number: {value}")
        self.value = value
