# 210. Course Schedule II

- Link: https://leetcode.com/problems/course-schedule-ii/
- Difficulty: Medium
- Category: Graphs (NeetCode 150)

## Statement

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return **any** of them. If it is impossible to finish all courses, return **an empty array**.

## Examples

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3] (or [0,1,2,3])

Input: numCourses = 1, prerequisites = []
Output: [0]
```

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- `ai != bi`
- All pairs `[ai, bi]` are distinct.

## Target

- Time: O(V + E)
- Space: O(V + E)
