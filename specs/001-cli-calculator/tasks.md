# Tasks: CLI Calculator

**Input**: Design documents from `/specs/001-cli-calculator/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/

**Tests**: Required per Constitution Principle II (Test-Driven Development). Tests MUST be written FIRST and FAIL before implementation.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/calculator/`, `tests/` at repository root
- Paths shown below follow the plan.md structure

---

## Phase 1: Setup

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directory structure per plan.md (src/calculator/, tests/unit/, tests/integration/)
- [x] T002 Initialize Python project with pyproject.toml (uv, ruff, mypy, pytest configuration)
- [x] T003 [P] Create src/calculator/__init__.py with package metadata and exports
- [x] T004 [P] Create src/calculator/__main__.py entry point stub
- [x] T005 [P] Create tests/conftest.py with pytest fixtures

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Create src/calculator/errors.py with CalculatorError base class and exception hierarchy (InvalidNumberError, InvalidOperatorError, MissingOperandError, DivisionByZeroError, OverflowError)
- [x] T007 [P] Create tests/unit/test_errors.py with tests for all error types (MUST FAIL initially)
- [x] T008 Create src/calculator/formatter.py with Result dataclass and format_result() function
- [x] T009 [P] Create tests/unit/test_formatter.py with formatting tests for integers, floats, precision, scientific notation (MUST FAIL initially)
- [x] T010 Create src/calculator/operations/__init__.py with Operator enum and operation registry

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Basic Arithmetic Operations (Priority: P1)

**Goal**: Users can perform addition, subtraction, multiplication, and division via CLI

**Independent Test**: Run `uv run calc 5 + 3` and verify output is `8`

### Tests for User Story 1 (TDD - Write First, Must Fail)

- [x] T011 [P] [US1] Create tests/unit/test_basic_ops.py with tests for add(), subtract(), multiply(), divide() functions
- [x] T012 [P] [US1] Create tests/integration/test_cli.py with basic arithmetic CLI tests (calc 5 + 3, calc 10 - 4, etc.)

### Implementation for User Story 1

- [x] T013 [P] [US1] Implement add() function in src/calculator/operations/basic.py with type hints and docstring
- [x] T014 [P] [US1] Implement subtract() function in src/calculator/operations/basic.py
- [x] T015 [P] [US1] Implement multiply() function in src/calculator/operations/basic.py
- [x] T016 [P] [US1] Implement divide() function in src/calculator/operations/basic.py with DivisionByZeroError
- [x] T017 [US1] Register basic operations in src/calculator/operations/__init__.py
- [x] T018 [US1] Create src/calculator/cli.py with argument parsing for binary operations
- [x] T019 [US1] Wire CLI to operations and implement main() in src/calculator/__main__.py
- [x] T020 [US1] Verify all US1 tests pass with `uv run pytest tests/unit/test_basic_ops.py tests/integration/test_cli.py -v`

**Checkpoint**: User Story 1 complete. Basic arithmetic works: `uv run calc 5 + 3` → `8`

---

## Phase 4: User Story 2 - Error Handling for Invalid Input (Priority: P2)

**Goal**: Users receive clear error messages for invalid numbers, operators, and missing operands

**Independent Test**: Run `uv run calc abc + 3` and verify stderr shows "Invalid number: abc" with exit code 1

### Tests for User Story 2 (TDD - Write First, Must Fail)

- [x] T021 [P] [US2] Add tests/unit/test_errors.py tests for error message formatting
- [x] T022 [P] [US2] Add tests/integration/test_cli.py tests for invalid input scenarios (abc + 3, 5 @ 3, 5 +, 10 / 0)

### Implementation for User Story 2

- [x] T023 [US2] Add input validation to src/calculator/cli.py for number parsing with InvalidNumberError
- [x] T024 [US2] Add operator validation to src/calculator/cli.py with InvalidOperatorError
- [x] T025 [US2] Add argument count validation to src/calculator/cli.py with MissingOperandError
- [x] T026 [US2] Add overflow detection to src/calculator/operations/basic.py with OverflowError
- [x] T027 [US2] Implement error output to stderr with proper exit codes in src/calculator/__main__.py
- [x] T028 [US2] Verify all US2 tests pass with `uv run pytest tests/ -k "error or invalid" -v`

**Checkpoint**: User Story 2 complete. Error handling works: `uv run calc abc + 3` → stderr "Error: Invalid number: abc"

---

## Phase 5: User Story 3 - Advanced Mathematical Operations (Priority: P3)

**Goal**: Users can perform power, modulo, and square root operations

**Independent Test**: Run `uv run calc 2 ^ 8` and verify output is `256`

### Tests for User Story 3 (TDD - Write First, Must Fail)

- [x] T029 [P] [US3] Create tests/unit/test_advanced_ops.py with tests for power(), modulo(), sqrt() functions
- [x] T030 [P] [US3] Add tests/integration/test_cli.py tests for advanced operations (2 ^ 8, 17 % 5, sqrt 16)

### Implementation for User Story 3

- [x] T031 [P] [US3] Implement power() function in src/calculator/operations/advanced.py with overflow detection
- [x] T032 [P] [US3] Implement modulo() function in src/calculator/operations/advanced.py with DivisionByZeroError
- [x] T033 [P] [US3] Implement sqrt() function in src/calculator/operations/advanced.py with negative number error
- [x] T034 [US3] Register advanced operations in src/calculator/operations/__init__.py
- [x] T035 [US3] Update src/calculator/cli.py to handle unary operations (sqrt)
- [x] T036 [US3] Verify all US3 tests pass with `uv run pytest tests/unit/test_advanced_ops.py tests/integration/test_cli.py -k "advanced or power or modulo or sqrt" -v`

