# 271. Encode and Decode Strings

- Link: https://leetcode.com/problems/encode-and-decode-strings/
- Difficulty: Medium
- Category: Arrays & Hashing (NeetCode 150)

## Statement

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Implement `encode` and `decode` methods.

### Examples

- `["lint","code","love","you"]` → encode → decode → `["lint","code","love","you"]`
- `["we","say",":","yes"]` → encode → decode → `["we","say",":","yes"]`

## Constraints

- 0 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- `strs[i]` contains any possible characters including unicode.

## Target

- Time: O(n) where n = total chars across all strings
- Space: O(1) extra beyond output

## Notes

Length-prefix encoding: `len(s) + "#" + s` for each string. On decode, read length, skip `#`, grab that many chars. Handles any character including `#` and digits.
