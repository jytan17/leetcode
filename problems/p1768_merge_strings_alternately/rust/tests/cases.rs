use p1768_merge_strings_alternately::Solution;

fn run(w1: &str, w2: &str) -> String {
    Solution::merge_alternately(w1.to_string(), w2.to_string())
}

#[test]
fn example_1_equal_length() {
    assert_eq!(run("abc", "pqr"), "apbqcr");
}

#[test]
fn example_2_word2_longer() {
    assert_eq!(run("ab", "pqrs"), "apbqrs");
}

#[test]
fn example_3_word1_longer() {
    assert_eq!(run("abcd", "pq"), "apbqcd");
}

#[test]
fn single_chars() {
    assert_eq!(run("a", "b"), "ab");
}

#[test]
fn word1_much_longer() {
    assert_eq!(run("abcde", "x"), "axbcde");
}

#[test]
fn word2_much_longer() {
    assert_eq!(run("x", "abcde"), "xabcde");
}
