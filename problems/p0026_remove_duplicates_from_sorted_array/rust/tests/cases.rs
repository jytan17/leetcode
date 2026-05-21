use p0026_remove_duplicates_from_sorted_array::Solution;

fn run(mut nums: Vec<i32>, expected_k: i32, expected_prefix: &[i32]) {
    let k = Solution::remove_duplicates(&mut nums);
    assert_eq!(k, expected_k);
    assert_eq!(&nums[..k as usize], expected_prefix);
}

#[test]
fn example_1() {
    run(vec![1, 1, 2], 2, &[1, 2]);
}

#[test]
fn example_2() {
    run(vec![0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, &[0, 1, 2, 3, 4]);
}

#[test]
fn single_element() {
    run(vec![1], 1, &[1]);
}

#[test]
fn all_same() {
    run(vec![2, 2, 2, 2], 1, &[2]);
}

#[test]
fn all_unique() {
    run(vec![1, 2, 3, 4, 5], 5, &[1, 2, 3, 4, 5]);
}

#[test]
fn negatives() {
    run(vec![-3, -3, -1, 0, 0, 2], 4, &[-3, -1, 0, 2]);
}

#[test]
fn two_same() {
    run(vec![5, 5], 1, &[5]);
}
