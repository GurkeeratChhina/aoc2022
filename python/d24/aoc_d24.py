import re

input_file  = 'python/d24/input.txt'
test_file = 'python/d24/test.txt'

class ValleyState:
    def __init__(self, height, width):
        self.hei = height
        self.wid = width
        self.state = [[[(0,0)] for x in range(width)] for y in range(height)]

    def loop_0_to_back(self):
        for y in range(self.hei):
            for x in range(self.wid):
                self.state[y][x].remove((0,0))
                self.state[y][x].append((0,0))

    def update_state(self):
        for y in range(self.hei):
            for x in range(self.wid):
                while True:
                    arrow = self.state[y][x][0]
                    if arrow == (0,0):
                        self.state[y][x].append(arrow)
                        del self.state[y][x][0]
                        break
                    elif arrow == (1,0):
                        self.state[y][(x+1)%self.wid].append(arrow)
                        del self.state[y][x][0]
                    elif arrow == (-1,0):
                        self.state[y][(x-1)%self.wid].append(arrow)
                        del self.state[y][x][0]
                    elif arrow == (0,1):
                        self.state[(y+1)%self.hei][x].append(arrow)
                        del self.state[y][x][0]
                    elif arrow == (0,-1):
                        self.state[(y-1)%self.hei][x].append(arrow)
                        del self.state[y][x][0]
        self.loop_0_to_back()
    
    def find_safe(self):
        safes = []
        for y in range(self.hei):
            for x in range(self.wid):
                if len(self.state[y][x]) == 1:
                    safes.append((x,y))
        return safes

    def print(self):
        for y in range(self.hei):
            for x in range(self.wid):
                if len(self.state[y][x]) == 1:
                    print(".", end = "")
                elif len(self.state[y][x]) == 2:
                    print(to_symbol(self.state[y][x][0]), end = "")
                else:
                    print(len(self.state[y][x])-1, end="")
            print("")

    def fastest_trip(self, start, end):
        self.loop_0_to_back()
        i = 0
        reachable_positions = {start}
        while True:
            # print("i =", i)
            # valley.print()
            i +=1
            self.update_state()
            safe_spots = self.find_safe()
            new_reachables = {start}
            for pos in safe_spots:
                if any(x in reachable_positions for x in adjacencies(pos)):
                    new_reachables.add(pos)
            reachable_positions = new_reachables
            if end in reachable_positions:
                self.update_state()
                return i+1

def to_tuple(symbol):
    if symbol == ".":
        return None
    elif symbol == "<":
        return (-1,0)
    elif symbol == ">":
        return (1,0)
    elif symbol == "^":
        return (0,-1)
    elif symbol == "v":
        return (0,1)

def to_symbol(tup):
    if tup == (0,0):
        return "."
    elif tup == (-1,0):
        return "<"
    elif tup == (1,0):
        return ">"
    elif tup == (0,-1):
        return "^"
    elif tup == (0,1):
        return "v"

def parse(filename):
    valley = None
    with open(filename) as file:
        lines = file.readlines()
        height = len(lines) - 2
        width = len(lines[0]) - 3
        valley = ValleyState(height, width)
        for y in range(height):
            for x in range(width):
                arrow = to_tuple(lines[y+1][x+1])
                if arrow is not None:
                    valley.state[y][x].append(arrow)
    return valley

def adjacencies(position):
    x,y = position[0], position[1]
    return [(x,y),(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

if __name__ == '__main__':
    valley = parse(input_file)
    distances = []
    distances.append(valley.fastest_trip((0,-1), (valley.wid-1, valley.hei-1)))
    distances.append(valley.fastest_trip((valley.wid-1, valley.hei),(0,0)))
    distances.append(valley.fastest_trip((0,-1), (valley.wid-1, valley.hei-1)))
    print(distances, sum(distances))
        
