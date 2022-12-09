input_file = 'd9/input.txt'

def move_head(head,tail,direction,visited):
    if max([abs(head[i]+direction[i]-tail[i]) for i in (0,1)]) > 1:
        tail[:] = head
        visited.add(tuple(tail))
    head[:] = [head[i]+direction[i] for i in (0,1)]
    
def to_direction(letter):
    if letter == "L":
        return (-1,0)
    if letter == "R":
        return (1,0)
    if letter == "U":
        return (0,1)
    if letter == "D":
        return (0,-1)


def count_visited(filename):
    head = [0,0]
    tail = [0,0]
    visited = {(0,0)}
    with open(filename) as file:
        for line in file:
            for i in range(int(line.strip().split()[1])):
                move_head(head, tail, to_direction(line.strip().split()[0]), visited)
    return len(visited)
            

if __name__ == '__main__':
    print(count_visited(input_file))