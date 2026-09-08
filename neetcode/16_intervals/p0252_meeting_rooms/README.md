# 252. Meeting Rooms

- Link: https://leetcode.com/problems/meeting-rooms/
- Difficulty: Easy
- Category: Intervals (NeetCode 150)

## Statement

Given an array of meeting time intervals `intervals` where `intervals[i] = [starti, endi]`, determine if a person could attend all meetings.

## Examples

```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Input: intervals = [[7,10],[2,4]]
Output: true
```

## Constraints

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= starti < endi <= 10^6`

## Target

- Time: O(n log n)
- Space: O(1)
