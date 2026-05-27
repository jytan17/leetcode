use p1480_running_sum_of_1d_array::Solution;

#[test]
fn example_1() {
    assert_eq!(Solution::running_sum(vec![1, 2, 3, 4]), vec![1, 3, 6, 10]);
}

#[test]
fn example_2() {
    assert_eq!(Solution::running_sum(vec![1, 1, 1, 1, 1]), vec![1, 2, 3, 4, 5]);
}

#[test]
fn example_3() {
    assert_eq!(Solution::running_sum(vec![3, 1, 2, 10, 1]), vec![3, 4, 6, 16, 17]);
}

#[test]
fn single_element() {
    assert_eq!(Solution::running_sum(vec![5]), vec![5]);
}

#[test]
fn negatives() {
    assert_eq!(Solution::running_sum(vec![-1, -2, 3, -4]), vec![-1, -3, 0, -4]);
}
