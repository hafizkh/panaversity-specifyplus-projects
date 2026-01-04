"""Result formatting for calculator output.

This module provides the Result dataclass and format_result function
for properly formatting calculation results.
"""

from dataclasses import dataclass


@dataclass
class Result:
    """Calculation result with formatted output.

    Attributes:
        value: The raw numeric result of the calculation.
        display_value: The formatted string representation for output.
    """

    value: float
    display_value: str


def format_result(value: float) -> Result:
    """Format a numeric result for display.

    Formatting rules:
    - Whole numbers display without decimal point (e.g., 8 not 8.0)
    - Floats show up to 10 significant decimal digits
    - Trailing zeros are removed
    - Very large (>1e15) or very small (<1e-10) numbers use scientific notation

    Args:
        value: The numeric value to format.

    Returns:
        A Result containing both the raw value and formatted display string.

    Examples:
        >>> format_result(8.0)
        Result(value=8.0, display_value='8')
        >>> format_result(3.14159)
        Result(value=3.14159, display_value='3.14159')
        >>> format_result(2.50)
        Result(value=2.5, display_value='2.5')
    """
    # Handle special cases for very large or very small numbers
    abs_value = abs(value)
    if abs_value != 0 and (abs_value >= 1e15 or abs_value < 1e-10):
        # Use scientific notation
        display_value = f"{value:.10e}"
        # Clean up scientific notation (remove trailing zeros in mantissa)
        if "e" in display_value:
            mantissa, exponent = display_value.split("e")
            mantissa = mantissa.rstrip("0").rstrip(".")
            display_value = f"{mantissa}e{exponent}"
    else:
        # Check if it's a whole number
        if value == int(value):
            display_value = str(int(value))
        else:
            # Format with up to 10 decimal places, removing trailing zeros
            display_value = f"{value:.10f}".rstrip("0").rstrip(".")

    return Result(value=value, display_value=display_value)
