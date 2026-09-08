# 286. Walls and Gates

- Link: https://leetcode.com/problems/walls-and-gates/
- Difficulty: Medium
- Category: Graphs (NeetCode 150)

## Statement

You are given an `m x n` grid `rooms` initialized with these three possible values:

- `-1` — A wall or an obstacle.
- `0` — A gate.
- `INF` — Infinity means an empty room. We use the value `2^31 - 1 = 2147483647` to represent INF.

Fill each empty room with the distance to its **nearest gate**. If it is impossible to reach a gate, leave it as `INF`.

Distance is measured in steps (4-directional).

## Examples

```
Input: rooms = [
  [INF, -1,  0, INF],
  [INF,INF,INF,  -1],
  [INF, -1,INF,  -1],
  [  0, -1,INF, INF]
]
Output: [
  [3, -1, 0, 1],
  [2,  2, 1,-1],
  [1, -1, 2,-1],
  [0, -1, 3, 4]
]

Input: rooms = [[-1]]
Output: [[-1]]
```

## Constraints

- `m == rooms.length`
- `n == rooms[i].length`
- `1 <= m, n <= 250`
- `rooms[i][j]` is `-1`, `0`, or `2^31 - 1`

## Target

- Time: O(m * n)
- Space: O(m * n)
