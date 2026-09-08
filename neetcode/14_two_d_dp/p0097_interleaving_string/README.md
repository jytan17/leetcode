# 97. Interleaving String

- Link: https://leetcode.com/problems/interleaving-string/
- Difficulty: Medium
- Category: 2-D Dynamic Programming (NeetCode 150)

## Statement

Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an interleaving of `s1` and `s2`.

An interleaving of two strings `s1` and `s2` is a configuration where `s1` and `s2` are divided into `n` and `m` substrings respectively, such that:

- `s1 = s1_1 + s1_2 + ... + s1_n`
- `s2 = s2_1 + s2_2 + ... + s2_m`
- `|n - m| <= 1`
- The interleaving is `s1_1 + s2_1 + s1_2 + s2_2 + ...` or `s2_1 + s1_1 + s2_2 + s1_2 + ...`

## Examples

```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Input: s1 = "", s2 = "", s3 = ""
Output: true
```

## Constraints

- `0 <= s1.length, s2.length <= 100`
- `0 <= s3.length <= 200`
- `s1`, `s2`, and `s3` consist of lowercase English letters.

## Target

- Time: O(m × n)
- Space: O(n)
