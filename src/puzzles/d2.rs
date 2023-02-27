use std::fs;
#[path = "../functions/arithmetic.rs"] mod arithmetic;

static INPUT_FILE:&str = "inputs/d2input.txt";

pub fn part1() -> i32{
    let mut sum = 0;
    let rounds = fs::read_to_string(INPUT_FILE).unwrap();
    for round in rounds.split("\n") {
        let (opponent, yours) = parse_input(round); 
        sum += score(yours, outcome_given_yours(opponent, yours));
    }
    sum
}

pub fn part2() -> i32{
    let mut sum = 0;
    let rounds = fs::read_to_string(INPUT_FILE).unwrap();
    for round in rounds.split("\n") {
        let (opponent, outcome) = parse_input(round); 
        sum += score(yours_given_outcome(opponent, outcome), outcome);
    }
    sum
}

fn outcome_given_yours(opponent:i32, yours:i32) -> i32{
    arithmetic::modulo(yours-opponent+1, 3)
}

fn yours_given_outcome(opponent:i32,outcome:i32) -> i32{
    arithmetic::modulo(opponent+outcome-1, 3)
}

fn score(yours:i32, outcome:i32) -> i32{
    3*outcome + yours + 1
}

fn parse_input(line:&str) -> (i32, i32) {
    let mut inputs = line.chars();
    let first = inputs.next().unwrap();
    inputs.next();
    let second = inputs.next().unwrap();
    ((first as u32 - 'A' as u32) as i32, (second as u32 - 'X' as u32) as i32)
}