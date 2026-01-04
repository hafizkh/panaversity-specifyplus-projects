"""Pydantic schemas for API request/response models."""

from pydantic import BaseModel, Field


class CalculateRequest(BaseModel):
    """Request model for calculation endpoint."""

    operand1: float = Field(..., description="First operand")
    operator: str = Field(..., description="Operator (+, -, *, /, ^, %, sqrt)")
    operand2: float | None = Field(
        None, description="Second operand (optional for unary)"
    )


class CalculateResponse(BaseModel):
    """Response model for successful calculation."""

    success: bool = True
    result: float = Field(..., description="Numeric result")
    display: str = Field(..., description="Formatted display value")


class ErrorResponse(BaseModel):
    """Response model for calculation errors."""

    success: bool = False
    error: str = Field(..., description="Error message")
    code: str = Field(..., description="Error code")


class OperatorInfo(BaseModel):
    """Information about an operator."""

    symbol: str
    type: str  # "binary" or "unary"
    description: str


class OperatorsResponse(BaseModel):
    """Response model for operators endpoint."""

    operators: list[OperatorInfo]


class HealthResponse(BaseModel):
    """Response model for health check."""

    status: str = "ok"
    version: str
