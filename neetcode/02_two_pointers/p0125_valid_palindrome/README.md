# 125. Valid Palindrome

- Link: https://leetcode.com/problems/valid-palindrome/
- Difficulty: Easy
- Category: Two Pointers (NeetCode 150)

## Statement

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

### Examples

- `s = "A man, a plan, a canal: Panama"` → `true` (cleans to `"amanaplanacanalpanama"`)
- `s = "race a car"` → `false` (cleans to `"raceacar"`)
- `s = " "` → `true` (cleans to `""`, an empty string reads the same both ways)

## Constraints

- 1 <= s.length <= 2 * 10^5
- `s` consists only of printable ASCII characters.

## Target

- Time: O(n)
- Space: O(1)

## Notes

Left/right pointers moving inward. Skip non-alphanumeric on each side, compare lowercased. Building a cleaned string first also works but costs O(n) space.
