use p0121_best_time_to_buy_and_sell_stock::Solution;

#[test]
fn example_1() {
    assert_eq!(Solution::max_profit(vec![7, 1, 5, 3, 6, 4]), 5);
}

#[test]
fn example_2_no_profit() {
    assert_eq!(Solution::max_profit(vec![7, 6, 4, 3, 1]), 0);
}

#[test]
fn single_day() {
    assert_eq!(Solution::max_profit(vec![5]), 0);
}

#[test]
fn two_days_profit() {
    assert_eq!(Solution::max_profit(vec![1, 2]), 1);
}

#[test]
fn two_days_loss() {
    assert_eq!(Solution::max_profit(vec![2, 1]), 0);
}

#[test]
fn all_equal() {
    assert_eq!(Solution::max_profit(vec![3, 3, 3, 3]), 0);
}

#[test]
fn max_at_end() {
    assert_eq!(Solution::max_profit(vec![2, 4, 1, 10]), 9);
}
