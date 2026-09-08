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


def test_kth_largest_k_equals_length():
    k = KthLargest(3, [1, 2, 3])
    assert k.add(0) == 1
    assert k.add(4) == 2


def test_kth_largest_duplicates():
    k = KthLargest(2, [0])
    assert k.add(0) == 0
    assert k.add(0) == 0
    assert k.add(1) == 0
    assert k.add(1) == 1
