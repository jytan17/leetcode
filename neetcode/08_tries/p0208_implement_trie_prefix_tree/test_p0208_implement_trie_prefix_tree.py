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


def test_trie_prefix_not_word():
    t = Trie()
    t.insert("hello")
    assert t.startsWith("hel") is True
    assert t.search("hel") is False
    assert t.startsWith("hello") is True
    assert t.search("hello") is True
    assert t.startsWith("helloo") is False


def test_trie_multiple_words_shared_prefix():
    t = Trie()
    t.insert("car")
    t.insert("card")
    t.insert("care")
    t.insert("cared")
    assert t.search("car") is True
    assert t.search("card") is True
    assert t.search("care") is True
    assert t.search("cared") is True
    assert t.search("cars") is False
    assert t.startsWith("car") is True
    assert t.startsWith("care") is True


def test_trie_single_char():
    t = Trie()
    t.insert("b")
    assert t.search("b") is True
    assert t.search("a") is False
    assert t.startsWith("b") is True
    assert t.startsWith("a") is False
