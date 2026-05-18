pub struct Solution;

impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        if nums.is_empty() {
            return 0;
        }

        let mut left: i32 = 0;
        let mut right: i32 = nums.len() as i32 - 1;

        while left <= right {
            if nums[left as usize] == val {
                nums[left as usize] = nums[right as usize];
                right -= 1;
            } else {
                left += 1;
            }
        }
        left
    }
}
