use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut hash_map: HashMap<i32, u32> = HashMap::new();
        let mut ans = nums[0];
        let mut best = 0u32;

        for &n in &nums {
            let c = hash_map.entry(n).or_insert(0);
            *c += 1;

            if *c > best {
                best = *c;
                ans = n;
            }
        }

        ans
    }
}
