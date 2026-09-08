# 215. Kth Largest Element in an Array

- Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
- Difficulty: Medium
- Category: Heap / Priority Queue (NeetCode 150)

## Statement

Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.

Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

Can you solve it without sorting?

## Examples

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Target

- Time: O(n) average with quickselect, O(n log k) with heap
- Space: O(k) with heap, O(1) with quickselect
