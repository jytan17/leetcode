use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut hash_map: HashMap<i32, i32> = HashMap::new();
        let mut ans = nums[0];
        let mut cnt = 0i32;

        for n in nums {
            *hash_map.entry(n).or_insert(0) += 1;
            if hash_map.get(&n).unwrap() > &cnt {
                ans = n;
                cnt = *hash_map.get(&n).unwrap();
            }
        }
        ans
    }
}
