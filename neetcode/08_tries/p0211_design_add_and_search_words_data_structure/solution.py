from typing import List, Optional


class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        cur = self.trie
        for char in word:
            if char not in cur.children:
                cur.children[char] = Trie()
            cur = cur.children[char]

        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self.trie

        def bt(trie, idx):
            if idx == len(word):
                return trie.is_word

            char = word[idx]
            if char == ".":
                for wild in trie.children:
                    if bt(trie.children[wild], idx + 1):
                        return True
            elif char in trie.children:
                return bt(trie.children[char], idx + 1)
            return False

        return bt(self.trie, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
