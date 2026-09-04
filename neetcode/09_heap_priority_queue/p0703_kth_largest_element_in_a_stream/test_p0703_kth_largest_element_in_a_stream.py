import pytest
from solution import KthLargest


def test_kth_largest_example():
    k = KthLargest(3, [4, 5, 8, 2])
    assert k.add(3) == 4
    assert k.add(5) == 5
    assert k.add(10) == 5
    assert k.add(9) == 8
    assert k.add(4) == 8


def test_kth_largest_empty_start():
    k = KthLargest(1, [])
    assert k.add(-3) == -3
    assert k.add(-2) == -2
    assert k.add(-4) == -2
