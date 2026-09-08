import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([[0, 30], [5, 10], [15, 20]],), 2),
    (([[7, 10], [2, 4]],), 1),
    # Edge cases
    (([[1, 5]],), 1),
    (([[1, 5], [2, 6], [3, 7]],), 3),
    (([[1, 5], [5, 10], [10, 15]],), 1),
    (([[1, 3], [2, 4], [3, 5]],), 2),
])
def test_min_meeting_rooms(args, expected):
    assert Solution().minMeetingRooms(*args) == expected
