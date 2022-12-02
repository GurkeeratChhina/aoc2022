input_file = 'd2/input.txt'

def score_given(input):
    return 3*((input[1]-input[0]+1) % 3) + input[1] + 1

def total_score_given(filename):
    sum = 0
    with open(filename) as file:
        for line in file:
            round = line.strip().split()
            round_int = [ord(round[0]) - ord("A"), ord(round[1]) - ord("X")]
            sum += score_given(round_int)
    return sum

def score_outcome(input):
    return 3*input[1] + (input[0]+input[1]-1)%3 + 1

def total_score_outcome(filename):
    sum = 0
    with open(filename) as file:
        for line in file:
            round = line.strip().split()
            round_int = [ord(round[0]) - ord("A"), ord(round[1]) - ord("X")]
            sum += score_outcome(round_int)
    return sum
        

if __name__ == '__main__':
    print(total_score_given(input_file))
    print(total_score_outcome(input_file))