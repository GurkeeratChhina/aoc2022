import re

input_file  = 'python/d22/input.txt'
test_file = 'python/d22/test.txt'

def build_grid(filename):
    grid = []
    with open(filename) as file:
        for line in file:
            grid.append(line.strip("\n"))
    return grid[:-2], grid[-1]

def turn_to_int(turn):
    if turn == "L":
        return -1
    if turn == "R":
        return 1

def extract_distances(instructions):
    return [int(x) for x in re.findall(r'\d+', instructions)]

def extract_turns(instructions):
    return re.findall(r'[LR]', instructions)

def find_start_x(grid):
    for i in range(len(grid[0])):
        if grid[0][i] == ".":
            return i

def calc_next_pos(x,y,facing,x_max,y_max):
    if facing == 0:
        return (x+1)%x_max, y
    elif facing == 1:
        return x, (y+1)%y_max
    elif facing == 2:
        return (x-1)%x_max, y
    elif facing == 3:
        return x, (y-1)%y_max

def calc_box_coords(x,y, facing):
    bigx = x//50
    bigy = y//50
    if bigx == 0:
        if bigy == 0:
            if facing == 0:
                return 99,149-y,2
            elif facing == 1:
                return x+100,0,1
            elif facing == 2:
                return 0,149-y,0
            else:
                print("error1!")
        elif bigy == 1:
            if facing == 2:
                return y-50,100,1
            elif facing == 3:
                return 50,x+50,0
            else:
                print("error2!")
        else:
            print("error3!")
    elif bigx == 1:
        if facing == 0:
            return y-100,149,3
        elif facing == 1:
            return 49,x+100,2
        elif facing == 3:
            return 0,x+100,0
        else:
            print("error4!")
    elif bigx == 2:
        if bigy == 1:
            if facing == 0:
                return y+50,49,3
            elif facing == 1:
                return 99,x-50,2
            else:
                print("error5!",x,y,facing)
        elif bigy == 2:
            if facing == 0:
                return 149,149-y,2
            elif facing == 2:
                return 50,149-y,0
            else:
                print("error6!")
        elif bigy == 3:
            if facing == 2:
                return y-100,0,1
            elif facing == 3:
                return x-100,199,3
            else:
                print("error7!")
        else:
           print("error8!") 

class GridInstructions:
    def __init__(self, grid, instructions):
        self.grid = grid
        self.instructions = instructions
        self.x = find_start_x(grid)
        self.y = 0
        self.facing = 0
        self.y_max = len(grid)
        self.x_max = max([len(grid[i]) for i in range(len(grid))])
        self.distances = extract_distances(instructions)
        self.turns = extract_turns(instructions)

    def move(self, i, mode):
        # print("moving", self.distances[i], "spaces to the", self.facing)
        # print("current position", self.x,self.y)
        for j in range(self.distances[i]):
            # print("step number:", j)
            next_pos_x, next_pos_y = calc_next_pos(self.x,self.y,self.facing,self.x_max,self.y_max)
            next_facing = self.facing
            while True:
                # print("looking for next valid space")
                try:
                    if self.grid[next_pos_y][next_pos_x]  == "#":
                        # print("wall found")
                        return
                    elif self.grid[next_pos_y][next_pos_x] == ".":
                        # print("empty space found")
                        self.x, self.y, self.facing = next_pos_x, next_pos_y, next_facing
                        break
                    else:
                        if mode == "torus":
                            next_pos_x, next_pos_y = calc_next_pos(next_pos_x,next_pos_y,self.facing,self.x_max,self.y_max)
                        elif mode == "cube":
                            # print("pre cubewrapping!",next_pos_x,next_pos_y,next_facing)
                            next_pos_x, next_pos_y, next_facing = calc_box_coords(next_pos_x,next_pos_y,next_facing)
                            # print("post cubewrapping!",next_pos_x,next_pos_y,next_facing)
                except:
                    # print("valid space not found")
                    if mode == "torus":
                        next_pos_x, next_pos_y = calc_next_pos(next_pos_x,next_pos_y,self.facing,self.x_max,self.y_max)
                    elif mode == "cube":
                        # print("pre cubewrapping!",next_pos_x,next_pos_y,next_facing)
                        next_pos_x, next_pos_y, next_facing = calc_box_coords(next_pos_x,next_pos_y,next_facing)
                        # print("post cubewrapping!",next_pos_x,next_pos_y,next_facing)

    def follow_instructions(self, mode):
        for i in range(len(self.turns)):
        # for i in range(1):
            # print("movement iteration number:", i)
            # print("position before movement", i, ":", self.x, self.y, self.facing)
            self.move(i,mode) 
            self.facing = (self.facing + turn_to_int(self.turns[i]))%4
        # print("position before movement 6 :", self.x, self.y, self.facing)
        self.move(-1,mode)
        return self.x,self.y,self.facing

if __name__ == '__main__':
    grid, instructions = build_grid(input_file)
    mygrid = GridInstructions(grid, instructions)
    mysecondgrid = GridInstructions(grid, instructions)
    x,y,facing = mygrid.follow_instructions("torus")
    print(x,y,facing, "\n", 1000*(y+1)+ 4*(x+1)+facing)
    x2,y2,facing2 = mysecondgrid.follow_instructions("cube")
    print(x2,y2,facing2, "\n", 1000*(y2+1)+ 4*(x2+1)+facing2)