# @version ^0.3.7

struct Foo:
    owner: uint256

owner: Foo

@external
def test(
    owner: uint256  # Should raise
) -> uint256:
    self.owner.owner = 123  # Should not count as a reference
    return 1
