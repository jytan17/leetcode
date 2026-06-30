pub struct Solution;

impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.is_empty() {
            return String::new();
        }

        let first = strs[0].as_bytes();

        for i in 0..first.len() {
            for s in &strs[1..] {
                let b = s.as_bytes();
                if i >= b.len() || b[i] != first[i] {
                    return strs[0][..i].to_string();
                }
            }
        }

        strs[0].clone()
    }
}
