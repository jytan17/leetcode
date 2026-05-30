use p1929_concatenation_of_array::Solution;

#[test]
fn example_1() {
    assert_eq!(Solution::get_concatenation(vec![1, 2, 1]), vec![1, 2, 1, 1, 2, 1]);
}

#[test]
fn example_2() {
    assert_eq!(
        Solution::get_concatenation(vec![1, 3, 2, 1]),
        vec![1, 3, 2, 1, 1, 3, 2, 1]
    );
}

#[test]
fn single() {
    assert_eq!(Solution::get_concatenation(vec![7]), vec![7, 7]);
}
