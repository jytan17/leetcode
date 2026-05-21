pub struct Solution;

impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let b = s.as_bytes();
        let (mut l, mut r) = (0usize, b.len().wrapping_sub(1));

        while l < r && r < b.len() {
            if !b[l].is_ascii_alphanumeric() {
                l += 1;
                continue;
            }
            if !b[r].is_ascii_alphanumeric() {
                r -= 1;
                continue;
            }
            if !b[l].eq_ignore_ascii_case(&b[r]) {
                return false;
            }
            l += 1;
            r -= 1;
        }

        true
    }
}
