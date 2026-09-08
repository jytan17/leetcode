# 853. Car Fleet

- Link: https://leetcode.com/problems/car-fleet/
- Difficulty: Medium
- Category: Stack (NeetCode 150)

## Statement

There are `n` cars at given miles away from the starting mile 0, heading toward a common destination at mile `target`.

You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting position of the `i`th car and `speed[i]` is the speed of the `i`th car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up and then travel at the same speed as the car ahead. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (they are assumed to be at the same position).

A **car fleet** is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it still counts as one car fleet.

Return the number of car fleets that will arrive at the destination.

## Examples

```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
- Cars at 10 and 8 become a fleet, meeting at 12.
- Car at 0 never catches up.
- Cars at 5 and 3 become a fleet, meeting at [6,9,...].
  Car at 5 arrives at 12 at time 7, car at 3 at time 3. But car at 3 catches car at 5 first.

Input: target = 10, position = [3], speed = [3]
Output: 1

Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
```

## Constraints

- `n == position.length == speed.length`
- `1 <= n <= 10^5`
- `0 < target <= 10^6`
- `0 <= position[i] < target`
- `0 < speed[i] <= 10^6`
- All values of `position` are unique.

## Target

- Time: O(n log n)
- Space: O(n)
