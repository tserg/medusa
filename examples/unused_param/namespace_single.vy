# @version ^0.3.7

owner: uint256

@external
def test(owner: uint256) -> uint256:
    self.owner = 123  # Should not raise
    return 1
