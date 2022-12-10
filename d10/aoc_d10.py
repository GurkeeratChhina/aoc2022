input_file = 'd10/input.txt'

class Computer:
    def __init__(self, register = 1, cycles = 0):
        self.cycles = cycles
        self.register = register
        self.count = 0
    
    def noop(self):
        self.cycles += 1
        if self.cycles%40 == 20:
            self.count += self.cycles*self.register
    
    def addx(self, x):
        self.noop()
        self.noop()
        self.register += x

def read_input(filename):
    myComputer = Computer()
    with open(filename) as file:
        for line in file:
            if line.strip() == "noop":
                myComputer.noop()
            else:
                myComputer.addx(int(line.strip().split()[1]))
    return myComputer


if __name__ == '__main__':
    testcomputer = read_input(input_file)
    print(testcomputer.cycles, testcomputer.count)
