pub struct Solution;

impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        let mut idx = m + n - 1;
        let mut i1 = m - 1;
        let mut i2 = n - 1;

        while idx >= 0 {
            if i1 < 0 {
                nums1[idx as usize] = nums2[i2 as usize];
                i2 -= 1;
            } else if i2 < 0 {
                nums1[idx as usize] = nums1[i1 as usize];
                i1 -= 1;
            } else {
                if nums1[i1 as usize] < nums2[i2 as usize] {
                    nums1[idx as usize] = nums2[i2 as usize];
                    i2 -= 1;
                } else {
                    nums1[idx as usize] = nums1[i1 as usize];
                    i1 -= 1;
                }
            }
            idx -= 1;
        }
    }
}
