use p0682_baseball_game::Solution;

fn ops(xs: &[&str]) -> Vec<String> {
    xs.iter().map(|s| s.to_string()).collect()
}

#[test]
fn example_1() {
    assert_eq!(Solution::cal_points(ops(&["5", "2", "C", "D", "+"])), 30);
}

#[test]
fn example_2() {
    assert_eq!(
        Solution::cal_points(ops(&["5", "-2", "4", "C", "D", "9", "+", "+"])),
        27
    );
}

#[test]
fn example_3_cancel_to_empty() {
    assert_eq!(Solution::cal_points(ops(&["1", "C"])), 0);
}

#[test]
fn single_score() {
    assert_eq!(Solution::cal_points(ops(&["7"])), 7);
}

#[test]
fn negative_scores() {
    assert_eq!(Solution::cal_points(ops(&["-5", "-3", "+"])), -16);
}

#[test]
fn double_then_plus() {
    assert_eq!(Solution::cal_points(ops(&["3", "D", "+"])), 18);
}

#[test]
fn multiple_cancels() {
    assert_eq!(Solution::cal_points(ops(&["1", "2", "3", "C", "C"])), 1);
}
