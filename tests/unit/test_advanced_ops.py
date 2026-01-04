"""Unit tests for advanced mathematical operations."""

import math

import pytest

from calculator.errors import DivisionByZeroError, NegativeSqrtError
from calculator.operations.advanced import modulo, power, sqrt


class TestPower:
    """Tests for the power function."""

    def test_positive_exponent(self) -> None:
        """Test power with positive exponent."""
        assert power(2, 8) == 256

    def test_zero_exponent(self) -> None:
        """Test any number to power of zero equals 1."""
        assert power(5, 0) == 1
        assert power(100, 0) == 1

    def test_one_exponent(self) -> None:
        """Test power of 1 returns the base."""
        assert power(42, 1) == 42

    def test_negative_exponent(self) -> None:
        """Test power with negative exponent."""
        assert power(2, -1) == pytest.approx(0.5)
        assert power(10, -2) == pytest.approx(0.01)

    def test_fractional_exponent(self) -> None:
        """Test power with fractional exponent (square root)."""
        assert power(16, 0.5) == pytest.approx(4.0)

    def test_zero_base(self) -> None:
        """Test zero to positive power equals zero."""
        assert power(0, 5) == 0

    def test_large_result(self) -> None:
        """Test power with large result."""
        assert power(10, 10) == 1e10


class TestModulo:
    """Tests for the modulo function."""

    def test_positive_numbers(self) -> None:
        """Test modulo with positive numbers."""
        assert modulo(17, 5) == 2

    def test_exact_division(self) -> None:
        """Test modulo when division is exact."""
        assert modulo(10, 5) == 0

    def test_negative_dividend(self) -> None:
        """Test modulo with negative dividend."""
        # Python's modulo follows the sign of the divisor
        result = modulo(-17, 5)
        assert result == 3  # Python behavior: -17 % 5 = 3

    def test_negative_divisor(self) -> None:
        """Test modulo with negative divisor."""
        result = modulo(17, -5)
        assert result == -3  # Python behavior: 17 % -5 = -3

    def test_floats(self) -> None:
        """Test modulo with floating-point numbers."""
        assert modulo(7.5, 2.5) == pytest.approx(0.0)

    def test_division_by_zero_raises_error(self) -> None:
        """Test that modulo by zero raises DivisionByZeroError."""
        with pytest.raises(DivisionByZeroError):
            modulo(10, 0)


class TestSqrt:
    """Tests for the sqrt function."""

    def test_perfect_square(self) -> None:
        """Test square root of perfect square."""
        assert sqrt(16) == 4
        assert sqrt(144) == 12

    def test_non_perfect_square(self) -> None:
        """Test square root of non-perfect square."""
        assert sqrt(2) == pytest.approx(math.sqrt(2))

    def test_zero(self) -> None:
        """Test square root of zero."""
        assert sqrt(0) == 0

    def test_one(self) -> None:
        """Test square root of one."""
        assert sqrt(1) == 1

    def test_large_number(self) -> None:
        """Test square root of large number."""
        assert sqrt(1e10) == pytest.approx(1e5)

    def test_small_number(self) -> None:
        """Test square root of small positive number."""
        assert sqrt(0.25) == pytest.approx(0.5)

    def test_negative_raises_error(self) -> None:
        """Test that sqrt of negative number raises NegativeSqrtError."""
        with pytest.raises(NegativeSqrtError):
            sqrt(-4)

    def test_negative_error_message(self) -> None:
        """Test NegativeSqrtError message contains the value."""
        with pytest.raises(NegativeSqrtError) as exc_info:
            sqrt(-9)
        assert "-9" in str(exc_info.value)
