use p0049_group_anagrams::Solution;

fn s(v: &[&str]) -> Vec<String> {
    v.iter().map(|x| x.to_string()).collect()
}

fn normalize(mut groups: Vec<Vec<String>>) -> Vec<Vec<String>> {
    for g in groups.iter_mut() {
        g.sort();
    }
    groups.sort();
    groups
}

fn check(input: Vec<String>, expected: Vec<Vec<String>>) {
    let got = normalize(Solution::group_anagrams(input));
    let want = normalize(expected);
    assert_eq!(got, want);
}

#[test]
fn example_1() {
    check(
        s(&["eat", "tea", "tan", "ate", "nat", "bat"]),
        vec![s(&["bat"]), s(&["nat", "tan"]), s(&["ate", "eat", "tea"])],
    );
}

#[test]
fn example_2_empty_string() {
    check(s(&[""]), vec![s(&[""])]);
}

#[test]
fn example_3_single() {
    check(s(&["a"]), vec![s(&["a"])]);
}

#[test]
fn all_distinct() {
    check(
        s(&["abc", "def", "ghi"]),
        vec![s(&["abc"]), s(&["def"]), s(&["ghi"])],
    );
}

#[test]
fn all_same_anagram() {
    check(
        s(&["abc", "bca", "cab", "acb"]),
        vec![s(&["abc", "bca", "cab", "acb"])],
    );
}

#[test]
fn mixed_lengths() {
    check(
        s(&["a", "aa", "aaa", "aa"]),
        vec![s(&["a"]), s(&["aa", "aa"]), s(&["aaa"])],
    );
}
