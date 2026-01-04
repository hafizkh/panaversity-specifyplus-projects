"""Integration tests for the calculator CLI."""


class TestBasicArithmeticCLI:
    """Tests for basic arithmetic operations via CLI."""

    def test_addition(self, run_calc) -> None:
        """Test addition via CLI."""
        result = run_calc("5", "+", "3")
        assert result.stdout == "8"
        assert result.returncode == 0

    def test_subtraction(self, run_calc) -> None:
        """Test subtraction via CLI."""
        result = run_calc("10", "-", "4")
        assert result.stdout == "6"
        assert result.returncode == 0

    def test_multiplication(self, run_calc) -> None:
        """Test multiplication via CLI."""
        result = run_calc("6", "*", "7")
        assert result.stdout == "42"
        assert result.returncode == 0

    def test_division(self, run_calc) -> None:
        """Test division via CLI."""
        result = run_calc("20", "/", "4")
        assert result.stdout == "5"
        assert result.returncode == 0

    def test_division_float_result(self, run_calc) -> None:
        """Test division with float result."""
        result = run_calc("10", "/", "4")
        assert result.stdout == "2.5"
        assert result.returncode == 0

    def test_negative_first_operand(self, run_calc) -> None:
        """Test with negative first operand using -- separator."""
        result = run_calc("--", "-5", "+", "3")
        assert result.stdout == "-2"
        assert result.returncode == 0

    def test_float_operands(self, run_calc) -> None:
        """Test with floating-point operands."""
        result = run_calc("3.14", "*", "2")
        assert result.stdout == "6.28"
        assert result.returncode == 0


class TestErrorHandlingCLI:
    """Tests for error handling via CLI."""

    def test_invalid_number(self, run_calc) -> None:
        """Test error for invalid number input."""
        result = run_calc("abc", "+", "3")
        assert "Invalid number: abc" in result.stderr
        assert result.returncode == 1

    def test_invalid_operator(self, run_calc) -> None:
        """Test error for invalid operator."""
        result = run_calc("5", "@", "3")
        assert "Invalid operator: @" in result.stderr
        assert result.returncode == 1

    def test_missing_operand(self, run_calc) -> None:
        """Test error for missing operand."""
        result = run_calc("5", "+")
        assert "Missing operand" in result.stderr
        assert result.returncode == 1

    def test_division_by_zero(self, run_calc) -> None:
        """Test error for division by zero."""
        result = run_calc("10", "/", "0")
        assert "Division by zero" in result.stderr
        assert result.returncode == 2


class TestAdvancedOperationsCLI:
    """Tests for advanced operations via CLI."""

    def test_power(self, run_calc) -> None:
        """Test power operation via CLI."""
        result = run_calc("2", "^", "8")
        assert result.stdout == "256"
        assert result.returncode == 0

    def test_modulo(self, run_calc) -> None:
        """Test modulo operation via CLI."""
        result = run_calc("17", "%", "5")
        assert result.stdout == "2"
        assert result.returncode == 0

    def test_sqrt(self, run_calc) -> None:
        """Test square root operation via CLI."""
        result = run_calc("sqrt", "16")
        assert result.stdout == "4"
        assert result.returncode == 0

    def test_sqrt_float_result(self, run_calc) -> None:
        """Test square root with float result."""
        result = run_calc("sqrt", "2")
        assert result.stdout.startswith("1.41421")
        assert result.returncode == 0


class TestHelpAndUsageCLI:
    """Tests for help and usage functionality."""

    def test_help_flag(self, run_calc) -> None:
        """Test --help flag displays help text."""
        result = run_calc("--help")
        assert "Calculator" in result.stdout
        assert "+" in result.stdout
        assert "-" in result.stdout
        assert "*" in result.stdout
        assert "/" in result.stdout
        assert result.returncode == 0

    def test_no_arguments_shows_usage(self, run_calc) -> None:
        """Test no arguments shows usage information."""
        result = run_calc()
        assert "Usage" in result.stdout or "usage" in result.stdout.lower()
        assert result.returncode == 0

    def test_version_flag(self, run_calc) -> None:
        """Test --version flag displays version."""
        result = run_calc("--version")
        assert "1.0.0" in result.stdout
        assert result.returncode == 0
