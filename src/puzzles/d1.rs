use std::fs;

static INPUT_FILE:&str = "inputs/d1input.txt";

pub fn part1() -> i32{
    return sum_largest(to_sums(INPUT_FILE), 1);
}

pub fn part2() -> i32{
    return sum_largest(to_sums(INPUT_FILE), 3);
}

fn to_sums(file:&str) -> Vec<i32>{
    return fs::read_to_string(file).unwrap().split("\n\n").map(|x| x.split("\n").fold(0, |acc, y| acc + y.parse::<i32>().unwrap())).collect();
}

fn sum_largest(mut list:Vec<i32>, amount:usize) -> i32{
    list.sort_by(|a, b| b.cmp(a));
    let mut sum = 0;
    for i in &list[0..amount]{
        sum += i;
    }
    return sum;
}
