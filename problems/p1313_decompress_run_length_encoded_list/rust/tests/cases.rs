use p1313_decompress_run_length_encoded_list::Solution;

#[test]
fn example_1() {
    assert_eq!(Solution::decompress_rl_elist(vec![1, 2, 3, 4]), vec![2, 4, 4, 4]);
}

#[test]
fn example_2() {
    assert_eq!(Solution::decompress_rl_elist(vec![1, 1, 2, 3]), vec![1, 3, 3]);
}

#[test]
fn single_pair() {
    assert_eq!(Solution::decompress_rl_elist(vec![3, 7]), vec![7, 7, 7]);
}

#[test]
fn freq_one_each() {
    assert_eq!(Solution::decompress_rl_elist(vec![1, 5, 1, 9, 1, 2]), vec![5, 9, 2]);
}
