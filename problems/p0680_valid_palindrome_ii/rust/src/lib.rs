pub struct Solution;

impl Solution {
    pub fn valid_palindrome(s: String) -> bool {
        let b = s.as_bytes();
        let (mut l, mut r) = (0usize, s.len().saturating_sub(1));

        while l < r {
            if b[r] != b[l] {
                return is_pali(b, l + 1, r) || is_pali(b, l, r - 1);
            }
            l += 1;
            r -= 1;
        }

        true
    }
}

fn is_pali(b: &[u8], mut l: usize, mut r: usize) -> bool {
    while l < r {
        if b[l] != b[r] {
            return false;
        }
        l += 1;
        r -= 1;
    }
    true
}
