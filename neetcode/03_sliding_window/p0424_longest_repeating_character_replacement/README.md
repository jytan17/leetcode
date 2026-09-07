# 424. Longest Repeating Character Replacement

- Link: https://leetcode.com/problems/longest-repeating-character-replacement/
- Difficulty: Medium
- Category: Sliding Window (NeetCode 150)

## Statement

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

### Examples

- `s = "ABAB", k = 2` → `4` (replace both `A`s with `B`, or both `B`s with `A`)
- `s = "AABABBA", k = 1` → `4` (replace the middle `A` to get `"AABBBBA"`, window `"BBBB"`)

## Constraints

- 1 <= s.length <= 10^5
- `s` consists of only uppercase English letters.
- 0 <= k <= s.length

## Target

- Time: O(n)
- Space: O(1) — 26-letter count map

## Notes

A window is valid when `windowLen - maxCount <= k`, where `maxCount` is the frequency of the most common char in the window. Shrink from the left when invalid. `maxCount` never needs to be decreased — a stale-high value only blocks growth, so the answer stays correct while keeping the pass O(n).
