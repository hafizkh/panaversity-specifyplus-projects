"""API route handlers for the calculator."""

from fastapi import APIRouter, HTTPException

# Import operations to register them
import calculator.operations.advanced  # noqa: F401
import calculator.operations.basic  # noqa: F401
from calculator import __version__
from calculator.errors import CalculatorError
from calculator.formatter import format_result
from calculator.operations import (
    get_binary_operation,
    get_unary_operation,
    is_binary_operator,
    is_unary_operator,
)

from .schemas import (
    CalculateRequest,
    CalculateResponse,
    ErrorResponse,
    HealthResponse,
    OperatorInfo,
    OperatorsResponse,
)

router = APIRouter(prefix="/api", tags=["calculator"])


def _make_error(message: str, code: str) -> dict[str, object]:
    """Create an error detail dictionary."""
    return {"success": False, "error": message, "code": code}


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(status="ok", version=__version__)


@router.get("/operators", response_model=OperatorsResponse)
async def get_operators() -> OperatorsResponse:
    """Get list of available operators."""
    operators = [
        OperatorInfo(symbol="+", type="binary", description="Addition"),
        OperatorInfo(symbol="-", type="binary", description="Subtraction"),
        OperatorInfo(symbol="*", type="binary", description="Multiplication"),
        OperatorInfo(symbol="/", type="binary", description="Division"),
        OperatorInfo(symbol="^", type="binary", description="Power"),
        OperatorInfo(symbol="%", type="binary", description="Modulo"),
        OperatorInfo(symbol="sqrt", type="unary", description="Square root"),
    ]
    return OperatorsResponse(operators=operators)


@router.post(
    "/calculate",
    response_model=CalculateResponse,
    responses={400: {"model": ErrorResponse}, 422: {"model": ErrorResponse}},
)
async def calculate(request: CalculateRequest) -> CalculateResponse | ErrorResponse:
    """Perform a calculation."""
    try:
        operator = request.operator
        operand1 = request.operand1
        operand2 = request.operand2

        # Handle unary operations
        if is_unary_operator(operator):
            unary_op = get_unary_operation(operator)
            if unary_op is None:
                msg = f"Unknown operator: {operator}"
                raise HTTPException(
                    status_code=400,
                    detail=_make_error(msg, "INVALID_OPERATOR"),
                )
            result_value = unary_op(operand1)

        # Handle binary operations
        elif is_binary_operator(operator):
            if operand2 is None:
                raise HTTPException(
                    status_code=400,
                    detail=_make_error(
                        "Second operand required for binary operation",
                        "MISSING_OPERAND",
                    ),
                )
            binary_op = get_binary_operation(operator)
            if binary_op is None:
                msg = f"Unknown operator: {operator}"
                raise HTTPException(
                    status_code=400,
                    detail=_make_error(msg, "INVALID_OPERATOR"),
                )
            result_value = binary_op(operand1, operand2)

        else:
            raise HTTPException(
                status_code=400,
                detail=_make_error(f"Invalid operator: {operator}", "INVALID_OPERATOR"),
            )

        # Format the result
        result = format_result(result_value)
        return CalculateResponse(
            success=True,
            result=result.value,
            display=result.display_value,
        )

    except CalculatorError as e:
        error_code = type(e).__name__.replace("Error", "").upper()
        raise HTTPException(
            status_code=400,
            detail=_make_error(str(e), error_code),
        ) from None
