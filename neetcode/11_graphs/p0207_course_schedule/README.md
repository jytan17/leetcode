# 207. Course Schedule

- Link: https://leetcode.com/problems/course-schedule/
- Difficulty: Medium
- Category: Graphs (NeetCode 150)

## Statement

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

Return `true` if you can finish all courses. Otherwise, return `false`.

## Examples

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: Take course 0 then course 1.

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: Cycle exists.
```

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- All prerequisite pairs are unique.

## Target

- Time: O(V + E)
- Space: O(V + E)
