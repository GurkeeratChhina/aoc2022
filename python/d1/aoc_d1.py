input_file = 'python/d1/input.txt'

def find_largest(filename):
    sum = 0
    max_sum = 0
    with open(filename) as file:
        for line in file:
            if not line.strip():
                max_sum = max(max_sum, sum)
                sum = 0
            else:
                sum += int(line.strip())
    return max_sum

def find_largest_three(filename):
    sum = 0
    max_sum = [0,0,0]
    with open(filename) as file:
        for line in file:
            if not line.strip():
                max_sum = sorted(max_sum + [sum])[1:4]
                sum = 0
            else:
                sum += int(line.strip())
    return max_sum

if __name__ == '__main__':
    print(find_largest(input_file))
    print(sum(find_largest_three(input_file)))