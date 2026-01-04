"""Unit tests for basic arithmetic operations."""

import pytest

from calculator.errors import DivisionByZeroError
from calculator.operations.basic import add, divide, multiply, subtract


class TestAdd:
    """Tests for the add function."""

    def test_positive_integers(self) -> None:
        """Test addition of positive integers."""
        assert add(5, 3) == 8

    def test_negative_integers(self) -> None:
        """Test addition with negative integers."""
        assert add(-5, 3) == -2

    def test_floats(self) -> None:
        """Test addition of floating-point numbers."""
        assert add(3.14, 2.86) == pytest.approx(6.0)

    def test_zero(self) -> None:
        """Test addition with zero."""
        assert add(5, 0) == 5
        assert add(0, 5) == 5

    def test_large_numbers(self) -> None:
        """Test addition of large numbers."""
        assert add(1e10, 1e10) == 2e10


class TestSubtract:
    """Tests for the subtract function."""

    def test_positive_integers(self) -> None:
        """Test subtraction of positive integers."""
        assert subtract(10, 4) == 6

    def test_negative_result(self) -> None:
        """Test subtraction resulting in negative number."""
        assert subtract(3, 5) == -2

    def test_floats(self) -> None:
        """Test subtraction of floating-point numbers."""
        assert subtract(5.5, 2.5) == pytest.approx(3.0)

    def test_zero(self) -> None:
        """Test subtraction with zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5


class TestMultiply:
    """Tests for the multiply function."""

    def test_positive_integers(self) -> None:
        """Test multiplication of positive integers."""
        assert multiply(6, 7) == 42

    def test_negative_integers(self) -> None:
        """Test multiplication with negative integers."""
        assert multiply(-3, 4) == -12
        assert multiply(-3, -4) == 12

    def test_floats(self) -> None:
        """Test multiplication of floating-point numbers."""
        assert multiply(2.5, 4) == pytest.approx(10.0)

    def test_zero(self) -> None:
        """Test multiplication with zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0

    def test_one(self) -> None:
        """Test multiplication with one (identity)."""
        assert multiply(42, 1) == 42


class TestDivide:
    """Tests for the divide function."""

    def test_positive_integers(self) -> None:
        """Test division of positive integers."""
        assert divide(20, 4) == 5

    def test_float_result(self) -> None:
        """Test division resulting in float."""
        assert divide(10, 4) == pytest.approx(2.5)

    def test_negative_division(self) -> None:
        """Test division with negative numbers."""
        assert divide(-10, 2) == -5
        assert divide(10, -2) == -5
        assert divide(-10, -2) == 5

    def test_zero_numerator(self) -> None:
        """Test division of zero."""
        assert divide(0, 5) == 0

    def test_division_by_zero_raises_error(self) -> None:
        """Test that division by zero raises DivisionByZeroError."""
        with pytest.raises(DivisionByZeroError):
            divide(10, 0)

    def test_floats(self) -> None:
        """Test division of floating-point numbers."""
        assert divide(7.5, 2.5) == pytest.approx(3.0)
