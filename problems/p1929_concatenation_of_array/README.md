# 1929. Concatenation of Array

Link: https://leetcode.com/problems/concatenation-of-array/

## Statement

Given integer array `nums` of length `n`, return array `ans` of length `2n`
where `ans[i] == nums[i]` and `ans[i + n] == nums[i]` for `0 <= i < n`.
(i.e. `ans` = `nums` concatenated with itself.)

## Constraints

- `1 <= n <= 1000`
- `1 <= nums[i] <= 1000`

## Examples

- Input: `nums = [1,2,1]`
  Output: `[1,2,1,1,2,1]`
- Input: `nums = [1,3,2,1]`
  Output: `[1,3,2,1,1,3,2,1]`

## Target

- Time: O(n)
- Space: O(n)
