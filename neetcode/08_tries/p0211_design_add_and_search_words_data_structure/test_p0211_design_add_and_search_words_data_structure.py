import pytest
from solution import WordDictionary


def test_word_dictionary_example():
    d = WordDictionary()
    d.addWord("bad")
    d.addWord("dad")
    d.addWord("mad")
    assert d.search("pad") is False
    assert d.search("bad") is True
    assert d.search(".ad") is True
    assert d.search("b..") is True


def test_word_dictionary_wildcards_and_length():
    d = WordDictionary()
    d.addWord("a")
    d.addWord("ab")
    assert d.search(".") is True
    assert d.search("a.") is True
    assert d.search("..") is True
    assert d.search("...") is False
