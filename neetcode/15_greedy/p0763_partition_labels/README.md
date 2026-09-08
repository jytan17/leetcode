# 763. Partition Labels

- Link: https://leetcode.com/problems/partition-labels/
- Difficulty: Medium
- Category: Greedy (NeetCode 150)

## Statement

You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be `s`.

Return a list of integers representing the size of these parts.

## Examples

```
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
Each letter appears in at most one part.

Input: s = "eccbbbbdec"
Output: [10]
```

## Constraints

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.

## Target

- Time: O(n)
- Space: O(1) (26 letters)
