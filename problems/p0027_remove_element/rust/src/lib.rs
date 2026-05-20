pub struct Solution;

impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut slow = 0;
        let mut fast = 0;

        while fast < nums.len() {
            if nums[fast] != val {
                nums.swap(slow, fast);
                slow += 1;
            }
            fast += 1;
        }
        slow as i32
    }
}
