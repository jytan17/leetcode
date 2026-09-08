# 678. Valid Parenthesis String

- Link: https://leetcode.com/problems/valid-parenthesis-string/
- Difficulty: Medium
- Category: Greedy (NeetCode 150)

## Statement

Given a string `s` containing only three types of characters: `'('`, `')'` and `'*'`, return `true` if `s` is valid.

The following rules define a valid string:

- Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
- Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
- Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
- `'*'` could be treated as a single right parenthesis `')'` OR a single left parenthesis `'('` OR an empty string `""`.

## Examples

```
Input: s = "()"
Output: true

Input: s = "(*)"
Output: true

Input: s = "(*))"
Output: true
```

## Constraints

- `1 <= s.length <= 100`
- `s[i]` is `'('`, `')'` or `'*'`.

## Target

- Time: O(n)
- Space: O(1)
