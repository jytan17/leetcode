import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (("ababcbacadefegdehijhklij",), [9, 7, 8]),
    (("eccbbbbdec",), [10]),
    # Edge cases
    (("a",), [1]),
    (("abcabc",), [6]),
    (("abcdef",), [1, 1, 1, 1, 1, 1]),
    (("aaa",), [3]),
])
def test_partition_labels(args, expected):
    assert Solution().partitionLabels(*args) == expected
