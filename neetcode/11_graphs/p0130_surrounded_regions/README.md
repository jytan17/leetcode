# 130. Surrounded Regions

- Link: https://leetcode.com/problems/surrounded-regions/
- Difficulty: Medium
- Category: Graphs (NeetCode 150)

## Statement

You are given an `m x n` matrix `board` containing letters `'X'` and `'O'`. Capture all regions that are **4-directionally surrounded** by `'X'`.

A region is **captured** by flipping all `'O'`s into `'X'`s in that surrounded region.

An `'O'` is **not surrounded** if it is on the border or connected to an `'O'` on the border (4-directionally).

## Examples

```
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Input: board = [["X"]]
Output: [["X"]]
```

## Constraints

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is `'X'` or `'O'`

## Target

- Time: O(m * n)
- Space: O(m * n)
