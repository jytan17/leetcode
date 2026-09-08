import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([[0, 30], [5, 10], [15, 20]],), False),
    (([[7, 10], [2, 4]],), True),
    # Edge cases
    (([],), True),
    (([[1, 5]],), True),
    (([[1, 5], [5, 10]],), True),
    (([[1, 5], [4, 10]],), False),
    (([[1, 2], [3, 4], [5, 6]],), True),
])
def test_can_attend_meetings(args, expected):
    assert Solution().canAttendMeetings(*args) == expected
