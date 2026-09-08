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


def test_time_map_multiple_keys():
    tm = TimeMap()
    tm.set("k1", "v1", 1)
    tm.set("k2", "v2", 2)
    assert tm.get("k1", 5) == "v1"
    assert tm.get("k2", 5) == "v2"
    assert tm.get("k1", 0) == ""


def test_time_map_overwrite_same_key():
    tm = TimeMap()
    tm.set("key", "a", 1)
    tm.set("key", "b", 2)
    tm.set("key", "c", 4)
    assert tm.get("key", 1) == "a"
    assert tm.get("key", 2) == "b"
    assert tm.get("key", 3) == "b"
    assert tm.get("key", 4) == "c"
    assert tm.get("key", 100) == "c"


def test_time_map_exact_vs_floor_timestamp():
    tm = TimeMap()
    tm.set("x", "first", 10)
    tm.set("x", "second", 20)
    assert tm.get("x", 9) == ""
    assert tm.get("x", 10) == "first"
    assert tm.get("x", 15) == "first"
    assert tm.get("x", 20) == "second"
    assert tm.get("x", 25) == "second"
