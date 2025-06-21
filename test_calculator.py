import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    """Fixture to create a Calculator instance."""
    return Calculator()


def test_add(calc):
    """Test addition functionality."""
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0


def test_subtract(calc):
    """Test subtraction functionality."""
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(1, 5) == -4
    assert calc.subtract(0, 0) == 0


def test_multiply(calc):
    """Test multiplication functionality."""
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 5) == 0


def test_divide(calc):
    """Test division functionality."""
    assert calc.divide(6, 2) == 3
    assert calc.divide(5, 2) == 2.5
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        calc.divide(10, 0)
