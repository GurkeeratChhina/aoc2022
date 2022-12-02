input_file = 'd2/input.txt'

def outcome(input):
    return (input[1]-input[0]+1) % 3

def score(input):
    return 3*outcome(input) + input[1] + 1

def total_score(filename):
    sum = 0
    with open(filename) as file:
        for line in file:
            round = line.strip().split()
            round_int = [ord(round[0]) - ord("A"), ord(round[1]) - ord("X")]
            sum += score(round_int)
    return sum

if __name__ == '__main__':
    print(total_score(input_file))