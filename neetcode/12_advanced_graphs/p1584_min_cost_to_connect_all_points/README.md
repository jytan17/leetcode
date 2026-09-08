# 1584. Min Cost to Connect All Points

- Link: https://leetcode.com/problems/min-cost-to-connect-all-points/
- Difficulty: Medium
- Category: Advanced Graphs (NeetCode 150)

## Statement

You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.

The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the **Manhattan distance** between them: `|xi - xj| + |yi - yj|`.

Return the minimum cost to make all points connected. All points are connected if there is **exactly one** simple path between any two points.

## Examples

```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

## Constraints

- `1 <= points.length <= 1000`
- `-10^6 <= xi, yi <= 10^6`
- All pairs `(xi, yi)` are distinct.

## Target

- Time: O(N² log N) Kruskal's or O(N²) Prim's
- Space: O(N²)
