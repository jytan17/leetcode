pub struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut ans = 0i32;
        let mut min_p = prices[0];

        for &p in prices.iter().skip(1) {
            ans = ans.max(p - min_p);
            min_p = min_p.min(p);
        }

        ans
    }
}
