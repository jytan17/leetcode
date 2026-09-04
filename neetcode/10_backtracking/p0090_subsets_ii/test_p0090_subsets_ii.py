import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([1, 2, 2],), [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
    (([0],), [[], [0]]),
])
def test_subsets_with_dup(args, expected):
    assert sorted(sorted(x) for x in Solution().subsetsWithDup(*args)) == sorted(sorted(x) for x in expected)
