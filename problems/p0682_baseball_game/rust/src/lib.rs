pub struct Solution;

impl Solution {
    pub fn cal_points(operations: Vec<String>) -> i32 {
        let mut stack: Vec<i32> = Vec::new();

        for op in &operations {
            match op.as_str() {
                "C" => {
                    stack.pop().unwrap();
                }
                "D" => {
                    let last = *stack.last().unwrap();
                    stack.push(last * 2);
                }
                "+" => {
                    let n = stack.len();
                    stack.push(stack[n - 1] + stack[n - 2]);
                }
                _ => {
                    let n: i32 = op.parse().unwrap();
                    stack.push(n);
                }
            }
        }

        stack.iter().sum()
    }
}
