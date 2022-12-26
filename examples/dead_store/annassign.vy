# @version ^0.3.7

@external
def foo() -> uint256:
    x: uint256 = 1  # Should raise
    y: uint256 = 2
    return y
