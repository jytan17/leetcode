pub struct Solution;

impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let mut ans = String::new();
        let mut it1 = word1.chars();
        let mut it2 = word2.chars();

        loop {
            match (it1.next(), it2.next()) {
                (None, None) => break,
                (a, b) => {
                    if let Some(c) = a {
                        ans.push(c);
                    }
                    if let Some(c) = b {
                        ans.push(c);
                    }
                }
            }
        }
        ans
    }
}
