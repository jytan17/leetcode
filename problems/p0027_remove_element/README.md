# Problem 0027: Remove Element

Link: https://leetcode.com/problems/remove-element/

## Statement

Given integer array `nums` and integer `val`, remove all occurrences of `val` in `nums` **in-place**. Order of remaining elements may change. Return number of elements not equal to `val`.

Let `k` = count of elements != `val`. First `k` slots of `nums` must contain those elements (any order). Rest of array don't matter.

## Constraints

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

## Examples

- Input: `nums = [3,2,2,3]`, `val = 3`
  Output: `2`, `nums = [2,2,_,_]`
- Input: `nums = [0,1,2,2,3,0,4,2]`, `val = 2`
  Output: `5`, `nums = [0,1,4,0,3,_,_,_]`

## Target

- Time: O(n)
- Space: O(1)

## Notes

- Two pointer: write index lags read index.
- Order of kept elements need not preserve.
