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


def test_detect_squares_empty():
    d = DetectSquares()
    assert d.count([0, 0]) == 0


def test_detect_squares_unit_square():
    d = DetectSquares()
    d.add([0, 0])
    d.add([0, 1])
    d.add([1, 0])
    assert d.count([1, 1]) == 1


def test_detect_squares_multiple_squares():
    d = DetectSquares()
    d.add([0, 0])
    d.add([0, 2])
    d.add([2, 0])
    d.add([0, 1])
    d.add([1, 0])
    assert d.count([2, 2]) == 1
    assert d.count([1, 1]) == 1


def test_detect_squares_duplicates():
    d = DetectSquares()
    d.add([0, 0])
    d.add([0, 0])
    d.add([0, 1])
    d.add([1, 0])
    assert d.count([1, 1]) == 2
