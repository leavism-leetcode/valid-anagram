use std::collections::HashMap;

pub struct Solution {}

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut s_map: HashMap<char, i32> = HashMap::new();

        for character in s.chars() {
            let count = s_map.entry(character).or_insert(0);

            *count += 1;
        }

        for character in t.chars() {
            let count = s_map.entry(character).or_insert(0);
            *count -= 1;
        }

        for value in s_map.values() {
            if *value != 0 {
                return false;
            }
        }

        return true;
    }
}
