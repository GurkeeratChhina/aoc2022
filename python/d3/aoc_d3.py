input_file = 'python/d3/input.txt'

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
        while True:
            try:
                linea = file.readline().strip()
                lineb = file.readline().strip()
                linec = file.readline().strip()
                repeat_letter = set(linea).intersection(set(lineb), set(linec))
                num = ord(repeat_letter.pop())
                priority = num - ord("A") + 27 if num < ord("a") else num - ord("a") + 1
                sum += priority
            except:
                break
    return sum

if __name__ == '__main__':
    print(priority_duplicates(input_file))
    print(priority_badges(input_file))