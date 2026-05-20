use p0027_remove_element::Solution;

fn check(mut nums: Vec<i32>, val: i32, expected_k: i32, expected_remaining: &[i32]) {
    let k = Solution::remove_element(&mut nums, val);
    assert_eq!(k, expected_k, "k mismatch");
    let mut front: Vec<i32> = nums[..k as usize].to_vec();
    front.sort();
    let mut want: Vec<i32> = expected_remaining.to_vec();
    want.sort();
    assert_eq!(front, want, "first k elements mismatch (order-agnostic)");
}

#[test]
fn example_1() {
    check(vec![3, 2, 2, 3], 3, 2, &[2, 2]);
}

#[test]
fn example_2() {
    check(vec![0, 1, 2, 2, 3, 0, 4, 2], 2, 5, &[0, 1, 4, 0, 3]);
}

#[test]
fn empty_input() {
    check(vec![], 5, 0, &[]);
}

#[test]
fn all_match() {
    check(vec![4, 4, 4], 4, 0, &[]);
}

#[test]
fn none_match() {
    check(vec![1, 2, 3], 9, 3, &[1, 2, 3]);
}

#[test]
fn single_no_match() {
    check(vec![7], 3, 1, &[7]);
}

#[test]
fn single_match() {
    check(vec![3], 3, 0, &[]);
}

#[test]
fn match_at_end() {
    check(vec![1, 2, 3], 2, 2, &[1, 3]);
}
