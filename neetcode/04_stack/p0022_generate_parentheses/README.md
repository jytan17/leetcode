# 22. Generate Parentheses

- Link: https://leetcode.com/problems/generate-parentheses/
- Difficulty: Medium
- Category: Stack (NeetCode 150)

## Statement

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## Examples

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]
```

## Constraints

- `1 <= n <= 8`

## Target

- Time: O(4^n / sqrt(n)) — nth Catalan number
- Space: O(n) — recursion depth
