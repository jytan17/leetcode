# 36. Valid Sudoku

- Link: https://leetcode.com/problems/valid-sudoku/
- Difficulty: Medium
- Category: Arrays & Hashing (NeetCode 150)

## Statement

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition.

A Sudoku board (partially filled) could be valid but is not necessarily solvable. Only filled cells need to be validated.

### Examples

- Valid board: standard example with no duplicates in rows/cols/boxes → `true`
- Invalid board: two 8s in first column → `false`

## Constraints

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `1-9` or `'.'`.

## Target

- Time: O(81) = O(1)
- Space: O(81) = O(1)

## Notes

Three sets (or one dict of sets): track seen digits per row, per col, per box. Box index = `(r // 3, c // 3)`.
