# Problem 1313: Decompress Run-Length Encoded List

Link: https://leetcode.com/problems/decompress-run-length-encoded-list/

## Statement

List `nums` is run-length encoded: pairs `[freq_i, val_i]` at indices `2*i, 2*i+1`. Decompress to flat list where each `val_i` repeats `freq_i` times. Concatenate in order.

## Constraints

- 2 <= nums.length <= 100
- nums.length % 2 == 0
- 1 <= nums[i] <= 100

## Examples

- Input: `nums = [1,2,3,4]`
  Output: `[2,4,4,4]`
  Explanation: pair (1,2) → [2], pair (3,4) → [4,4,4].
- Input: `nums = [1,1,2,3]`
  Output: `[1,3,3]`

## Target

- Time: O(sum of freqs)
- Space: O(sum of freqs)

## Notes

LeetCode sig: `pub fn decompress_rl_elist(nums: Vec<i32>) -> Vec<i32>`. Practice: `chunks(2)`, `Vec::extend`, `std::iter::repeat(...).take(n)`.
