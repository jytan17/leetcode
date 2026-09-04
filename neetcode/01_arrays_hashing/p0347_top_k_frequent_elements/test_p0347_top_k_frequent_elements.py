import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([1, 1, 1, 2, 2, 3], 2), [1, 2]),
    (([1], 1), [1]),
    (([4, 4, 4, 5, 5, 6], 3), [4, 5, 6]),
])
def test_top_k_frequent(args, expected):
    assert sorted(Solution().topKFrequent(*args)) == sorted(expected)
