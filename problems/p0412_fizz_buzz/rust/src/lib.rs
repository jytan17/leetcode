pub struct Solution;

impl Solution {
    pub fn fizz_buzz(n: i32) -> Vec<String> {
        let mut ans = vec![];

        for i in 1..=n {
            let mut val = String::new();
            if i % 3 == 0 {
                val.push_str("Fizz");
            }
            if i % 5 == 0 {
                val.push_str("Buzz");
            }

            if val.is_empty() {
                val.push_str(&i.to_string());
            }
            ans.push(val);
        }
        ans
    }
}
