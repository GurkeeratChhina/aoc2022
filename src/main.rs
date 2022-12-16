#[path = "d1/d1.rs"] mod d1;

fn main() {
    println!("Here are the results for day 1.");
    println!("Part 1: {}, Part 2: {}", d1::part1(), d1::part2());
}