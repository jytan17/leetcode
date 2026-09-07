# 567. Permutation in String

- Link: https://leetcode.com/problems/permutation-in-string/
- Difficulty: Medium
- Category: Sliding Window (NeetCode 150)

## Statement

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise. In other words, return `true` if one of `s1`'s permutations is a substring of `s2`.

### Examples

- `s1 = "ab", s2 = "eidbaooo"` → `true` (`s2` contains `"ba"`)
- `s1 = "ab", s2 = "eidboaoo"` → `false`
- `s1 = "adc", s2 = "dcda"` → `true`

## Constraints

- 1 <= s1.length, s2.length <= 10^4
- `s1` and `s2` consist of lowercase English letters.

## Target

- Time: O(n)
- Space: O(1) — 26-letter counts

## Notes

Fixed-size window of `len(s1)` over `s2`. Compare character counts; slide by adding the entering char and removing the leaving one instead of recounting. Return `false` immediately if `len(s1) > len(s2)`. Keeping a `matches` counter of how many of the 26 letters have equal counts turns each comparison into O(1).
