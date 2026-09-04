import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([[0, 30], [5, 10], [15, 20]],), False),
    (([[7, 10], [2, 4]],), True),
    (([],), True),
])
def test_can_attend_meetings(args, expected):
    assert Solution().canAttendMeetings(*args) == expected
