# 167. Two Sum II - Input Array Is Sorted

- Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
- Difficulty: Medium
- Category: Two Pointers (NeetCode 150)

## Statement

Given a 1-indexed array of integers `numbers` sorted in non-decreasing order, find two numbers that add up to a specific `target`. Return the indices of the two numbers, `index1` and `index2`, as `[index1, index2]` with `1 <= index1 < index2 <= numbers.length`.

There is exactly one solution. You may not use the same element twice. Your solution must use only constant extra space.

### Examples

- `numbers = [2,7,11,15], target = 9` → `[1,2]`
- `numbers = [2,3,4], target = 6` → `[1,3]`
- `numbers = [-1,0], target = -1` → `[1,2]`

## Constraints

- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- `numbers` is sorted in non-decreasing order.
- -1000 <= target <= 1000
- Exactly one valid answer exists.

## Target

- Time: O(n)
- Space: O(1)

## Notes

Left at 0, right at end. Sum too small → `left += 1`; too big → `right -= 1`. Return 1-indexed. Hash map would work but violates the O(1) space requirement.
