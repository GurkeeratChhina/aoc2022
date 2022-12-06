input_file = 'd6/input.txt'

def has_duplicates(list):
    return not len(list) == len(set(list))

def find_marker(filename):
    with open(filename) as file:
        line = file.readline()
        for i in range(len(line)):
            if not has_duplicates(line[i:i+4]):
                return i+4

if __name__ == '__main__':
    print(find_marker(input_file))