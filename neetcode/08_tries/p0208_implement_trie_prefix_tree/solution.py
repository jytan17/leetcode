from collections import defaultdict
from typing import List, Optional


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_word = False

    def insert(self, word: str, idx: int = 0) -> None:
        if idx == len(word):
            self.is_word = True
            return

        self.children[word[idx]].insert(word, idx + 1)

    def search(self, word: str, idx: int = 0) -> bool:
        if idx == len(word):
            return self.is_word

        if word[idx] not in self.children:
            return False
        return self.children[word[idx]].search(word, idx + 1)

    def startsWith(self, prefix: str, idx: int = 0) -> bool:
        if idx == len(prefix):
            return True

        if prefix[idx] not in self.children:
            return False
        return self.children[prefix[idx]].startsWith(prefix, idx + 1)
