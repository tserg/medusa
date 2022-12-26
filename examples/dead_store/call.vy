# @version ^0.3.7

@internal
def _bar(i: uint256) -> uint256:
    return i + 1


@external
def bar() -> uint256:
    y: uint256 = 2  # Should not raise
    x: uint256 = self._bar(y)
    return x
