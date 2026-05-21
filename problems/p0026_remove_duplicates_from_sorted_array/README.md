# 26. Remove Duplicates from Sorted Array

https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`. To get accepted, you need to do the following:

- Change `nums` so that the first `k` elements contain the unique elements in the order they were present originally.
- The remaining elements of `nums` past `k` do not matter.
- Return `k`.

## Examples

- `nums = [1,1,2]` → `k = 2`, `nums = [1,2,_]`
- `nums = [0,0,1,1,1,2,2,3,3,4]` → `k = 5`, `nums = [0,1,2,3,4,_,_,_,_,_]`

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order.

## Target

- Time: O(n)
- Space: O(1) — in-place, two pointers
