# 226. Invert Binary Tree

- Link: https://leetcode.com/problems/invert-binary-tree/
- Difficulty: Easy
- Category: Trees (NeetCode 150)

## Statement

Given the `root` of a binary tree, invert the tree, and return its root.

Inverting a binary tree means swapping every left and right child node.

## Examples

```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input: root = [2,1,3]
Output: [2,3,1]

Input: root = []
Output: []
```

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Target

- Time: O(n)
- Space: O(n) — recursion stack / queue
