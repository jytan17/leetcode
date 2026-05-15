use p0001_two_sum::Solution;

fn check(nums: Vec<i32>, target: i32, expected: Vec<i32>) {
    let mut got = Solution::two_sum(nums, target);
    let mut want = expected;
    got.sort();
    want.sort();
    assert_eq!(got, want);
}

#[test]
fn example_1() {
    check(vec![2, 7, 11, 15], 9, vec![0, 1]);
}

#[test]
fn example_2() {
    check(vec![3, 2, 4], 6, vec![1, 2]);
}

#[test]
fn example_3() {
    check(vec![3, 3], 6, vec![0, 1]);
}

#[test]
fn all_negative() {
    check(vec![-1, -2, -3, -4, -5], -8, vec![2, 4]);
}

#[test]
fn zeros_and_dupes() {
    check(vec![0, 4, 3, 0], 0, vec![0, 3]);
}

#[test]
fn constraint_bounds() {
    check(vec![1_000_000_000, -1_000_000_000], 0, vec![0, 1]);
}
