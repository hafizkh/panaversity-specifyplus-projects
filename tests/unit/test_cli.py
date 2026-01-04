"""Unit tests for CLI module (direct function calls)."""

import pytest

from calculator.cli import (
    create_parser,
    execute_calculation,
    main,
    parse_number,
)
from calculator.errors import (
    InvalidNumberError,
    InvalidOperatorError,
    MissingOperandError,
)


class TestParseNumber:
    """Tests for the parse_number function."""

    def test_integer(self) -> None:
        """Test parsing integer string."""
        assert parse_number("42") == 42.0

    def test_float(self) -> None:
        """Test parsing float string."""
        assert parse_number("3.14") == pytest.approx(3.14)

    def test_negative(self) -> None:
        """Test parsing negative number."""
        assert parse_number("-5") == -5.0

    def test_scientific_notation(self) -> None:
        """Test parsing scientific notation."""
        assert parse_number("1e10") == 1e10

    def test_invalid_raises_error(self) -> None:
        """Test invalid input raises InvalidNumberError."""
        with pytest.raises(InvalidNumberError) as exc_info:
            parse_number("abc")
        assert exc_info.value.value == "abc"


class TestExecuteCalculation:
    """Tests for the execute_calculation function."""

    def test_addition(self) -> None:
        """Test addition calculation."""
        result = execute_calculation(["5", "+", "3"])
        assert result == "8"

    def test_subtraction(self) -> None:
        """Test subtraction calculation."""
        result = execute_calculation(["10", "-", "4"])
        assert result == "6"

    def test_multiplication(self) -> None:
        """Test multiplication calculation."""
        result = execute_calculation(["6", "*", "7"])
        assert result == "42"

    def test_division(self) -> None:
        """Test division calculation."""
        result = execute_calculation(["20", "/", "4"])
        assert result == "5"

    def test_power(self) -> None:
        """Test power calculation."""
        result = execute_calculation(["2", "^", "8"])
        assert result == "256"

    def test_modulo(self) -> None:
        """Test modulo calculation."""
        result = execute_calculation(["17", "%", "5"])
        assert result == "2"

    def test_sqrt(self) -> None:
        """Test sqrt calculation."""
        result = execute_calculation(["sqrt", "16"])
        assert result == "4"

    def test_empty_args_raises_error(self) -> None:
        """Test empty args raises MissingOperandError."""
        with pytest.raises(MissingOperandError):
            execute_calculation([])

    def test_single_arg_raises_error(self) -> None:
        """Test single arg raises MissingOperandError."""
        with pytest.raises(MissingOperandError):
            execute_calculation(["5"])

    def test_two_args_binary_raises_error(self) -> None:
        """Test two args with binary operator raises MissingOperandError."""
        with pytest.raises(MissingOperandError):
            execute_calculation(["5", "+"])

    def test_invalid_operator_raises_error(self) -> None:
        """Test invalid operator raises InvalidOperatorError."""
        with pytest.raises(InvalidOperatorError):
            execute_calculation(["5", "@", "3"])

    def test_invalid_number_raises_error(self) -> None:
        """Test invalid number raises InvalidNumberError."""
        with pytest.raises(InvalidNumberError):
            execute_calculation(["abc", "+", "3"])


class TestMain:
    """Tests for the main function."""

    def test_help_flag(self, capsys) -> None:
        """Test --help flag returns 0 and prints help."""
        result = main(["--help"])
        assert result == 0
        captured = capsys.readouterr()
        assert "Calculator" in captured.out

    def test_version_flag(self, capsys) -> None:
        """Test --version flag returns 0 and prints version."""
        result = main(["--version"])
        assert result == 0
        captured = capsys.readouterr()
        assert "1.0.0" in captured.out

    def test_no_args_shows_usage(self, capsys) -> None:
        """Test no args returns 0 and shows usage."""
        result = main([])
        assert result == 0
        captured = capsys.readouterr()
        assert "Usage" in captured.out

    def test_valid_calculation(self, capsys) -> None:
        """Test valid calculation returns 0 and prints result."""
        result = main(["5", "+", "3"])
        assert result == 0
        captured = capsys.readouterr()
        assert captured.out.strip() == "8"

    def test_invalid_input_returns_error_code(self, capsys) -> None:
        """Test invalid input returns error code 1."""
        result = main(["abc", "+", "3"])
        assert result == 1
        captured = capsys.readouterr()
        assert "Invalid number" in captured.err

    def test_division_by_zero_returns_error_code(self, capsys) -> None:
        """Test division by zero returns error code 2."""
        result = main(["10", "/", "0"])
        assert result == 2
        captured = capsys.readouterr()
        assert "Division by zero" in captured.err


class TestCreateParser:
    """Tests for the create_parser function."""

    def test_parser_created(self) -> None:
        """Test parser is created successfully."""
        parser = create_parser()
        assert parser is not None
        assert parser.prog == "calc"

    def test_parser_help_flag(self) -> None:
        """Test parser recognizes --help flag."""
        parser = create_parser()
        args = parser.parse_args(["--help"])
        assert args.show_help is True

    def test_parser_version_flag(self) -> None:
        """Test parser recognizes --version flag."""
        parser = create_parser()
        args = parser.parse_args(["--version"])
        assert args.show_version is True

    def test_parser_args(self) -> None:
        """Test parser captures calculation args."""
        parser = create_parser()
        args = parser.parse_args(["5", "+", "3"])
        assert args.args == ["5", "+", "3"]
