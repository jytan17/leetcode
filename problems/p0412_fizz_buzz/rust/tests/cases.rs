use p0412_fizz_buzz::Solution;

fn s(v: &[&str]) -> Vec<String> {
    v.iter().map(|x| x.to_string()).collect()
}

#[test]
fn example_1() {
    assert_eq!(Solution::fizz_buzz(3), s(&["1", "2", "Fizz"]));
}

#[test]
fn example_2() {
    assert_eq!(Solution::fizz_buzz(5), s(&["1", "2", "Fizz", "4", "Buzz"]));
}

#[test]
fn example_3() {
    assert_eq!(
        Solution::fizz_buzz(15),
        s(&[
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz",
        ])
    );
}

#[test]
fn single() {
    assert_eq!(Solution::fizz_buzz(1), s(&["1"]));
}
