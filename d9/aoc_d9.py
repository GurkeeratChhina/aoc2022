from numpy import sign

input_file = 'd9/input.txt'

class LinkedList:
    def __init__(self, length, dimension = 2):
        self.current = [0 for i in range(dimension)]
        if length == 1:
            self.next = None
        else:
            self.next = LinkedList(length-1)

def l_infinity(point_a, point_b):
    return max([abs(point_a[i] - point_b[i]) for i in range(len(point_a))])

def get_direction(point_a, point_b):
    return tuple([sign(point_b[i]-point_a[i]) for i in range(len(point_a))])

def move_list(LL, direction, visited):
    LL.current[:] = [LL.current[i]+direction[i] for i in range(len(LL.current))]
    if LL.next is None:
        visited.add(tuple(LL.current))
    elif l_infinity(LL.current, LL.next.current) > 1:
        move_list(LL.next, get_direction(LL.next.current, LL.current), visited)

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


def count_visited(filename, length):
    rope = LinkedList(length)
    visited = {(0,0)}
    with open(filename) as file:
        for line in file:
            for i in range(int(line.strip().split()[1])):
                move_list(rope, to_direction(line.strip().split()[0]), visited)
    return len(visited)
            

if __name__ == '__main__':
    print(count_visited(input_file, 2))
    print(count_visited(input_file, 10))