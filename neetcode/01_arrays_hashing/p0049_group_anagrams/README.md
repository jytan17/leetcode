# 49. Group Anagrams

- Link: https://leetcode.com/problems/group-anagrams/
- Difficulty: Medium
- Category: Arrays & Hashing (NeetCode 150)

## Statement

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

### Examples

- `strs = ["eat","tea","tan","ate","nat","bat"]` → `[["bat"],["nat","tan"],["ate","eat","tea"]]`
- `strs = [""]` → `[[""]]`
- `strs = ["a"]` → `[["a"]]`

## Constraints

- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- `strs[i]` consists of lowercase English letters.

## Target

- Time: O(n * k) where k = max string length
- Space: O(n * k)

## Notes

Hash map keyed by sorted string or char-count tuple. Group strings with same key.
