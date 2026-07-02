use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut hash_map: HashMap<String, Vec<String>> = HashMap::new();

        for s in &strs {
            hash_map.entry(normalize(s)).or_default().push(s.clone())
        }

        hash_map.into_values().collect()
    }
}

fn normalize(s: &str) -> String {
    let mut chars: Vec<char> = s.chars().collect();
    chars.sort_unstable();
    chars.into_iter().collect()
}
