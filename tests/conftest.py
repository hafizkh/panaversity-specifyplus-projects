"""Pytest configuration and fixtures for calculator tests."""

import subprocess
import sys
from typing import NamedTuple

import pytest


class CLIResult(NamedTuple):
    """Result of running the calculator CLI."""

    stdout: str
    stderr: str
    returncode: int


@pytest.fixture
def run_calc() -> callable:
    """Fixture to run the calculator CLI and capture output.

    Returns:
        A callable that takes CLI arguments and returns CLIResult.
    """

    def _run_calc(*args: str) -> CLIResult:
        """Run the calculator with given arguments.

        Args:
            *args: Command-line arguments to pass to the calculator.

        Returns:
            CLIResult with stdout, stderr, and return code.
        """
        result = subprocess.run(
            [sys.executable, "-m", "calculator", *args],
            capture_output=True,
            text=True,
            cwd=None,
        )
        return CLIResult(
            stdout=result.stdout.strip(),
            stderr=result.stderr.strip(),
            returncode=result.returncode,
        )

    return _run_calc
