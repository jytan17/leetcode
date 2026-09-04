import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    ((2, [[1, 0]]), True),
    ((2, [[1, 0], [0, 1]]), False),
    ((1, []), True),
])
def test_can_finish(args, expected):
    assert Solution().canFinish(*args) == expected
