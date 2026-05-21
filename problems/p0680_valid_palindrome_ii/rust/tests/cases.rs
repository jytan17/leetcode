use p0680_valid_palindrome_ii::Solution;

#[test]
fn example_1() {
    assert!(Solution::valid_palindrome("aba".to_string()));
}

#[test]
fn example_2() {
    assert!(Solution::valid_palindrome("abca".to_string()));
}

#[test]
fn example_3() {
    assert!(!Solution::valid_palindrome("abc".to_string()));
}

#[test]
fn single_char() {
    assert!(Solution::valid_palindrome("a".to_string()));
}

#[test]
fn two_chars_diff() {
    assert!(Solution::valid_palindrome("ab".to_string()));
}

#[test]
fn already_palindrome_even() {
    assert!(Solution::valid_palindrome("abba".to_string()));
}

#[test]
fn delete_left_side() {
    assert!(Solution::valid_palindrome("deeee".to_string()));
}

#[test]
fn two_mismatches() {
    assert!(!Solution::valid_palindrome("abcdef".to_string()));
}

#[test]
fn near_palindrome_inner() {
    assert!(Solution::valid_palindrome("eeccccbebaeeabebccceea".to_string()) == false);
}
