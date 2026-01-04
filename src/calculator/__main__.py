"""Entry point for running calculator as a module: python -m calculator."""

import sys

from calculator.cli import main

if __name__ == "__main__":
    sys.exit(main())