**Checkpoint**: User Story 3 complete. Advanced operations work: `uv run calc sqrt 16` → `4`

---

## Phase 6: User Story 4 - Help and Usage Information (Priority: P4)

**Goal**: Users can view help information and usage examples

**Independent Test**: Run `uv run calc --help` and verify help text displays all operations

### Tests for User Story 4 (TDD - Write First, Must Fail)

- [x] T037 [P] [US4] Add tests/integration/test_cli.py tests for --help flag output
- [x] T038 [P] [US4] Add tests/integration/test_cli.py tests for no-arguments usage output

### Implementation for User Story 4

- [x] T039 [US4] Add --help and -h argument handling to src/calculator/cli.py
- [x] T040 [US4] Create help text with all operations and examples in src/calculator/cli.py
- [x] T041 [US4] Add usage message for no-arguments case in src/calculator/__main__.py
- [x] T042 [US4] Add --version flag support in src/calculator/cli.py
- [x] T043 [US4] Verify all US4 tests pass with `uv run pytest tests/integration/test_cli.py -k "help or usage or version" -v`

**Checkpoint**: User Story 4 complete. Help works: `uv run calc --help` displays full documentation

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final quality checks and documentation

- [x] T044 [P] Run full test suite with coverage: `uv run pytest --cov=src/calculator --cov-report=term-missing`
- [x] T045 [P] Verify coverage meets 80% threshold per constitution (88.24% achieved)
- [x] T046 [P] Run type checker: `uv run mypy src/`
- [x] T047 [P] Run linter: `uv run ruff check src/ tests/`
- [x] T048 [P] Run formatter: `uv run ruff format src/ tests/`
- [x] T049 Create README.md with installation and usage instructions (quickstart.md serves as comprehensive docs)
- [x] T050 Validate quickstart.md scenarios work as documented

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - US1 can proceed independently
  - US2 depends on US1 (needs working CLI to test error handling)
  - US3 can proceed in parallel with US2 (independent functionality)
  - US4 can proceed after US1 (needs basic CLI structure)
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

```
Phase 1: Setup
    ↓
Phase 2: Foundational (errors, formatter, operation registry)
    ↓
    ├── Phase 3: US1 - Basic Arithmetic (MUST complete first)
    │       ↓
    │   ┌───┴───┐
    │   ↓       ↓
    │ Phase 4  Phase 6
    │  (US2)    (US4)
    │
    └── Phase 5: US3 - Advanced Operations (parallel with US2)
            ↓
        Phase 7: Polish
```

### Within Each User Story

1. Tests MUST be written and FAIL before implementation
2. Implementation tasks in order: functions → registry → CLI → verification
3. Story complete when checkpoint verification passes

### Parallel Opportunities

**Setup Phase** (all [P] tasks):
```bash
# Can run in parallel:
T003: Create __init__.py
T004: Create __main__.py
T005: Create conftest.py
```

**Foundational Phase** (tests in parallel):
```bash
# Can run in parallel:
T007: test_errors.py
T009: test_formatter.py
```

**User Story 1** (tests and functions in parallel):
```bash
# Tests in parallel:
T011: test_basic_ops.py
T012: test_cli.py (basic)

# Functions in parallel:
T013: add()
T014: subtract()
T015: multiply()
T016: divide()
```

**User Story 3** (tests and functions in parallel):
```bash
# Tests in parallel:
T029: test_advanced_ops.py
T030: test_cli.py (advanced)

# Functions in parallel:
T031: power()
T032: modulo()
T033: sqrt()
```

**Polish Phase** (all checks in parallel):
```bash
# Can run in parallel:
T044: pytest --cov
T046: mypy
T047: ruff check
T048: ruff format
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test `uv run calc 5 + 3` → `8`
5. Deploy/demo if ready

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add US1 (Basic Arithmetic) → Test independently → First working calculator!
3. Add US2 (Error Handling) → Test independently → Robust error messages
4. Add US3 (Advanced Ops) → Test independently → Full calculator functionality
5. Add US4 (Help) → Test independently → User-friendly documentation
6. Polish → Production ready

### TDD Discipline (Per Constitution)

For each user story:
1. **RED**: Write tests first (T011-T012, T021-T022, etc.) - tests MUST fail
2. **GREEN**: Implement minimum code to pass tests
3. **REFACTOR**: Improve code quality while keeping tests green
4. **VERIFY**: Run checkpoint command to confirm story complete

---

## Summary

| Phase | Tasks | Parallel | Description |
|-------|-------|----------|-------------|
| Setup | 5 | 3 | Project initialization |
| Foundational | 5 | 2 | Errors, formatter, registry |
| US1 (P1) | 10 | 6 | Basic arithmetic |
| US2 (P2) | 8 | 2 | Error handling |
| US3 (P3) | 8 | 6 | Advanced operations |
| US4 (P4) | 7 | 2 | Help and usage |
| Polish | 7 | 5 | Quality checks |
| **Total** | **50** | **26** | |

**MVP Scope**: Phases 1-3 (20 tasks) delivers working basic calculator
**Full Feature**: All phases (50 tasks) delivers complete CLI calculator with help
