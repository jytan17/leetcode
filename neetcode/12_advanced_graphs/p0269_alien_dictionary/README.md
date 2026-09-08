# 269. Alien Dictionary

- Link: https://leetcode.com/problems/alien-dictionary/
- Difficulty: Hard
- Category: Advanced Graphs (NeetCode 150)

## Statement

There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings `words` from the alien language's dictionary, where the strings in `words` are **sorted lexicographically** by the rules of this new language.

Derive the order of letters in this language, and return it. If the order is invalid, return an empty string. If there are multiple valid orderings, return **any** of them.

## Examples

```
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Input: words = ["z","x"]
Output: "zx"

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
```

## Constraints

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consists of only lowercase English letters.

## Target

- Time: O(C) where C = total length of all words
- Space: O(1) (26 letters max) or O(U + E) where U = unique letters
