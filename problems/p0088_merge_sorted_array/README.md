# Problem 0088: Merge Sorted Array

Link: https://leetcode.com/problems/merge-sorted-array/

## Statement

Two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m`, `n` representing number of valid elements in each.

Merge `nums1` and `nums2` into a single sorted array. Merge stored **inside `nums1`** — `nums1.len() == m + n`. First `m` slots are real data, last `n` slots are 0 placeholders. `nums2.len() == n`.

## Constraints

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

## Examples

- Input: `nums1 = [1,2,3,0,0,0]`, `m = 3`, `nums2 = [2,5,6]`, `n = 3`
  Output: `nums1 = [1,2,2,3,5,6]`
- Input: `nums1 = [1]`, `m = 1`, `nums2 = []`, `n = 0`
  Output: `nums1 = [1]`
- Input: `nums1 = [0]`, `m = 0`, `nums2 = [1]`, `n = 1`
  Output: `nums1 = [1]`

## Target

- Time: O(m + n)
- Space: O(1)

## Notes

- Fill from the back. Three pointers: `i = m-1` (nums1 real), `j = n-1` (nums2), `k = m+n-1` (write).
- Pick larger of `nums1[i]`, `nums2[j]`, place at `nums1[k]`.
- When `i < 0`, drain remaining `nums2`. (When `j < 0`, nums1 already in place.)
