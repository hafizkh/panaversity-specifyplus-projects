<!--
=============================================================================
SYNC IMPACT REPORT
=============================================================================
Version change: 0.0.0 → 1.0.0 (MAJOR: Initial constitution ratification)

Modified principles: N/A (new constitution)

Added sections:
  - Core Principles (5 principles):
    - I. Type Safety First
    - II. Test-Driven Development
    - III. Modular Design
    - IV. CLI-First Interface
    - V. Simplicity Over Complexity
  - Code Quality Standards
  - Development Workflow
  - Governance

Removed sections: N/A (new constitution)

Templates validated:
  ✅ .specify/templates/plan-template.md - Constitution Check section compatible
  ✅ .specify/templates/spec-template.md - Requirements format compatible
  ✅ .specify/templates/tasks-template.md - Task phases compatible

Follow-up TODOs: None
=============================================================================
-->

# Calculator Panaversity Constitution

## Core Principles

### I. Type Safety First

All Python code MUST use type hints for function parameters, return values, and class attributes.
Type annotations MUST be validated using a static type checker (mypy or pyright).

- Every function MUST have fully typed signatures
- Complex types MUST use `typing` module constructs (Optional, Union, List, Dict, etc.)
- Third-party library types MUST be properly annotated or use stubs
- Type errors MUST be resolved before code is merged

**Rationale**: Type hints catch errors at development time, improve IDE support, and serve as
living documentation for the codebase.

### II. Test-Driven Development

Tests MUST be written before implementation code. The Red-Green-Refactor cycle is mandatory.

- Write failing tests first (Red)
- Implement minimum code to pass tests (Green)
- Improve code quality while keeping tests green (Refactor)
- pytest is the required testing framework
- Minimum 80% code coverage for core calculator logic

**Rationale**: TDD ensures requirements are understood before coding and prevents regression.

### III. Modular Design

Calculator functionality MUST be organized into discrete, single-responsibility modules.

- Each mathematical operation category MUST be a separate module
- Core calculation logic MUST be independent of I/O concerns
- Dependencies between modules MUST be explicit and minimal
- Circular dependencies are prohibited

**Rationale**: Modular design enables independent testing, easier maintenance, and future extensibility.

### IV. CLI-First Interface

The calculator MUST expose all functionality through a command-line interface.

- All operations MUST accept input via command-line arguments or stdin
- Output MUST go to stdout; errors MUST go to stderr
- Exit codes MUST follow Unix conventions (0 for success, non-zero for errors)
- Help text MUST be available via `--help` flag

**Rationale**: CLI interface enables scripting, testing, and integration with other tools.

### V. Simplicity Over Complexity

Solutions MUST be the simplest approach that meets requirements.

- YAGNI: Do not implement features until they are needed
- Prefer standard library solutions over third-party dependencies
- Avoid premature optimization
- Code MUST be readable without extensive comments

**Rationale**: Simple code is easier to understand, test, debug, and maintain.

## Code Quality Standards

- Python version: 3.11+ (for modern type hint features)
- Package manager: uv (required for all dependency management)
- Code formatting: ruff format (must pass before commit)
- Linting: ruff check (must pass before commit)
- Type checking: mypy or pyright (must pass before commit)
- All public functions MUST have docstrings
- Maximum line length: 88 characters (ruff default)
- Import sorting: isort-compatible ordering via ruff

## Development Workflow

1. **Branch Strategy**: Feature branches from main, squash merge on completion
2. **Commit Messages**: Conventional commits format (feat:, fix:, docs:, test:, refactor:)
3. **Pre-commit Checks**: Format, lint, type-check, and test MUST pass
4. **Code Review**: All changes require review before merge
5. **Documentation**: README and docstrings MUST be updated with new features

## Governance

This constitution supersedes all other development practices for this project.

**Amendment Procedure**:
1. Propose change with rationale in a constitution amendment PR
2. Document impact on existing code and workflows
3. Update affected templates and documentation
4. Obtain approval from project maintainer
5. Increment version according to semantic versioning

**Versioning Policy**:
- MAJOR: Backward-incompatible principle changes or removals
- MINOR: New principles or significant expansions
- PATCH: Clarifications, typo fixes, non-semantic refinements

**Compliance**:
- All PRs MUST verify compliance with these principles
- Violations MUST be documented and justified if unavoidable
- Periodic reviews SHOULD assess constitution adherence

**Version**: 1.0.0 | **Ratified**: 2026-01-04 | **Last Amended**: 2026-01-04
