# 5. Longest Palindromic Substring

- Link: https://leetcode.com/problems/longest-palindromic-substring/
- Difficulty: Medium
- Category: 1-D Dynamic Programming (NeetCode 150)

## Statement

Given a string `s`, return the longest palindromic substring in `s`.

## Examples

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"
```

## Constraints

- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

## Target

- Time: O(n²)
- Space: O(1) with expand-around-center
