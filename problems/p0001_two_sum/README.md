# Problem 0001: Two Sum

Link: https://leetcode.com/problems/two-sum/

## Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input has **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

## Examples

- Input: `nums = [2,7,11,15], target = 9` → Output: `[0,1]`
- Input: `nums = [3,2,4], target = 6` → Output: `[1,2]`
- Input: `nums = [3,3], target = 6` → Output: `[0,1]`

## Target

- Time: O(n) — single pass with hash map
- Space: O(n)

## Notes

- Brute force O(n^2) trivial; drill the hash-map one-pass.
- Hash map: `value -> index`. For each `n`, check if `target - n` already seen.
- Return order doesn't matter — tests sort before compare.
