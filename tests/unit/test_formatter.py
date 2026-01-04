"""Unit tests for result formatting."""

from calculator.formatter import Result, format_result


class TestResult:
    """Tests for the Result dataclass."""

    def test_value_attribute(self) -> None:
        """Test value is stored correctly."""
        result = Result(value=42.0, display_value="42")
        assert result.value == 42.0

    def test_display_value_attribute(self) -> None:
        """Test display_value is stored correctly."""
        result = Result(value=3.14, display_value="3.14")
        assert result.display_value == "3.14"


class TestFormatResult:
    """Tests for the format_result function."""

    def test_integer_result(self) -> None:
        """Test whole numbers display without decimal point."""
        result = format_result(8.0)
        assert result.display_value == "8"

    def test_integer_large(self) -> None:
        """Test large integers display correctly."""
        result = format_result(1000000.0)
        assert result.display_value == "1000000"

    def test_float_result(self) -> None:
        """Test floats display with decimals."""
        result = format_result(3.14)
        assert result.display_value == "3.14"

    def test_trailing_zeros_removed(self) -> None:
        """Test trailing zeros are removed from floats."""
        result = format_result(2.50)
        assert result.display_value == "2.5"

    def test_precision_limit(self) -> None:
        """Test results show up to 10 significant decimal digits."""
        result = format_result(1.123456789012345)
        # Should have at most 10 decimal places
        parts = result.display_value.split(".")
        if len(parts) == 2:
            assert len(parts[1]) <= 10

    def test_negative_integer(self) -> None:
        """Test negative whole numbers display correctly."""
        result = format_result(-5.0)
        assert result.display_value == "-5"

    def test_negative_float(self) -> None:
        """Test negative floats display correctly."""
        result = format_result(-3.14159)
        assert result.display_value == "-3.14159"

    def test_zero(self) -> None:
        """Test zero displays as 0."""
        result = format_result(0.0)
        assert result.display_value == "0"

    def test_very_small_number(self) -> None:
        """Test very small numbers use scientific notation."""
        result = format_result(1e-15)
        # Should use scientific notation for very small numbers
        assert "e" in result.display_value.lower() or result.display_value == "0"

    def test_very_large_number(self) -> None:
        """Test very large numbers use scientific notation."""
        result = format_result(1e20)
        # Should use scientific notation for very large numbers
        assert "e" in result.display_value.lower()

    def test_result_value_matches_input(self) -> None:
        """Test the Result.value matches the input value."""
        result = format_result(42.5)
        assert result.value == 42.5
