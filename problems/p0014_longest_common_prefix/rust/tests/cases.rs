use p0014_longest_common_prefix::Solution;

fn s(v: &[&str]) -> Vec<String> {
    v.iter().map(|x| x.to_string()).collect()
}

#[test]
fn example_1() {
    assert_eq!(
        Solution::longest_common_prefix(s(&["flower", "flow", "flight"])),
        "fl"
    );
}

#[test]
fn example_2_no_common() {
    assert_eq!(
        Solution::longest_common_prefix(s(&["dog", "racecar", "car"])),
        ""
    );
}

#[test]
fn single_string() {
    assert_eq!(Solution::longest_common_prefix(s(&["alone"])), "alone");
}

#[test]
fn empty_string_in_input() {
    assert_eq!(Solution::longest_common_prefix(s(&["", "abc"])), "");
}

#[test]
fn all_identical() {
    assert_eq!(
        Solution::longest_common_prefix(s(&["same", "same", "same"])),
        "same"
    );
}

#[test]
fn one_is_prefix_of_others() {
    assert_eq!(
        Solution::longest_common_prefix(s(&["ab", "abc", "abcd"])),
        "ab"
    );
}
