# 15. 3Sum

- Link: https://leetcode.com/problems/3sum/
- Difficulty: Medium
- Category: Two Pointers (NeetCode 150)

## Statement

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

The solution set must not contain duplicate triplets. The order of the output and the order within each triplet do not matter.

### Examples

- `nums = [-1,0,1,2,-1,-4]` → `[[-1,-1,2],[-1,0,1]]`
- `nums = [0,1,1]` → `[]`
- `nums = [0,0,0]` → `[[0,0,0]]`

## Constraints

- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

## Target

- Time: O(n^2)
- Space: O(1) extra, ignoring the sort and the output

## Notes

Sort, then for each index `i` run the sorted two-pointer scan on the rest for `-nums[i]`. Skip duplicates: `continue` when `nums[i] == nums[i-1]`, and advance the left pointer past repeats after recording a hit. Break early once `nums[i] > 0`.
