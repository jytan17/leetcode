use p0169_majority_element::Solution;

#[test]
fn example_1() {
    assert_eq!(Solution::majority_element(vec![3, 2, 3]), 3);
}

#[test]
fn example_2() {
    assert_eq!(Solution::majority_element(vec![2, 2, 1, 1, 1, 2, 2]), 2);
}

#[test]
fn single_element() {
    assert_eq!(Solution::majority_element(vec![7]), 7);
}

#[test]
fn all_same() {
    assert_eq!(Solution::majority_element(vec![5, 5, 5, 5]), 5);
}

#[test]
fn two_elements() {
    assert_eq!(Solution::majority_element(vec![1, 1]), 1);
}

#[test]
fn negative_values() {
    assert_eq!(Solution::majority_element(vec![-1, -1, -1, 2, 3]), -1);
}

#[test]
fn majority_at_end() {
    assert_eq!(Solution::majority_element(vec![1, 2, 3, 3, 3, 3, 3]), 3);
}
