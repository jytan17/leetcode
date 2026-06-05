pub struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut min_price = prices[0];

        for p in &prices[1..] {
            if p - min_price > ans {
                ans = p - min_price;
            }
            min_price = min_price.min(*p);
        }

        ans
    }
}
