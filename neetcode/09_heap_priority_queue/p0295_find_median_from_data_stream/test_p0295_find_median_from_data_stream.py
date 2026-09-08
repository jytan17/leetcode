import pytest
from solution import MedianFinder


def test_median_finder_example():
    m = MedianFinder()
    m.addNum(1)
    m.addNum(2)
    assert m.findMedian() == pytest.approx(1.5)
    m.addNum(3)
    assert m.findMedian() == pytest.approx(2.0)


def test_median_finder_single_and_negatives():
    m = MedianFinder()
    m.addNum(-1)
    assert m.findMedian() == pytest.approx(-1.0)
    m.addNum(-2)
    assert m.findMedian() == pytest.approx(-1.5)
    m.addNum(-3)
    assert m.findMedian() == pytest.approx(-2.0)


def test_median_finder_single_element():
    m = MedianFinder()
    m.addNum(5)
    assert m.findMedian() == pytest.approx(5.0)


def test_median_finder_duplicates():
    m = MedianFinder()
    m.addNum(1)
    m.addNum(1)
    assert m.findMedian() == pytest.approx(1.0)
    m.addNum(1)
    assert m.findMedian() == pytest.approx(1.0)


def test_median_finder_descending():
    m = MedianFinder()
    m.addNum(5)
    m.addNum(4)
    m.addNum(3)
    m.addNum(2)
    m.addNum(1)
    assert m.findMedian() == pytest.approx(3.0)
