use p0217_contains_duplicate::Solution;

#[test]
fn example_1() {
    assert_eq!(Solution::contains_duplicate(vec![1, 2, 3, 1]), true);
}

#[test]
fn example_2() {
    assert_eq!(Solution::contains_duplicate(vec![1, 2, 3, 4]), false);
}

#[test]
fn example_3() {
    assert_eq!(
        Solution::contains_duplicate(vec![1, 1, 1, 3, 3, 4, 3, 2, 4, 2]),
        true
    );
}

#[test]
fn single_element() {
    assert_eq!(Solution::contains_duplicate(vec![1]), false);
}

#[test]
fn negatives_with_dup() {
    assert_eq!(Solution::contains_duplicate(vec![-1, -2, -3, -1]), true);
}

#[test]
fn bounds() {
    assert_eq!(
        Solution::contains_duplicate(vec![1_000_000_000, -1_000_000_000, 1_000_000_000]),
        true
    );
}
