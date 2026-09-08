# 287. Find the Duplicate Number

- Link: https://leetcode.com/problems/find-the-duplicate-number/
- Difficulty: Medium
- Category: Linked List (NeetCode 150)

## Statement

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only one repeated number in `nums`, return this repeated number.

You must solve the problem without modifying the array `nums` and using only constant extra space.

## Examples

```
Input: nums = [1,3,4,2,2]
Output: 2

Input: nums = [3,1,3,4,2]
Output: 3

Input: nums = [3,3,3,3,3]
Output: 3
```

## Constraints

- `1 <= n <= 10^5`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- There is only one repeated number in `nums`, but it could be repeated more than once.

## Target

- Time: O(n)
- Space: O(1)

**Follow up:** How can you prove that at least one duplicate number must exist in `nums`? (Pigeonhole principle)
