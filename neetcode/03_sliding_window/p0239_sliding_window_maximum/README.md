# 239. Sliding Window Maximum

- Link: https://leetcode.com/problems/sliding-window-maximum/
- Difficulty: Hard
- Category: Sliding Window (NeetCode 150)

## Statement

You are given an array of integers `nums` and a window of size `k` sliding from the very left of the array to the very right. You can only see the `k` numbers in the window; each time the window moves right by one position.

Return an array of the max value in each window.

### Examples

- `nums = [1,3,-1,-3,5,3,6,7], k = 3` → `[3,3,5,5,6,7]`
- `nums = [1], k = 1` → `[1]`

## Constraints

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length

## Target

- Time: O(n)
- Space: O(k)

## Notes

Monotonic decreasing deque holding *indices*. Before pushing `i`, pop from the back while `nums[back] <= nums[i]` — those can never be a max again. Pop from the front when it falls out of the window (`front <= i - k`). Front is the current max; start recording once `i >= k - 1`.
