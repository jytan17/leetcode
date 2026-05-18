# Problem 0344: Reverse String

Link: https://leetcode.com/problems/reverse-string/

## Statement

Reverse a string given as a char array `s`. Modify in-place with O(1) extra memory.

## Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is a printable ASCII character.

## Examples

- Input: `s = ["h","e","l","l","o"]`
  Output: `["o","l","l","e","h"]`
- Input: `s = ["H","a","n","n","a","h"]`
  Output: `["h","a","n","n","a","H"]`

## Target

- Time: O(n)
- Space: O(1)

## Notes

- Two pointer swap, left/right toward center.
- Or `s.reverse()` (stdlib) — works on `Vec<char>`.
