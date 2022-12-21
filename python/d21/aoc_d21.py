import re

input_file  = 'python/d21/input.txt'
test_file = 'python/d21/test.txt'

def build_dict(filename):
    monkey_dict = {}
    with open(filename) as file:
        for line in file:
            id, value = line.strip().split(":")
            if value.strip().isdigit():
                monkey_dict[id] = int(value)
            else:
                monkey_dict[id] = value
    return monkey_dict

def root_value(dictionary):
    def parse_operation(op_str):
        a, op, b = op_str.split()
        if op == "+":
            return recursive_value(a) + recursive_value(b)
        elif op == "-":
            return recursive_value(a) - recursive_value(b)
        elif op == "*":
            return recursive_value(a) * recursive_value(b)
        elif op == "/":
            return recursive_value(a) / recursive_value(b)
    
    def recursive_value(id):
        if isinstance(dictionary[id], str):
            value = parse_operation(dictionary[id])
            dictionary[id] = value
        return dictionary[id]
    
    return recursive_value('root')

if __name__ == '__main__':
    mydict = build_dict(input_file)
    print(root_value(mydict))