use p0088_merge_sorted_array::Solution;

fn check(mut nums1: Vec<i32>, m: i32, mut nums2: Vec<i32>, n: i32, expected: Vec<i32>) {
    Solution::merge(&mut nums1, m, &mut nums2, n);
    assert_eq!(nums1, expected);
}

#[test]
fn example_1() {
    check(vec![1, 2, 3, 0, 0, 0], 3, vec![2, 5, 6], 3, vec![1, 2, 2, 3, 5, 6]);
}

#[test]
fn example_2_nums2_empty() {
    check(vec![1], 1, vec![], 0, vec![1]);
}

#[test]
fn example_3_nums1_empty() {
    check(vec![0], 0, vec![1], 1, vec![1]);
}

#[test]
fn all_nums2_smaller() {
    check(vec![4, 5, 6, 0, 0, 0], 3, vec![1, 2, 3], 3, vec![1, 2, 3, 4, 5, 6]);
}

#[test]
fn all_nums2_larger() {
    check(vec![1, 2, 3, 0, 0, 0], 3, vec![4, 5, 6], 3, vec![1, 2, 3, 4, 5, 6]);
}

#[test]
fn with_negatives() {
    check(vec![-5, 0, 3, 0, 0], 3, vec![-3, 2], 2, vec![-5, -3, 0, 2, 3]);
}

#[test]
fn duplicates() {
    check(vec![1, 1, 1, 0, 0, 0], 3, vec![1, 1, 1], 3, vec![1, 1, 1, 1, 1, 1]);
}
