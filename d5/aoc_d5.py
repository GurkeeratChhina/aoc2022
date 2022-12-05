input_file = 'd5/input.txt'

def move_crate_single(amount, origin, destination):
    destination[:] = list(reversed(origin[0:amount])) + destination
    origin[:] = origin[amount:]

def move_crate_stack(amount, origin, destination):
    destination[:] = origin[0:amount] + destination
    origin[:] = origin[amount:]

def move_crates(filename, movement_function):
    list_of_piles = []
    with open(filename) as file:
        line = file.readline()
        num_piles = len(line)//4
        list_of_piles = [[] for i in range(num_piles)]
        while True:
            try:
                for i in range(num_piles):
                    if line[1+4*i].strip():
                        list_of_piles[i].append(line[1+4*i])
                line = file.readline()
            except:
                break
        while True:
            try:
                line = file.readline().split()
                movement_function(int(line[1]), list_of_piles[int(line[3])-1], list_of_piles[int(line[5])-1])
            except:
                break
    return [pile[0] for pile in list_of_piles]


if __name__ == '__main__':
    print(*move_crates(input_file, move_crate_single))
    print(*move_crates(input_file, move_crate_stack))