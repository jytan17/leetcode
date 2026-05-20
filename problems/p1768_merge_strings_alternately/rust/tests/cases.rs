use p1768_merge_strings_alternately::Solution;

fn check(w1: &str, w2: &str, expected: &str) {
    let got = Solution::merge_alternately(w1.to_string(), w2.to_string());
    assert_eq!(got, expected);
}

#[test]
fn example_1() {
    check("abc", "pqr", "apbqcr");
}

#[test]
fn example_2() {
    check("ab", "pqrs", "apbqrs");
}

#[test]
fn example_3() {
    check("abcd", "pq", "apbqcd");
}

#[test]
fn single_char_each() {
    check("a", "b", "ab");
}

#[test]
fn one_much_longer() {
    check("a", "bcdef", "abcdef");
}

#[test]
fn other_much_longer() {
    check("abcdef", "g", "agbcdef");
}
