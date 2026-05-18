use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut hashmap: HashMap<String, Vec<String>> = HashMap::new();

        for s in &strs {
            let key = normalize(s);
            hashmap.entry(key).or_default().push(s.clone());
        }
        hashmap.into_values().collect()
    }
}

fn normalize(word: &str) -> String {
    let mut bytes: Vec<u8> = word.bytes().collect();
    bytes.sort();
    String::from_utf8(bytes).unwrap()
}
