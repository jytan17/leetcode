# Problem 0242: Valid Anagram

Link: https://leetcode.com/problems/valid-anagram/

## Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, `false` otherwise. Anagram = rearrangement of same letters, same counts.

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

## Examples

- Input: `s = "anagram", t = "nagaram"`
  Output: `true`
- Input: `s = "rat", t = "car"`
  Output: `false`

## Target

- Time: O(n)
- Space: O(1) (fixed 26-letter alphabet) or O(k) for unicode follow-up

## Notes

Follow-up: what if inputs contain unicode? Then need HashMap, not [i32; 26].
