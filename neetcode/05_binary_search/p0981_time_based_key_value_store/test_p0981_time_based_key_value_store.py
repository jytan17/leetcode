import pytest
from solution import TimeMap


def test_time_map_example():
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"
    tm.set("foo", "bar2", 4)
    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"


def test_time_map_before_first_and_missing_key():
    tm = TimeMap()
    tm.set("a", "x", 5)
    assert tm.get("a", 4) == ""
    assert tm.get("missing", 10) == ""
