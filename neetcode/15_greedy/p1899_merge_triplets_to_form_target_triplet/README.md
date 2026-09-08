# 1899. Merge Triplets to Form Target Triplet

- Link: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
- Difficulty: Medium
- Category: Greedy (NeetCode 150)

## Statement

A triplet is an array of three integers. You are given a 2D integer array `triplets`, where `triplets[i] = [ai, bi, ci]` describes the `i`th triplet. You are also given an integer array `target = [x, y, z]` that describes the triplet you want to obtain.

To obtain `target`, you may apply the following operation on `triplets` any number of times (possibly zero):

- Choose two indices (0-indexed) `i` and `j` (`i != j`) and update `triplets[j]` to become `[max(ai, aj), max(bi, bj), max(ci, cj)]`.

Return `true` if it is possible to obtain the `target` triplet `[x, y, z]` as an element of `triplets`, or `false` otherwise.

## Examples

```
Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true

Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
Output: false

Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
Output: true
```

## Constraints

- `1 <= triplets.length <= 10^5`
- `triplets[i].length == target.length == 3`
- `1 <= ai, bi, ci, x, y, z <= 1000`

## Target

- Time: O(n)
- Space: O(1)
