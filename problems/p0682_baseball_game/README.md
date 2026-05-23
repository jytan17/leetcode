# 682. Baseball Game

https://leetcode.com/problems/baseball-game/

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings `operations`, where `operations[i]` is the `i`th operation you must apply to the record and is one of the following:

- An integer `x` — record a new score of `x`.
- `"+"` — record a new score that is the sum of the previous two scores.
- `"D"` — record a new score that is double the previous score.
- `"C"` — invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

## Examples

- `ops = ["5","2","C","D","+"]` → `30`
  - "5" → [5]; "2" → [5,2]; "C" → [5]; "D" → [5,10]; "+" → [5,10,15]. Sum = 30.
- `ops = ["5","-2","4","C","D","9","+","+"]` → `27`
  - [5] → [5,-2] → [5,-2,4] → [5,-2] → [5,-2,-4] → [5,-2,-4,9] → [5,-2,-4,9,5] → [5,-2,-4,9,5,14]. Sum = 27.
- `ops = ["1","C"]` → `0`

## Constraints

- `1 <= operations.length <= 1000`
- `operations[i]` is `"C"`, `"D"`, `"+"`, or a string representing an integer in `[-3 * 10^4, 3 * 10^4]`.
- For `"+"`: at least two previous scores on record.
- For `"C"` and `"D"`: at least one previous score on record.

## Target

- Time: O(n)
- Space: O(n) — stack of scores
