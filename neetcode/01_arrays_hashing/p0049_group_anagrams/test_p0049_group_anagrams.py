import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    ((["eat", "tea", "tan", "ate", "nat", "bat"],), [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
    (([""],), [[""]]),
    ((["a"],), [["a"]]),
])
def test_group_anagrams(args, expected):
    assert sorted(sorted(x) for x in Solution().groupAnagrams(*args)) == sorted(sorted(x) for x in expected)
