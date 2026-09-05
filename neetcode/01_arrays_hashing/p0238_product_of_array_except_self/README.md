# 238. Product of Array Except Self

- Link: https://leetcode.com/problems/product-of-array-except-self/
- Difficulty: Medium
- Category: Arrays & Hashing (NeetCode 150)

## Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and **without using the division operation**.

### Examples

- `nums = [1,2,3,4]` → `[24,12,8,6]`
- `nums = [-1,1,0,-3,3]` → `[0,0,9,0,0]`

## Constraints

- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- Product of any prefix/suffix fits in 32-bit integer.

## Target

- Time: O(n)
- Space: O(1) — output array doesn't count

## Notes

Two passes: prefix products left-to-right, then suffix products right-to-left. Multiply into result array.
