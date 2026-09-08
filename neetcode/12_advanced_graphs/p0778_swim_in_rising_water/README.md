# 778. Swim in Rising Water

- Link: https://leetcode.com/problems/swim-in-rising-water/
- Difficulty: Hard
- Category: Advanced Graphs (NeetCode 150)

## Statement

You are given an `n x n` integer matrix `grid` where each value `grid[i][j]` represents the elevation at that point `(i, j)`.

The rain starts to fall. At time `t`, the depth of the water everywhere is `t`. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares is at most `t`.

You start at the top-left square `(0, 0)`. Find the least time until you can reach the bottom-right square `(n - 1, n - 1)`.

The values in `grid` are a permutation of `[0, 1, ..., n*n - 1]`.

## Examples

```
Input: grid = [[0,2],[1,3]]
Output: 3

Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
```

## Constraints

- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 50`
- `0 <= grid[i][j] < n²`
- Each value in `grid` is unique.
- `grid[0][0] == 0` (this is guaranteed since values are a permutation)

## Target

- Time: O(N² log N) with Dijkstra's / binary search
- Space: O(N²)
