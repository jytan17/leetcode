# 217. Contains Duplicate

- Link: https://leetcode.com/problems/contains-duplicate/
- Difficulty: Easy
- Category: Arrays & Hashing (NeetCode 150)

## Statement

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Examples

- `nums = [1,2,3,1]` → `true`
- `nums = [1,2,3,4]` → `false`
- `nums = [1,1,1,3,3,4,3,2,4,2]` → `true`

## Constraints

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

## Target

- Time: O(n)
- Space: O(n)

## Notes

Set: add each element, return true if already seen.
