# @version ^0.3.7

from vyper.interfaces import ERC20


@external
def foo(a: address) -> uint256:
    x: uint256 = ERC20(a).balanceOf(a)
    return x
