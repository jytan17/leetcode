from typing import List, Optional


class Twitter:
    def __init__(self):
        raise NotImplementedError

    def postTweet(self, userId: int, tweetId: int) -> None:
        raise NotImplementedError

    def getNewsFeed(self, userId: int) -> List[int]:
        raise NotImplementedError

    def follow(self, followerId: int, followeeId: int) -> None:
        raise NotImplementedError

    def unfollow(self, followerId: int, followeeId: int) -> None:
        raise NotImplementedError
