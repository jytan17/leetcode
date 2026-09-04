import pytest
from solution import Solution


@pytest.mark.parametrize("strs", [
    ["lint", "code", "love", "you"],
    ["we", "say", ":", "yes"],
    [""],
    ["", "", ""],
    ["a#b", "2#xy", "###"],
    [],
])
def test_encode_decode_roundtrip(strs):
    sol = Solution()
    assert sol.decode(sol.encode(strs)) == strs
