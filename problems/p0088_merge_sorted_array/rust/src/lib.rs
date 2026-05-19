pub struct Solution;

impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        let mut i = m - 1;
        let mut j = n - 1;
        let mut k = m + n - 1;

        while 0 <= k && 0 <= j {
            let n1 = if 0 <= i { nums1[i as usize] } else { i32::MIN };
            let n2 = if 0 <= j { nums2[j as usize] } else { i32::MIN };

            if n1 < n2 {
                nums1[k as usize] = n2;
                j -= 1;
            } else {
                nums1[k as usize] = n1;
                i -= 1;
            }
            k -= 1;
        }
    }
}
