import pytest
from sympy import symbols, Integer, Rational, sqrt
from sympy.algebras.quaternion import _check_norm

def test_check_norm():
    x, y, z = symbols('x y z')

    # Test with valid norms
    elements = [Integer(3), Integer(4)]
    norm = Integer(5)
    _check_norm(elements, norm)  # Should pass without exception

    elements = [Integer(1), Integer(1), Integer(1)]
    norm = sqrt(3)
    _check_norm(elements, norm)  # Should pass without exception

    # Test with valid None norm
    elements = [Integer(3), Integer(4)]
    norm = None
    _check_norm(elements, norm)  # Should pass without exception

    # Test with negative norm
    norm = Integer(-5)
    with pytest.raises(ValueError, match="Input norm must be positive."):
        _check_norm(elements, norm)

    # Test with incompatible norm
    norm = Integer(6)
    with pytest.raises(ValueError, match="Incompatible value for norm."):
        _check_norm(elements, norm)

    # Test with non-number norm
    norm = symbols('n')
    _check_norm(elements, norm)  # Should pass without exception as norm is not a number

    # Test with non-numerical elements
    elements = [x, y, z]
    norm = Integer(1)
    _check_norm(elements, norm)  # Should pass without exception as elements are not numerical

if __name__ == "__main__":
    pytest.main([__file__])
