# 1046. Last Stone Weight

- Link: https://leetcode.com/problems/last-stone-weight/
- Difficulty: Easy
- Category: Heap / Priority Queue (NeetCode 150)

## Statement

You are given an array of integers `stones` where `stones[i]` is the weight of the `i`th stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:

- If `x == y`, both stones are destroyed, and
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return `0`.

## Examples

```
Input: stones = [2,7,4,1,8,1]
Output: 1

Input: stones = [1]
Output: 1
```

## Constraints

- `1 <= stones.length <= 30`
- `1 <= stones[i] <= 1000`

## Target

- Time: O(n log n)
- Space: O(n)
