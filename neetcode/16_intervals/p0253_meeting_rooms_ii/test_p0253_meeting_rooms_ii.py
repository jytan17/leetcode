import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([[0, 30], [5, 10], [15, 20]],), 2),
    (([[7, 10], [2, 4]],), 1),
    (([],), 0),
    (([[1, 5], [2, 6], [3, 7]],), 3),
])
def test_min_meeting_rooms(args, expected):
    assert Solution().minMeetingRooms(*args) == expected
