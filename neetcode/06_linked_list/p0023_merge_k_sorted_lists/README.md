# 23. Merge k Sorted Lists

- Link: https://leetcode.com/problems/merge-k-sorted-lists/
- Difficulty: Hard
- Category: Linked List (NeetCode 150)

## Statement

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

## Examples

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Input: lists = []
Output: []

Input: lists = [[]]
Output: []
```

## Constraints

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` is sorted in ascending order.
- The sum of `lists[i].length` will not exceed `10^4`.

## Target

- Time: O(N log k) where N is total number of nodes
- Space: O(k) for the heap (or O(1) with divide-and-conquer merge)
