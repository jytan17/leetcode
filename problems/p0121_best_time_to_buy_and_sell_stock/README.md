# Problem 0121: Best Time to Buy and Sell Stock

Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

## Constraints

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

## Examples

- Input: `prices = [7,1,5,3,6,4]`
  Output: `5`  (buy day 2 at 1, sell day 5 at 6)

- Input: `prices = [7,6,4,3,1]`
  Output: `0`  (no profitable transaction)

## Target

- Time: O(n)
- Space: O(1)

## Notes

Single pass. Track running min price; at each step compute `price - min` and update best profit.
