input_file = 'python/d13/input.txt'

def is_less_than(list1, list2):
    if isinstance(list1, int) and isinstance(list2, int):
        if list1 == list2:
            return "equal"
        else:
            return list1 < list2
    elif isinstance(list1, int) and isinstance(list2, list):
        return is_less_than([list1], list2)
    elif isinstance(list1, list) and isinstance(list2, int):
        return is_less_than(list1, [list2])
    else:
        for i in range(min(len(list1), len(list2))):
            comparison = is_less_than(list1[i], list2[i])
            if comparison != "equal":
                return comparison
        if len(list1) == len(list2):
            return "equal"
        else:
            return len(list1) < len(list2)

def parse(filename, first, second):
    sum = 0
    index_first = 1
    index_second = 2
    with open(filename) as file:
        pair_index = 1
        while(True):
            try:
                first_list = eval(file.readline().strip())
                second_list = eval(file.readline().strip())
                if is_less_than(first_list,second_list):
                    sum += pair_index
                if is_less_than(first_list, first):
                    index_first += 1
                    index_second += 1
                elif is_less_than(first_list, second):
                    index_second += 1
                if is_less_than(second_list, first):
                    index_first += 1
                    index_second += 1
                elif is_less_than(second_list, second):
                    index_second += 1
                pair_index += 1
                file.readline()
            except:
                break
    return [sum, index_first*index_second]

if __name__ == '__main__':
    print(parse(input_file, [[2]], [[6]]))