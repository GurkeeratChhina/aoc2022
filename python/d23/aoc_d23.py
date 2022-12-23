from copy import deepcopy

input_file  = 'python/d23/input.txt'
test_file = 'python/d23/test.txt'

def add(tuple1, tuple2):
    return tuple([tuple1[i]+tuple2[i] for i in range(len(tuple1))])

class Process:
    locations = {}
    iterations = 0

    def do_iteration(self):
        if all(self.get_next(loc) for loc in self.locations):
            return False
        for location in self.locations:
            self.get_next(location)
        copy = deepcopy(self.locations)
        for location in copy:
            next_location=add(location, self.locations[location])
            if next_location == location:
                continue
            if next_location in self.locations:
                self.locations[add(next_location,self.locations[location])] = (0,0)
                del self.locations[next_location]
            else: 
                self.locations[next_location] = (0,0)
                del self.locations[location]
        self.iterations = (self.iterations +1)%4
        return True

    def get_next(self, location):
        surrounding_8 = [(1,1),(0,1),(-1,1),(1,0),(-1,0),(1,-1), (0,-1),(-1,-1)]
        if all(adjacent not in self.locations for adjacent in [add(location, delta) for delta in surrounding_8]):
            self.locations[location] = (0,0)
            return True
        for j in range(4):
            if self.get_next_i(location, (j+self.iterations)%4):
                return False
        self.locations[location] = (0,0)
        return True

    def get_next_i(self,location,i):
        if i == 0:
            for j in range(-1,2):
                if add(location, (j, -1)) in self.locations:
                    return False
            self.locations[location] = (0,-1)
            return True
        elif i == 1:
            for j in range(-1,2):
                if add(location, (j, 1)) in self.locations:
                    return False
            self.locations[location] = (0,1)
            return True
        elif i == 2:
            for j in range(-1,2):
                if add(location, (-1, j)) in self.locations:
                    return False
            self.locations[location] = (-1,0)
            return True
        elif i == 3:
            for j in range(-1,2):
                if add(location, (1, j)) in self.locations:
                    return False
            self.locations[location] = (1,0)
            return True

    def get_bounds(self):
        first = next(iter(self.locations))
        x_min, x_max = first[0], first[0]
        y_min, y_max = first[1], first[1]
        count = 0
        for key in self.locations:
            x_min = min(key[0], x_min)
            x_max = max(key[0], x_max)
            y_min = min(key[1], y_min)
            y_max = max(key[1], y_max)
            count += 1
        return x_min, x_max, y_min, y_max, count
    
    def part1(self):
        for i in range(10):
            self.do_iteration()
        a,b,c,d,e = self.get_bounds()
        # print(a,b,c,d,e)
        return (b-a+1)*(d-c+1) - e
    
    def add_loc(self, location):
        self.locations[location] = (0,0)

    def print(self):
        a,b,c,d,e = self.get_bounds()
        for j in range(c,d+1):
            for i in range(a,b+1):
                if (i,j) in self.locations:
                    print("#", end = "")
                else:
                    print(".", end = "")
            print("")
    
    def part2(self):
        i = 0
        while(self.do_iteration()):
            i+=1
        return i+1

def parse(filename):
    myProcess = Process()
    with open(filename) as file:
        lines = file.readlines()
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if lines[i][j] == "#":
                    myProcess.add_loc((j,i))
    return myProcess

if __name__ == '__main__':
    myProcess = parse(input_file)
    print(myProcess.part2())