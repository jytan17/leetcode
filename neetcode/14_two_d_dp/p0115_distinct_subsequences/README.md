# 115. Distinct Subsequences

- Link: https://leetcode.com/problems/distinct-subsequences/
- Difficulty: Hard
- Category: 2-D Dynamic Programming (NeetCode 150)

## Statement

Given two strings `s` and `t`, return the number of distinct subsequences of `s` which equals `t`.

The test cases are generated so that the answer fits on a 32-bit signed integer.

## Examples

```
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabb_bit
rab_bbit
ra_bbbit

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
ba_g___
ba____g
b__g__g
___gb_g
____bag
```

## Constraints

- `1 <= s.length, t.length <= 1000`
- `s` and `t` consist of English letters.

## Target

- Time: O(m × n)
- Space: O(n)
