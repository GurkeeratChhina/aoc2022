input_file = 'python/d17/input.txt'
test_file = 'python/d17/test.txt'

max_sims = 1000000000000

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
        self.height = 0
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
            self.height = max(self.height, point[1])
        del rock

    def process_new_rock(self):
        rock = self.new_rock()
        while True:
            self.try_move(rock, to_direction(self.tape[self.left_right_index]))
            self.left_right_index = (self.left_right_index + 1)%self.tape_len
            successful = self.try_move(rock, (0,-1))
            if not successful:
                self.add_to_formation(rock)
                break

    def new_rock(self):
        rock = Rock(3, self.height+4, self.rock_count)
        self.rock_count += 1
        while len(self.formation) < self.height + 8:
            self.formation.append([1,0,0,0,0,0,0,0,1])
        return rock

    def find_cycle(self):
        past_positions = {}
        while True:
            self.process_new_rock()
            newtuple = (self.left_right_index, self.rock_count%5,tuple(self.formation[self.height]))
            if newtuple in past_positions:
                return [(self.height, self.rock_count),past_positions[newtuple]]
            else:
                past_positions[newtuple] = (self.height, self.rock_count)

    def height_with_cycles(self, iterations):
        self.find_cycle()
        cycle = myTetris.find_cycle()
        old_height = cycle[1][0]
        new_height = cycle[0][0]
        old_rocks = cycle[1][1]
        new_rocks = cycle[0][1]
        cycle_len_rocks = new_rocks- old_rocks
        cycle_len_height = new_height - old_height
        number_cycles = (iterations-old_rocks)//cycle_len_rocks
        remainder = (iterations-old_rocks)%cycle_len_rocks
        for i in range(remainder):
            self.process_new_rock()
        from_remainder = self.height - new_height
        final_height = old_height + cycle_len_height*number_cycles + from_remainder
        return final_height

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
    # for i in range(2022):
    #     myTetris.process_new_rock()
    # print(myTetris.height)
    print(myTetris.height_with_cycles(max_sims))

