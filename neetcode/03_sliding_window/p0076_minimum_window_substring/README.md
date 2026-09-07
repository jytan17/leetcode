# 76. Minimum Window Substring

- Link: https://leetcode.com/problems/minimum-window-substring/
- Difficulty: Hard
- Category: Sliding Window (NeetCode 150)

## Statement

Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

The answer is guaranteed to be unique.

### Examples

- `s = "ADOBECODEBANC", t = "ABC"` → `"BANC"`
- `s = "a", t = "a"` → `"a"`
- `s = "a", t = "aa"` → `""` (only one `a` in `s`)

## Constraints

- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- `s` and `t` consist of uppercase and lowercase English letters.

## Target

- Time: O(m + n)
- Space: O(charset)

## Notes

Need-count map from `t`, plus a `have` / `need` pair counting how many distinct chars hit their required count. Expand right; while `have == need`, record the window and shrink from the left. Duplicates matter — only decrement `have` when a count drops *below* what's required.
