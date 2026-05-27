pub struct Solution;

impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = Vec::new();
        let mut running_sum = 0_i32;

        for n in &nums {
            running_sum += n;
            ans.push(running_sum);
        }

        ans
    }
}
