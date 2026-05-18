use p0344_reverse_string::Solution;

fn check(input: &[char], expected: &[char]) {
    let mut v = input.to_vec();
    Solution::reverse_string(&mut v);
    assert_eq!(v, expected);
}

#[test]
fn example_1() {
    check(&['h', 'e', 'l', 'l', 'o'], &['o', 'l', 'l', 'e', 'h']);
}

#[test]
fn example_2() {
    check(
        &['H', 'a', 'n', 'n', 'a', 'h'],
        &['h', 'a', 'n', 'n', 'a', 'H'],
    );
}

#[test]
fn single_char() {
    check(&['a'], &['a']);
}

#[test]
fn two_chars() {
    check(&['a', 'b'], &['b', 'a']);
}

#[test]
fn palindrome() {
    check(&['r', 'a', 'c', 'e', 'c', 'a', 'r'], &['r', 'a', 'c', 'e', 'c', 'a', 'r']);
}
