# Problem 1480: Running Sum of 1d Array

Link: https://leetcode.com/problems/running-sum-of-1d-array/

## Statement

Given an array `nums`, return the running sum where `runningSum[i] = sum(nums[0]..=nums[i])`.

## Constraints

- 1 <= nums.length <= 1000
- -10^6 <= nums[i] <= 10^6

## Examples

- Input: `nums = [1,2,3,4]`
  Output: `[1,3,6,10]`
- Input: `nums = [1,1,1,1,1]`
  Output: `[1,2,3,4,5]`
- Input: `nums = [3,1,2,10,1]`
  Output: `[3,4,6,16,17]`

## Target

- Time: O(n)
- Space: O(n) for output (O(1) extra if mutating in place)

## Notes

In Rust try: `iter().scan`, `fold`, or plain index loop. In-place: `for i in 1..nums.len() { nums[i] += nums[i-1]; }`.
