import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # (inputs, expected_output),
])
def test_solve(args, expected):
    assert Solution().solve(*args) == expected
