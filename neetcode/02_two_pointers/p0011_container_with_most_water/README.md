# 11. Container With Most Water

- Link: https://leetcode.com/problems/container-with-most-water/
- Difficulty: Medium
- Category: Two Pointers (NeetCode 150)

## Statement

Given an integer array `height` of length `n`, there are `n` vertical lines where the endpoints of the i-th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container holding the most water. Return that maximum amount. You may not slant the container.

### Examples

- `height = [1,8,6,2,5,4,8,3,7]` → `49` (lines at index 1 and 8: `min(8,7) * 7`)
- `height = [1,1]` → `1`

## Constraints

- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

## Target

- Time: O(n)
- Space: O(1)

## Notes

Widest pair first, then shrink. Area = `min(height[l], height[r]) * (r - l)`. Move the shorter side inward — moving the taller one can only lose width without gaining height.
