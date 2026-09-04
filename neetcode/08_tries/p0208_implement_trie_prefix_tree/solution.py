from typing import List, Optional


class Trie:
    def __init__(self):
        raise NotImplementedError

    def insert(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError

    def startsWith(self, prefix: str) -> bool:
        raise NotImplementedError
