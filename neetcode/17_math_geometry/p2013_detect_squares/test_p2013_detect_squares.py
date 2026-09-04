import pytest
from solution import DetectSquares


def test_detect_squares_example():
    d = DetectSquares()
    d.add([3, 10])
    d.add([11, 2])
    d.add([3, 2])
    assert d.count([11, 10]) == 1
    assert d.count([14, 8]) == 0
    d.add([11, 2])
    assert d.count([11, 10]) == 2


def test_detect_squares_empty_and_degenerate():
    d = DetectSquares()
    assert d.count([0, 0]) == 0
    d.add([0, 0])
    d.add([0, 1])
    d.add([1, 0])
    assert d.count([1, 1]) == 1
    assert d.count([0, 0]) == 0
