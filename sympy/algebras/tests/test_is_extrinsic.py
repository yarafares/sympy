import pytest

def test_is_extrinsic():
    # Import the function from the module where it is defined
    from sympy.algebras.quaternion import _is_extrinsic

    # Test valid intrinsic sequences
    assert _is_extrinsic('xyz') == True
    assert _is_extrinsic('zyx') == True

    # Test valid extrinsic sequences
    assert _is_extrinsic('XYZ') == False
    assert _is_extrinsic('ZYX') == False

    # Test invalid type
    with pytest.raises(ValueError, match='Expected seq to be a string.'):
        _is_extrinsic(123)

    # Test invalid length
    with pytest.raises(ValueError, match='Expected 3 axes, got'):
        _is_extrinsic('xy')
    with pytest.raises(ValueError, match='Expected 3 axes, got'):
        _is_extrinsic('wxyz')

    # Test mixed case
    with pytest.raises(ValueError, match='seq must either be fully uppercase'):
        _is_extrinsic('xYz')

    # Test consecutive axes
    with pytest.raises(ValueError, match='Consecutive axes must be different'):
        _is_extrinsic('xyy')
    with pytest.raises(ValueError, match='Consecutive axes must be different'):
        _is_extrinsic('xzz')

    # Test invalid characters
    with pytest.raises(ValueError, match='Expected axes from `seq` to be from'):
        _is_extrinsic('xwp')
    with pytest.raises(ValueError, match='Expected axes from `seq` to be from'):
        _is_extrinsic('XWP')

if __name__ == "__main__":
    pytest.main([__file__])
