# Problem 0049: Group Anagrams

Link: https://leetcode.com/problems/group-anagrams/

## Statement

Given array of strings `strs`, group the anagrams together. Return groups in any order.

Anagram = rearrangement of another word's letters using all original letters exactly once.

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Examples

- Input: `strs = ["eat","tea","tan","ate","nat","bat"]`
  Output: `[["bat"],["nat","tan"],["ate","eat","tea"]]`
- Input: `strs = [""]`
  Output: `[[""]]`
- Input: `strs = ["a"]`
  Output: `[["a"]]`

## Target

- Time: O(N * K log K) where N = strs.length, K = max word length
- Space: O(N * K)

## Notes

- Key by sorted chars → group with HashMap<String, Vec<String>>.
- Alt key: 26-int char count tuple → O(N * K) but more code.
- Output order doesn't matter, but groups must be complete.
