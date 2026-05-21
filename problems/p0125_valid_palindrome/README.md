# 125. Valid Palindrome

https://leetcode.com/problems/valid-palindrome/

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Examples

- `s = "A man, a plan, a canal: Panama"` → `true` (`"amanaplanacanalpanama"`)
- `s = "race a car"` → `false` (`"raceacar"`)
- `s = " "` → `true` (empty after filter)

## Constraints

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

## Target

- Time: O(n)
- Space: O(1) — two pointers, no extra allocation
