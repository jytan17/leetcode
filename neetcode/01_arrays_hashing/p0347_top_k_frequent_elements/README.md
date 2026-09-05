# 347. Top K Frequent Elements

- Link: https://leetcode.com/problems/top-k-frequent-elements/
- Difficulty: Medium
- Category: Arrays & Hashing (NeetCode 150)

## Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

### Examples

- `nums = [1,1,1,2,2,3], k = 2` → `[1,2]`
- `nums = [1], k = 1` → `[1]`

## Constraints

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- `k` is in range [1, number of unique elements].
- Answer is guaranteed to be unique.

## Target

- Time: O(n)
- Space: O(n)

## Notes

Bucket sort: index = frequency, value = list of nums with that frequency. Avoids O(n log n) sort.
