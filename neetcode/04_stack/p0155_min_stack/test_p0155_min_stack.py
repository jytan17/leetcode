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
