import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("ababcbacadefegdehijhklij",), [9, 7, 8]),
    (("eccbbbbdec",), [10]),
    (("a",), [1]),
])
def test_partition_labels(args, expected):
    assert Solution().partitionLabels(*args) == expected
