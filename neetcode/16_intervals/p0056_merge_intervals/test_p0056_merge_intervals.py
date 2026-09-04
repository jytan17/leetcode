import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([[1, 3], [2, 6], [8, 10], [15, 18]],), [[1, 6], [8, 10], [15, 18]]),
    (([[1, 4], [4, 5]],), [[1, 5]]),
    (([[1, 4], [0, 4]],), [[0, 4]]),
])
def test_merge(args, expected):
    assert Solution().merge(*args) == expected
