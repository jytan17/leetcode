pub struct Solution;

impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let mut c1 = word1.chars();
        let mut c2 = word2.chars();
        let mut ans = String::with_capacity(word1.len() + word2.len());

        loop {
            match (c1.next(), c2.next()) {
                (Some(a), Some(b)) => {
                    ans.push(a);
                    ans.push(b);
                }
                (Some(a), None) => {
                    ans.push(a);
                    ans.extend(c1);
                    break;
                }
                (None, Some(b)) => {
                    ans.push(b);
                    ans.extend(c2);
                    break;
                }
                (None, None) => break,
            }
        }
        ans
    }
}
