# 121. Best Time to Buy and Sell Stock

- Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- Difficulty: Easy
- Category: Sliding Window (NeetCode 150)

## Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell it. Return the maximum profit you can achieve. If no profit is possible, return `0`.

### Examples

- `prices = [7,1,5,3,6,4]` → `5` (buy day 2 at 1, sell day 5 at 6)
- `prices = [7,6,4,3,1]` → `0` (prices only fall, no transaction)

## Constraints

- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

## Target

- Time: O(n)
- Space: O(1)

## Notes

Track the running minimum price seen so far; at each day the candidate profit is `price - minSoFar`. Keep the max. Buy must come strictly before sell, so update the min after taking the profit.
