# 202. Happy Number

- Link: https://leetcode.com/problems/happy-number/
- Difficulty: Easy
- Category: Math & Geometry (NeetCode 150)

## Statement

Write an algorithm to determine if a number `n` is happy.

A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return `true` if `n` is a happy number, and `false` if not.

## Examples

```
Input: n = 19
Output: true
Explanation:
1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1

Input: n = 2
Output: false
```

## Constraints

- `1 <= n <= 2^31 - 1`

## Target

- Time: O(log n)
- Space: O(1) (with Floyd's cycle detection)
