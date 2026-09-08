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


def test_word_dictionary_all_dots():
    d = WordDictionary()
    d.addWord("abc")
    assert d.search("...") is True
    assert d.search("..") is False
    assert d.search("....") is False


def test_word_dictionary_no_match():
    d = WordDictionary()
    d.addWord("at")
    d.addWord("and")
    d.addWord("an")
    assert d.search("a") is False
    assert d.search(".at") is False
    assert d.search("an.") is True
    assert d.search("a.d.") is False


def test_word_dictionary_empty():
    d = WordDictionary()
    assert d.search("a") is False
    assert d.search(".") is False
