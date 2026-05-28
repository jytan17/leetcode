# Problem 412: Fizz Buzz

Link: https://leetcode.com/problems/fizz-buzz/

## Statement

Given integer `n`, return string array `answer` (1-indexed) where:
- `answer[i] == "FizzBuzz"` if `i` divisible by 3 and 5
- `answer[i] == "Fizz"` if `i` divisible by 3
- `answer[i] == "Buzz"` if `i` divisible by 5
- `answer[i] == i` (as string) otherwise

## Constraints

- 1 <= n <= 10^4

## Examples

- Input: `n = 3`
  Output: `["1","2","Fizz"]`
- Input: `n = 5`
  Output: `["1","2","Fizz","4","Buzz"]`
- Input: `n = 15`
  Output: `["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]`

## Target

- Time: O(n)
- Space: O(n)

## Notes

LeetCode sig: `pub fn fizz_buzz(n: i32) -> Vec<String>`. Practice: `String::from`, `i32::to_string()`, `match` on `(i % 3, i % 5)`.
