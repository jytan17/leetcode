import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
     ["JFK", "MUC", "LHR", "SFO", "SJC"]),
    ([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]],
     ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]),
    # Edge cases
    ([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]],
     ["JFK", "NRT", "JFK", "KUL"]),
    ([["JFK", "AAA"], ["AAA", "JFK"], ["JFK", "BBB"], ["BBB", "JFK"]],
     ["JFK", "AAA", "JFK", "BBB", "JFK"]),
    ([["JFK", "ATL"]],
     ["JFK", "ATL"]),
])
def test_find_itinerary(args, expected):
    assert Solution().findItinerary(args) == expected
