pub struct Solution;

impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = nums.clone();
        ans.extend(ans.clone());
        ans
    }
}
