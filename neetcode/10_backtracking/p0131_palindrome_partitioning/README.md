# 131. Palindrome Partitioning

- Link: https://leetcode.com/problems/palindrome-partitioning/
- Difficulty: Medium
- Category: Backtracking (NeetCode 150)

## Statement

Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

## Examples

```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Input: s = "a"
Output: [["a"]]
```

## Constraints

- `1 <= s.length <= 16`
- `s` contains only lowercase English letters.

## Target

- Time: O(n * 2^n)
- Space: O(n) recursion depth
