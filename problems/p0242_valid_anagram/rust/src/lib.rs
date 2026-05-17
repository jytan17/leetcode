pub struct Solution;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut counts = [0i32; 26];
        for b in s.bytes() {
            counts[(b - b'a') as usize] += 1;
        }

        for b in t.bytes() {
            counts[(b - b'a') as usize] -= 1;
        }
        counts.iter().all(|&c| c == 0)
    }
}
