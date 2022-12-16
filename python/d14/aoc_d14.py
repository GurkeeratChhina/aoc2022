from numpy import sign

input_file = 'python/d14/input.txt'
test_file = 'python/d14/test.txt'

class Maze():
    def __init__(self, width, height, origin):
        self.height = height
        self.width = width
        self.array = [[0 for x in range(width+1)] for y in range(height+1)]
        self.sand_count = 0
        self.origin = origin

    def add_line(self, start, end):
        if start[0] == end[0]:
            for y in range(start[1], end[1], sign(end[1]-start[1])):
                self.array[y][start[0]] = 1
        else:
            for x in range(start[0], end[0], sign(end[0]-start[0])):
                self.array[start[1]][x] = 1

    def add_point(self, point):
        self.array[point[1]][point[0]] = 1
    
    def make_one_sand(self):
        position = list(self.origin)
        while(True):
            if position[1] == self.height:
                return False
            if self.array[position[1]+1][position[0]] == 0:
                position[1] += 1
            elif position[0] == 0:
                return False
            elif self.array[position[1]+1][position[0]- 1] == 0:
                position[1] += 1
                position[0] -= 1
            elif position[0] == self.width:
                return False
            elif self.array[position[1]+1][position[0]+ 1] == 0:
                position[1] += 1
                position[0] += 1
            else:
                self.array[position[1]][position[0]] = 1
                self.sand_count += 1
                return True
    
    def make_sand(self):
        while(self.array[self.origin[1]][self.origin[0]] == 0):
            if not self.make_one_sand():
                break
        return self.sand_count
    
    def draw(self, solid = "█", empty = " "):
        for row in self.array:
            for elem in row:
                if elem == 0:
                    print(empty, end = "")
                if elem == 1:
                    print(solid, end = "")
            print("")

def find_min_max(filename):
    x_min = 99999
    x_max = 0
    y_max = 0
    with open(filename) as file:
        for line in file:
            for pair in line.strip().split("->"):
                x_min = min(x_min, int(pair.split(",")[0]))
                x_max = max(x_max, int(pair.split(",")[0]))
                y_max = max(y_max, int(pair.split(",")[1]))
    return [x_min,x_max,y_max]

def make_maze(filename, x_min, x_max, y_max, origin):
    maze = Maze(x_max - x_min, y_max, (origin[0] - x_min, origin[1]))
    with open(filename) as file:
        for line in file:
            coords = [[int(pair.split(",")[0]) - x_min, int(pair.split(",")[1])] for pair in line.strip().split("->")]
            for i in range(len(coords) - 1):
                maze.add_line(coords[i], coords[i+1])
            maze.add_point(coords[-1])
    return maze

if __name__ == '__main__':
    x_min,x_max,y_max = find_min_max(input_file)
    myMaze = make_maze(input_file, x_min, x_max, y_max, [500, 0])
    print(myMaze.make_sand())
    myMaze2 = make_maze(input_file, x_min - y_max, x_max + y_max, y_max+2, [500,0])
    myMaze2.add_line([0, y_max+2], [x_max - x_min + 2*y_max, y_max+2])
    myMaze2.add_point([x_max - x_min + 2*y_max, y_max+2])
    print(myMaze2.make_sand())

