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

def human_value(dictionary):
    
    def parse_operation(op_str):
        a, op, b = op_str.split()
        c = recursive_value(a)
        d = recursive_value(b)
        if isinstance(c, str) or isinstance(d, str):
            return op_str
        elif op == "+":
            return c + d
        elif op == "-":
            return c - d
        elif op == "*":
            return c * d
        elif op == "/":
            return c / d
    
    def recursive_value(id):
        if id == 'humn':
            return "humn"
        if isinstance(dictionary[id], str):
            value = parse_operation(dictionary[id])
            dictionary[id] = value
        return dictionary[id]

    recursive_value("root")

    def reverse_operation(id, value):
        if id == "humn":
            dictionary[id] = value
            return
        a, op, b = dictionary[id].split()
        dictionary[id] = value
        if isinstance(dictionary[a], str):
            if op == "+":
                return reverse_operation(a, value - dictionary[b])
            elif op == "-":
                return reverse_operation(a, value + dictionary[b])
            elif op == "*":
                return reverse_operation(a, value / dictionary[b])
            elif op == "/":
                return reverse_operation(a, value * dictionary[b])
        elif isinstance(dictionary[b], str):
            if op == "+":
                return reverse_operation(b, value - dictionary[a])
            elif op == "-":
                return reverse_operation(b, dictionary[a]-value)
            elif op == "*":
                return reverse_operation(b, value / dictionary[a])
            elif op == "/":
                return reverse_operation(b,  dictionary[a]/value)

    dictionary["humn"] = "humn"
    left, middle, right = dictionary["root"].split()
    if isinstance(dictionary[left], str):
        reverse_operation(left, dictionary[right])
    elif isinstance(dictionary[right], str):
        reverse_operation(right, dictionary[left])
    

if __name__ == '__main__':
    mydict = build_dict(input_file)
    mydict2 = mydict.copy()
    print(root_value(mydict))
    human_value(mydict2)
    print(mydict2["humn"])
