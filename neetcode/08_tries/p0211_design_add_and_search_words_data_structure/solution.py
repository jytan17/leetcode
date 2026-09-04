from typing import List, Optional


class WordDictionary:
    def __init__(self):
        raise NotImplementedError

    def addWord(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError
