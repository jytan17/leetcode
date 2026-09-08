# 133. Clone Graph

- Link: https://leetcode.com/problems/clone-graph/
- Difficulty: Medium
- Category: Graphs (NeetCode 150)

## Statement

Given a reference of a node in a **connected** undirected graph, return a **deep copy** (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

```
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
```

The graph is represented in the test case using an adjacency list. Node values are unique and equal to the node's 1-indexed position.

## Examples

```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]

Input: adjList = [[]]
Output: [[]]

Input: adjList = []
Output: []
```

## Constraints

- The number of nodes in the graph is in the range `[0, 100]`.
- `1 <= Node.val <= 100`
- `Node.val` is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The graph is connected and all nodes can be visited starting from the given node.

## Target

- Time: O(V + E)
- Space: O(V)
