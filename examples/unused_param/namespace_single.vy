# @version ^0.3.7

owner: uint256

@external
def test(
    owner: uint256  # Should raise
) -> uint256:
    self.owner = 123
    return 1
