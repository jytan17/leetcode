# 242. Valid Anagram

- Link: https://leetcode.com/problems/valid-anagram/
- Difficulty: Easy
- Category: Arrays & Hashing (NeetCode 150)

## Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An anagram is a word formed by rearranging the letters of a different word, using all the original letters exactly once.

### Examples

- `s = "anagram", t = "nagaram"` → `true`
- `s = "rat", t = "car"` → `false`

## Constraints

- 1 <= s.length, t.length <= 5 * 10^4
- `s` and `t` consist of lowercase English letters.

## Target

- Time: O(n)
- Space: O(1) — fixed 26-char alphabet

## Notes

Count chars in both strings, compare counts. Or sort both and compare (O(n log n)).
