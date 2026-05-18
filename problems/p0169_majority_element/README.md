# Problem 0169: Majority Element

Link: https://leetcode.com/problems/majority-element/

## Statement

Given array `nums` of size `n`, return the majority element.

Majority element appears more than `n / 2` times. Assume majority element always exists.

## Constraints

- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

## Examples

- Input: `nums = [3,2,3]`
  Output: `3`
- Input: `nums = [2,2,1,1,1,2,2]`
  Output: `2`

## Target

- Time: O(n)
- Space: O(1)

## Notes

- HashMap count → O(n) time, O(n) space.
- Sort → O(n log n); answer at `nums[n/2]`.
- Boyer-Moore voting: O(n) time, O(1) space. Candidate + count; flip on count==0.
