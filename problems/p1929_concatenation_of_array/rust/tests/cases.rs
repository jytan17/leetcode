use p1929_concatenation_of_array::Solution;

#[test]
fn example_1() {
    assert_eq!(
        Solution::get_concatenation(vec![1, 2, 1]),
        vec![1, 2, 1, 1, 2, 1]
    );
}

#[test]
fn example_2() {
    assert_eq!(
        Solution::get_concatenation(vec![1, 3, 2, 1]),
        vec![1, 3, 2, 1, 1, 3, 2, 1]
    );
}

#[test]
fn single_element() {
    assert_eq!(Solution::get_concatenation(vec![7]), vec![7, 7]);
}

#[test]
fn max_value() {
    assert_eq!(Solution::get_concatenation(vec![1000]), vec![1000, 1000]);
}

#[test]
fn all_same() {
    assert_eq!(
        Solution::get_concatenation(vec![5, 5, 5]),
        vec![5, 5, 5, 5, 5, 5]
    );
}
