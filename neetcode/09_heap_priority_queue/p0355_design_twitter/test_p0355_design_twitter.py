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


def test_twitter_follow_self():
    t = Twitter()
    t.follow(1, 1)
    t.postTweet(1, 10)
    assert t.getNewsFeed(1) == [10]


def test_twitter_unfollow_without_follow():
    t = Twitter()
    t.unfollow(1, 2)
    t.postTweet(2, 5)
    assert t.getNewsFeed(1) == []


def test_twitter_multiple_followees():
    t = Twitter()
    t.follow(1, 2)
    t.follow(1, 3)
    t.postTweet(2, 10)
    t.postTweet(3, 20)
    t.postTweet(1, 30)
    assert t.getNewsFeed(1) == [30, 20, 10]
