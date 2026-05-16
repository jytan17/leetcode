use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen: HashMap<i32, usize> = HashMap::new();
        for (i, &n) in nums.iter().enumerate() {
            let x = target - n;
            if let Some(&j) = seen.get(&x) {
                return vec![i as i32, j as i32];
            }
            seen.insert(n, i);
        }

        vec![]
    }
}
