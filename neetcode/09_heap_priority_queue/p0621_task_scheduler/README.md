# 621. Task Scheduler

- Link: https://leetcode.com/problems/task-scheduler/
- Difficulty: Medium
- Category: Heap / Priority Queue (NeetCode 150)

## Statement

You are given an array of CPU tasks, each represented by letters A to Z, and a cooling interval `n`. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least `n` intervals due to cooling time.

Return the minimum number of intervals the CPU will take to finish all the given tasks.

## Examples

```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8

Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6

Input: tasks = ["A","A","A","B","B","B"], n = 3
Output: 10
```

## Constraints

- `1 <= tasks.length <= 10^4`
- `tasks[i]` is an uppercase English letter.
- `0 <= n <= 100`

## Target

- Time: O(n * m) where m is number of unique tasks
- Space: O(m)
