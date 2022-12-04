input_file = 'd4/input.txt'

def range_subset(a,b,c,d):
    """Returns true if (a,b) is a subset of (c,d) or vice versa"""
    return (a<=c and b>=d) or (a>=c and b<=d)

def count_inclusions(filename):
    sum = 0
    with open(filename) as file:
        for line in file:
            sum += range_subset(*[int(item) for half in line.strip().split(",") for item in half.split("-")])
    return sum

if __name__ == '__main__':
    print(count_inclusions(input_file))