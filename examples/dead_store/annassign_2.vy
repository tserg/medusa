# @version ^0.3.7

@external
def baz() -> uint256:
    x: uint256 = 1  # Should not raise
    y: uint256 = x  # Should raise
    z: uint256 = 3
    return z
