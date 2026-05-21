pub struct Solution;

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        if nums.is_empty() {
            return 0;
        }
        let mut slow = 1usize;

        for fast in 1..nums.len() {
            if nums[fast] != nums[slow - 1] {
                nums[slow] = nums[fast];
                slow += 1;
            }
        }
        slow as i32
    }
}
