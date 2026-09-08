# 152. Maximum Product Subarray

- Link: https://leetcode.com/problems/maximum-product-subarray/
- Difficulty: Medium
- Category: 1-D Dynamic Programming (NeetCode 150)

## Statement

Given an integer array `nums`, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

## Examples

```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
- The product of any subarray of `nums` is guaranteed to fit in a 32-bit integer.

## Target

- Time: O(n)
- Space: O(1)
