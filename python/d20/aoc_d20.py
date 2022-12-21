import re

input_file  = 'python/d20/input.txt'

decryption_key = 811589153

def parse(filename):
    with open(filename) as file:
        lines = file.readlines()
        num_lines = len(lines)
        output = []
        for i in range(num_lines):
            output.append((int(lines[i].strip()),i))
        return output

def part1(nums,num_iterations):
    tomix = nums.copy()
    n = len(nums)
    zero_elem = None
    for j in range(num_iterations):
        for i in range(n):
            elem_to_move = nums[i]
            if elem_to_move[0] == 0:
                zero_elem = elem_to_move
                continue
            index_of_elem = tomix.index(elem_to_move)
            del tomix[index_of_elem]
            new_index = (index_of_elem + elem_to_move[0]) % (n-1)
            tomix.insert(new_index, elem_to_move)
    zero_index = tomix.index(zero_elem)
    return sum([tomix[(zero_index+i)%n][0] for i in [1000,2000,3000]])


if __name__ == '__main__':
    nums = parse(input_file)
    print(part1(nums,1))
    bignums = [(x[0]*decryption_key,x[1]) for x in nums]
    print(part1(bignums,10))