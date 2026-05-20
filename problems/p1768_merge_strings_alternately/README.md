# Problem 1768: Merge Strings Alternately

Link: https://leetcode.com/problems/merge-strings-alternately/

## Statement

Given two strings `word1` and `word2`, merge them by adding letters in alternating order, starting with `word1`. If one string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

## Constraints

- `1 <= word1.length, word2.length <= 100`
- `word1` and `word2` consist of lowercase English letters.

## Examples

- Input: `word1 = "abc"`, `word2 = "pqr"`
  Output: `"apbqcr"`
- Input: `word1 = "ab"`, `word2 = "pqrs"`
  Output: `"apbqrs"`
- Input: `word1 = "abcd"`, `word2 = "pq"`
  Output: `"apbqcd"`

## Target

- Time: O(n + m)
- Space: O(n + m)

## Notes

Two pointers, alternate. After loop, append leftover tail of whichever is longer.
