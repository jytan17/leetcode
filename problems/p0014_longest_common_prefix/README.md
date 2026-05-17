# Problem 0014: Longest Common Prefix

Link: https://leetcode.com/problems/longest-common-prefix/

## Statement

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

## Constraints

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters if it is non-empty.

## Examples

- Input: `strs = ["flower","flow","flight"]`
  Output: `"fl"`
- Input: `strs = ["dog","racecar","car"]`
  Output: `""` (no common prefix)

## Target

- Time: O(S) where S = sum of all chars
- Space: O(1) extra

## Notes

- Vertical scan: compare char at index i across all strings.
- Or horizontal: shrink prefix against each string.
