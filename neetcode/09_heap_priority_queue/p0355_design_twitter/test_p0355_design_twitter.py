import pytest
from solution import Twitter


def test_twitter_example():
    t = Twitter()
    t.postTweet(1, 5)
    assert t.getNewsFeed(1) == [5]
    t.follow(1, 2)
    t.postTweet(2, 6)
    assert t.getNewsFeed(1) == [6, 5]
    t.unfollow(1, 2)
    assert t.getNewsFeed(1) == [5]


def test_twitter_feed_caps_at_ten():
    t = Twitter()
    for i in range(12):
        t.postTweet(1, i)
    assert t.getNewsFeed(1) == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]


def test_twitter_empty_feed():
    t = Twitter()
    assert t.getNewsFeed(9) == []
