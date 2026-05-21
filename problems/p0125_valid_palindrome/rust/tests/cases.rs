use p0125_valid_palindrome::Solution;

#[test]
fn example_1() {
    assert!(Solution::is_palindrome("A man, a plan, a canal: Panama".to_string()));
}

#[test]
fn example_2() {
    assert!(!Solution::is_palindrome("race a car".to_string()));
}

#[test]
fn only_space() {
    assert!(Solution::is_palindrome(" ".to_string()));
}

#[test]
fn single_char() {
    assert!(Solution::is_palindrome("a".to_string()));
}

#[test]
fn only_non_alnum() {
    assert!(Solution::is_palindrome(".,!".to_string()));
}

#[test]
fn digit_letter_mix_not_palindrome() {
    assert!(!Solution::is_palindrome("0P".to_string()));
}

#[test]
fn digits_palindrome() {
    assert!(Solution::is_palindrome("12321".to_string()));
}
