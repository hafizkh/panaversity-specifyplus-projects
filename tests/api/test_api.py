"""Tests for the calculator REST API."""

import pytest
from fastapi.testclient import TestClient

from api.main import app


@pytest.fixture
def client() -> TestClient:
    """Create a test client for the API."""
    return TestClient(app)


class TestHealthEndpoint:
    """Tests for the health check endpoint."""

    def test_health_check(self, client: TestClient) -> None:
        """Test health endpoint returns ok status."""
        response = client.get("/api/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert "version" in data


class TestOperatorsEndpoint:
    """Tests for the operators listing endpoint."""

    def test_get_operators(self, client: TestClient) -> None:
        """Test operators endpoint returns all operators."""
        response = client.get("/api/operators")
        assert response.status_code == 200
        data = response.json()
        assert "operators" in data

        operators = data["operators"]
        symbols = [op["symbol"] for op in operators]
        assert "+" in symbols
        assert "-" in symbols
        assert "*" in symbols
        assert "/" in symbols
        assert "^" in symbols
        assert "%" in symbols
        assert "sqrt" in symbols


class TestCalculateEndpoint:
    """Tests for the calculate endpoint."""

    def test_addition(self, client: TestClient) -> None:
        """Test addition via API."""
        response = client.post(
            "/api/calculate",
            json={"operand1": 5, "operator": "+", "operand2": 3},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["result"] == 8
        assert data["display"] == "8"

    def test_subtraction(self, client: TestClient) -> None:
        """Test subtraction via API."""
        response = client.post(
            "/api/calculate",
            json={"operand1": 10, "operator": "-", "operand2": 4},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["result"] == 6
        assert data["display"] == "6"

    def test_multiplication(self, client: TestClient) -> None:
        """Test multiplication via API."""
        response = client.post(
            "/api/calculate",
            json={"operand1": 6, "operator": "*", "operand2": 7},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["result"] == 42
        assert data["display"] == "42"

    def test_division(self, client: TestClient) -> None:
        """Test division via API."""
        response = client.post(
            "/api/calculate",
            json={"operand1": 20, "operator": "/", "operand2": 4},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["result"] == 5
        assert data["display"] == "5"

    def test_division_float_result(self, client: TestClient) -> None:
        """Test division with float result."""
        response = client.post(
            "/api/calculate",
            json={"operand1": 10, "operator": "/", "operand2": 4},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["result"] == 2.5
        assert data["display"] == "2.5"

    def test_power(self, client: TestClient) -> None:
        """Test power operation via API."""
        response = client.post(
            "/api/calculate",
            json={"operand1": 2, "operator": "^", "operand2": 8},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["result"] == 256
        assert data["display"] == "256"

    def test_modulo(self, client: TestClient) -> None:
        """Test modulo operation via API."""
        response = client.post(
            "/api/calculate",
            json={"operand1": 17, "operator": "%", "operand2": 5},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["result"] == 2
        assert data["display"] == "2"

    def test_sqrt(self, client: TestClient) -> None:
        """Test square root via API."""
        response = client.post(
            "/api/calculate",
            json={"operand1": 16, "operator": "sqrt"},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["result"] == 4
        assert data["display"] == "4"

    def test_sqrt_float_result(self, client: TestClient) -> None:
        """Test square root with float result."""
        response = client.post(
            "/api/calculate",
            json={"operand1": 2, "operator": "sqrt"},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["display"].startswith("1.41421")

    def test_negative_numbers(self, client: TestClient) -> None:
        """Test calculation with negative numbers."""
        response = client.post(
            "/api/calculate",
            json={"operand1": -5, "operator": "+", "operand2": 3},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["result"] == -2
        assert data["display"] == "-2"

    def test_float_operands(self, client: TestClient) -> None:
        """Test calculation with float operands."""
        response = client.post(
            "/api/calculate",
            json={"operand1": 3.14, "operator": "*", "operand2": 2},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["display"] == "6.28"


class TestCalculateErrors:
    """Tests for error handling in calculate endpoint."""

    def test_division_by_zero(self, client: TestClient) -> None:
        """Test division by zero returns error."""
        response = client.post(
            "/api/calculate",
            json={"operand1": 10, "operator": "/", "operand2": 0},
        )
        assert response.status_code == 400
        data = response.json()
        detail = data["detail"]
        assert detail["success"] is False
        assert "DIVISIONBYZERO" in detail["code"]

    def test_negative_sqrt(self, client: TestClient) -> None:
        """Test square root of negative number returns error."""
        response = client.post(
            "/api/calculate",
            json={"operand1": -4, "operator": "sqrt"},
        )
        assert response.status_code == 400
        data = response.json()
        detail = data["detail"]
        assert detail["success"] is False
        assert "NEGATIVESQRT" in detail["code"]

    def test_invalid_operator(self, client: TestClient) -> None:
        """Test invalid operator returns error."""
        response = client.post(
            "/api/calculate",
            json={"operand1": 5, "operator": "@", "operand2": 3},
        )
        assert response.status_code == 400
        data = response.json()
        detail = data["detail"]
        assert detail["success"] is False
        assert "INVALID_OPERATOR" in detail["code"]

    def test_missing_operand_for_binary(self, client: TestClient) -> None:
        """Test binary operator without second operand returns error."""
        response = client.post(
            "/api/calculate",
            json={"operand1": 5, "operator": "+"},
        )
        assert response.status_code == 400
        data = response.json()
        detail = data["detail"]
        assert detail["success"] is False
        assert "MISSING_OPERAND" in detail["code"]


class TestFrontendServing:
    """Tests for frontend file serving."""

    def test_serve_index(self, client: TestClient) -> None:
        """Test that index.html is served at root."""
        response = client.get("/")
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]
        assert "Calculator" in response.text

    def test_serve_css(self, client: TestClient) -> None:
        """Test that CSS file is served."""
        response = client.get("/css/style.css")
        assert response.status_code == 200
        assert "text/css" in response.headers["content-type"]

    def test_serve_js(self, client: TestClient) -> None:
        """Test that JS file is served."""
        response = client.get("/js/app.js")
        assert response.status_code == 200
        assert "javascript" in response.headers["content-type"]
