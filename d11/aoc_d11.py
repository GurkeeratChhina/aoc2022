from sympy.parsing.sympy_parser import parse_expr
from sympy import lambdify

input_file = 'd11/input.txt'

class Monkey:
    def __init__(self, list_of_items, if_true, if_false, throw_condition, worry_update, relief_function):
        self.items = list_of_items
        self.next_true = if_true
        self.next_false = if_false
        self.update = worry_update
        self.condition = throw_condition
        self.total_inspected = 0
        self.relief = relief_function
    
    def update_worries(self):
        self.items[:] = [self.relief(self.update(item)) for item in self.items]
    
    def pass_items(self):
        for item in self.items:
            if not item%self.condition:
                self.next_true.items.append(item)
            else:
                self.next_false.items.append(item)
        self.total_inspected += len(self.items)
        self.items[:] = []

class MonkeyCollection:
    def __init__(self, list_of_monkeys):
        self.monkeys = list_of_monkeys
        for monkey in self.monkeys:
            monkey.next_true = self.monkeys[monkey.next_true]
            monkey.next_false = self.monkeys[monkey.next_false]
    
    def do_round(self, amount):
        for i in range(amount):
            for monkey in self.monkeys:
                monkey.update_worries()
                monkey.pass_items()

    def monkey_business(self):
        inspections = sorted([monkey.total_inspected for monkey in self.monkeys])
        print(inspections)
        return inspections[-1]*inspections[-2]
        
def parse_input(filename, relief_function):
    list_of_monkeys = []
    with open(filename) as file:
        while(True):
            try:
                file.readline()
                items = [int(x) for x in file.readline().strip().split(":")[1].split(",")]
                worry_function = lambdify(parse_expr("old"), parse_expr(file.readline().strip().split("=")[1]))
                test = int(file.readline().strip().split(" ")[-1])
                pass_true = int(file.readline().strip().split(" ")[-1])
                pass_false = int(file.readline().strip().split(" ")[-1])
                file.readline()
                list_of_monkeys.append(Monkey(items,pass_true,pass_false,test,worry_function, relief_function))
            except:
                break
    return list_of_monkeys

if __name__ == '__main__':
    monkeys = MonkeyCollection(parse_input(input_file, lambda x: x//3))
    monkeys.do_round(20)
    print(monkeys.monkey_business())
    monkeys2 = MonkeyCollection(parse_input(input_file, lambda x: x%9699690))
    monkeys2.do_round(10000)
    print(monkeys2.monkey_business())
