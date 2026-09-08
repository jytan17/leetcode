import pytest
from solution import MinStack


def test_min_stack_example():
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.getMin() == -3
    s.pop()
    assert s.top() == 0
    assert s.getMin() == -2


def test_min_stack_duplicates():
    s = MinStack()
    s.push(1)
    s.push(1)
    s.push(2)
    assert s.getMin() == 1
    s.pop()
    assert s.getMin() == 1
    s.pop()
    assert s.getMin() == 1


def test_min_stack_single_element():
    s = MinStack()
    s.push(42)
    assert s.top() == 42
    assert s.getMin() == 42
    s.pop()


def test_min_stack_decreasing_then_pop():
    s = MinStack()
    s.push(3)
    s.push(2)
    s.push(1)
    assert s.getMin() == 1
    s.pop()
    assert s.getMin() == 2
    s.pop()
    assert s.getMin() == 3


def test_min_stack_negative_values():
    s = MinStack()
    s.push(-1)
    s.push(-2)
    s.push(-3)
    assert s.getMin() == -3
    assert s.top() == -3
    s.pop()
    assert s.getMin() == -2
