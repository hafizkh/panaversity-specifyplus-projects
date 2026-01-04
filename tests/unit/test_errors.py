"""Unit tests for calculator error types."""

from calculator.errors import (
    CalculatorError,
    DivisionByZeroError,
    InvalidNumberError,
    InvalidOperatorError,
    MissingOperandError,
    NegativeSqrtError,
    OverflowError,
)


class TestCalculatorError:
    """Tests for the base CalculatorError class."""

    def test_message_attribute(self) -> None:
        """Test that message is stored correctly."""
        error = CalculatorError("test message")
        assert error.message == "test message"

    def test_str_representation(self) -> None:
        """Test string representation returns message."""
        error = CalculatorError("test message")
        assert str(error) == "test message"

    def test_default_exit_code(self) -> None:
        """Test default exit code is 1."""
        error = CalculatorError("test")
        assert error.exit_code == 1


class TestInvalidNumberError:
    """Tests for InvalidNumberError."""

    def test_message_format(self) -> None:
        """Test error message includes the invalid value."""
        error = InvalidNumberError("abc")
        assert str(error) == "Invalid number: abc"

    def test_value_attribute(self) -> None:
        """Test value attribute stores the invalid input."""
        error = InvalidNumberError("xyz")
        assert error.value == "xyz"

    def test_exit_code(self) -> None:
        """Test exit code is 1 for input errors."""
        error = InvalidNumberError("abc")
        assert error.exit_code == 1

    def test_inheritance(self) -> None:
        """Test it inherits from CalculatorError."""
        error = InvalidNumberError("abc")
        assert isinstance(error, CalculatorError)


class TestInvalidOperatorError:
    """Tests for InvalidOperatorError."""

    def test_message_format(self) -> None:
        """Test error message includes the invalid operator."""
        error = InvalidOperatorError("@")
        assert str(error) == "Invalid operator: @"

    def test_operator_attribute(self) -> None:
        """Test operator attribute stores the invalid symbol."""
        error = InvalidOperatorError("&")
        assert error.operator == "&"

    def test_exit_code(self) -> None:
        """Test exit code is 1 for input errors."""
        error = InvalidOperatorError("@")
        assert error.exit_code == 1


class TestMissingOperandError:
    """Tests for MissingOperandError."""

    def test_message_format(self) -> None:
        """Test error message includes expected and got counts."""
        error = MissingOperandError(3, 2)
        assert str(error) == "Missing operand: expected 3 arguments, got 2"

    def test_expected_attribute(self) -> None:
        """Test expected attribute stores the expected count."""
        error = MissingOperandError(3, 1)
        assert error.expected == 3

    def test_got_attribute(self) -> None:
        """Test got attribute stores the actual count."""
        error = MissingOperandError(3, 1)
        assert error.got == 1

    def test_exit_code(self) -> None:
        """Test exit code is 1 for input errors."""
        error = MissingOperandError(3, 2)
        assert error.exit_code == 1


class TestDivisionByZeroError:
    """Tests for DivisionByZeroError."""

    def test_message(self) -> None:
        """Test error message is correct."""
        error = DivisionByZeroError()
        assert str(error) == "Division by zero is not allowed"

    def test_exit_code(self) -> None:
        """Test exit code is 2 for calculation errors."""
        error = DivisionByZeroError()
        assert error.exit_code == 2


class TestOverflowError:
    """Tests for OverflowError."""

    def test_message(self) -> None:
        """Test error message is correct."""
        error = OverflowError()
        assert str(error) == "Result exceeds maximum representable value"

    def test_exit_code(self) -> None:
        """Test exit code is 2 for calculation errors."""
        error = OverflowError()
        assert error.exit_code == 2


class TestNegativeSqrtError:
    """Tests for NegativeSqrtError."""

    def test_message_format(self) -> None:
        """Test error message includes the negative value."""
        error = NegativeSqrtError(-4)
        assert str(error) == "Cannot compute square root of negative number: -4"

    def test_value_attribute(self) -> None:
        """Test value attribute stores the negative number."""
        error = NegativeSqrtError(-9.5)
        assert error.value == -9.5

    def test_exit_code(self) -> None:
        """Test exit code is 2 for calculation errors."""
        error = NegativeSqrtError(-1)
        assert error.exit_code == 2
