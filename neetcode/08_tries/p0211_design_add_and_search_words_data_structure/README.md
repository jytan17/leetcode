# 211. Design Add and Search Words Data Structure

- Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
- Difficulty: Medium
- Category: Tries (NeetCode 150)

## Statement

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:

- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds `word` to the data structure, it can be matched later.
- `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

## Examples

```
Input:
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

Output:
[null,null,null,null,false,true,true,true]
```

## Constraints

- `1 <= word.length <= 25`
- `word` in `addWord` consists of lowercase English letters.
- `word` in `search` consists of `'.'` or lowercase English letters.
- There will be at most `3` dots in `word` for `search` queries.
- At most `10^4` calls will be made to `addWord` and `search`.

## Target

- Time: O(m) for addWord, O(m * 26^d) for search where d is number of dots
- Space: O(n * m) total
