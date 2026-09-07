# 42. Trapping Rain Water

- Link: https://leetcode.com/problems/trapping-rain-water/
- Difficulty: Hard
- Category: Two Pointers (NeetCode 150)

## Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

### Examples

- `height = [0,1,0,2,1,0,1,3,2,1,2,1]` → `6`
- `height = [4,2,0,3,2,5]` → `9`

## Constraints

- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5

## Target

- Time: O(n)
- Space: O(1)

## Notes

Water above bar `i` is `min(maxLeft, maxRight) - height[i]`, clamped at 0. Two pointers with running `leftMax` / `rightMax`: move whichever side has the smaller max, since that side's max is the binding constraint. Prefix/suffix max arrays give the same answer in O(n) space.
