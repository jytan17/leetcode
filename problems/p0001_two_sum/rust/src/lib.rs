use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut hash_map: HashMap<i32, i32> = HashMap::new();

        for (idx, n) in nums.iter().enumerate() {
            let x = target - n;
            if let Some(&j) = hash_map.get(&x) {
                return vec![j, idx as i32];
            }
            hash_map.insert(*n, idx as i32);
        }
        vec![]
    }
}
