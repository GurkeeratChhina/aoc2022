input_file = 'python/d17/input.txt'
test_file = 'python/d17/test.txt'

class Rock:
    def __init__(self, x,y, rock_type):
        if rock_type%5 == 0:
            self.points = [(x,y), (x+1,y), (x+2,y), (x+3,y)]
        elif rock_type%5 == 1:
            self.points = [(x,y+1), (x+1,y), (x+1,y+1), (x+1,y+2), (x+2,y+1)]
        elif rock_type%5 == 2:
            self.points = [(x,y), (x+1,y), (x+2,y), (x+2,y+1), (x+2,y+2)]
        elif rock_type%5 == 3:
            self.points = [(x,y), (x,y+1), (x,y+2), (x,y+3)]
        elif rock_type%5 == 4:
            self.points = [(x,y), (x,y+1), (x+1,y), (x+1,y+1)]

    def move(self, direction):
        self.points = [(point[0] + direction[0], point[1] + direction[1]) for point in self.points]

class Game:
    def __init__(self, left_right_tape):
        self.formation = [[1,1,1,1,1,1,1,1,1],[1,0,0,0,0,0,0,0,1]]
        self.height = 1
        self.rock_count = 0
        self.left_right_index = 0
        self.tape = left_right_tape
        self.tape_len = len(left_right_tape)

    def __str__(self):
        for i in range(1, len(self.formation)+1):
            for x in self.formation[-i]:
                if x == 1:
                    print("█", end = "")
                elif x == 0:
                    print(" ", end = "")
            print("")
        return ""
    def try_move(self, rock, direction):
        rock.move(direction)
        for point in rock.points:
            if self.formation[point[1]][point[0]] == 1:
                rock.move((-direction[0], -direction[1]))
                return False
        return True

    def add_to_formation(self, rock):
        for point in rock.points:
            self.formation[point[1]][point[0]] = 1
            self.height = max(self.height, point[1]+1)
        del rock

    def process_new_rock(self):
        rock = self.new_rock()
        while True:
            self.try_move(rock, to_direction(self.tape[self.left_right_index%self.tape_len]))
            self.left_right_index += 1
            successful = self.try_move(rock, (0,-1))
            if not successful:
                self.add_to_formation(rock)
                break

    def new_rock(self):
        rock = Rock(3, self.height+3, self.rock_count)
        self.rock_count += 1
        while len(self.formation) < self.height + 7:
            self.formation.append([1,0,0,0,0,0,0,0,1])
        return rock

def to_direction(arrow):
    if arrow == '<':
        return (-1,0)
    elif arrow == '>':
        return (1,0)

if __name__ == '__main__':
    tape = ""
    with open(input_file) as f:
        tape = f.readline().strip()
    myTetris = Game(tape)
    for i in range(1000000000000):
        myTetris.process_new_rock()
    print(myTetris.height-1)