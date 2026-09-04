import pytest
from solution import Trie


def test_trie_example():
    t = Trie()
    t.insert("apple")
    assert t.search("apple") is True
    assert t.search("app") is False
    assert t.startsWith("app") is True
    t.insert("app")
    assert t.search("app") is True


def test_trie_empty_and_missing():
    t = Trie()
    assert t.search("a") is False
    assert t.startsWith("a") is False
    t.insert("a")
    assert t.search("a") is True
