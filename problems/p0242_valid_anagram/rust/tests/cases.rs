use p0242_valid_anagram::Solution;

fn s(x: &str) -> String {
    x.to_string()
}

#[test]
fn example_1() {
    assert_eq!(Solution::is_anagram(s("anagram"), s("nagaram")), true);
}

#[test]
fn example_2() {
    assert_eq!(Solution::is_anagram(s("rat"), s("car")), false);
}

#[test]
fn different_lengths() {
    assert_eq!(Solution::is_anagram(s("ab"), s("abc")), false);
}

#[test]
fn single_char_equal() {
    assert_eq!(Solution::is_anagram(s("a"), s("a")), true);
}

#[test]
fn single_char_diff() {
    assert_eq!(Solution::is_anagram(s("a"), s("b")), false);
}

#[test]
fn same_letters_diff_counts() {
    assert_eq!(Solution::is_anagram(s("aacc"), s("ccac")), false);
}
