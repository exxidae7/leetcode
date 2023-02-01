use std::usize;

fn main() {
    let vec = vec![1, 2, 3, 4, 5, 6, 7, 8];
    let target: i32 = 2;
    println!("{:#?}", binary_search(&vec, target));
}

pub fn binary_search(arr: &Vec<i32>, target: i32) -> Option<i32> {
    let mut left: i32 = 0;
    let mut right: i32 = (arr.len() as i32) - 1;

    while left <= right {
        let mid = (left + right) / 2;
        let mid_index = mid as usize;
        let mid_val = &arr[mid_index];

        if mid_val == &target {
            return Some(mid_index as i32);
        }
        if mid_val < &target {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    None
}