input_file = 'd3/input.txt'

def repeat(line):
    half = int(len(line)/2)
    first_half = set(line[0:half])
    second_half = set(line[half:2*half])
    return (first_half.intersection(second_half)).pop()

def priority_duplicates(filename):
    sum = 0
    with open(filename) as file:
        for line in file:
            num = ord(repeat(line.strip()))
            priority = num - ord("A") + 27 if num < ord("a") else num - ord("a") + 1
            sum += priority
    return sum

def priority_badges(filename):
    sum = 0
    with open(filename) as file:
        lines = file.readlines()
        for a,b,c in zip(lines[::3], lines[1::3], lines[2::3]):
            repeat_letter = (set(a.strip()).intersection(set(b.strip()),set(c.strip())))
            num = ord(repeat_letter.pop())
            priority = num - ord("A") + 27 if num < ord("a") else num - ord("a") + 1
            sum += priority
    return sum

if __name__ == '__main__':
    print(priority_duplicates(input_file))
    print(priority_badges(input_file))