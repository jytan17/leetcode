# 3. Longest Substring Without Repeating Characters

- Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
- Difficulty: Medium
- Category: Sliding Window (NeetCode 150)

## Statement

Given a string `s`, find the length of the longest substring without duplicate characters.

### Examples

- `s = "abcabcbb"` → `3` (`"abc"`)
- `s = "bbbbb"` → `1` (`"b"`)
- `s = "pwwkew"` → `3` (`"wke"`; `"pwke"` is a subsequence, not a substring)
- `s = ""` → `0`

## Constraints

- 0 <= s.length <= 5 * 10^4
- `s` consists of English letters, digits, symbols and spaces.

## Target

- Time: O(n)
- Space: O(min(n, charset))

## Notes

Window with a set: extend right, and while the new char is already in the set, pop from the left. Alternative: map char → last index and jump `left = max(left, lastIndex + 1)` — the `max` matters, or a stale index drags the window backward.
