pub struct Solution;

impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let ref_word = strs[0].as_bytes();
        let mut idx = 0;

        'outer: for i in 0..ref_word.len() {
            for word in strs.iter().skip(1) {
                let b = word.as_bytes();
                if i >= b.len() || b[i] != ref_word[i] {
                    break 'outer;
                }
            }
            idx += 1;
        }

        strs[0][..idx].to_string()
    }
}
