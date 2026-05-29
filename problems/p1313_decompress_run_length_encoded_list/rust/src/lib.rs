pub struct Solution;

impl Solution {
    pub fn decompress_rl_elist(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = Vec::new();

        for pair in nums.chunks_exact(2) {
            let [freq, val] = [pair[0], pair[1]];
            ans.extend(std::iter::repeat_n(val, freq as usize));
        }

        ans
    }
}
