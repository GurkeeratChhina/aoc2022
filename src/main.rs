#[path = "puzzles/d1.rs"] mod d1;
#[path = "puzzles/d2.rs"] mod d2;

fn main() {
    println!("Here are the results for day 1.");
    println!("Part 1: {}, Part 2: {}", d1::part1(), d1::part2());
    println!("Here are the results for day 2.");
    println!("Part 1: {}, Part 2: {}", d2::part1(), d2::part2());
}