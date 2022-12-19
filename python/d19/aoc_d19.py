import re

input_file  = 'python/d19/input.txt'

def find_maximum_geodes(blueprint, time):
    remaining_time = time

    def can_build(node):
        cost = blueprint[node[8]]
        for i in range(3):
            if cost[i] > node[i]:
                return False
        return True

    def next_node_list(node):
        return [node[0]+node[4], node[1]+node[5], node[2]+node[6], node[3]+node[7]] + list(node[4:])

    def max_cost(i):
        return max([cost[i] for cost in blueprint])

    def should_add(i):
        if i == 0 and node[5] > 0:
            return False
        if i < 3 and node[4+i]*remaining_time + node[i] >= max_cost(i)*remaining_time:
            return False
        return True

    def next_builds(node):
        index_built = node[8]
        cost = blueprint[index_built]
        output = set()
        for i in range(4):
            if should_add(i):
                new_node = next_node_list(node)
                for j in range(3):
                    new_node[j] -= cost[j]
                new_node[index_built+4] += 1
                new_node[8] = i
                output.add(tuple(new_node))
        return output
    
    def find_max(layer,index):
        maximum = 0
        for node in layer:
            maximum = max(maximum, node[index])
        return maximum

    current_layer = {(0,0,0,0,1,0,0,0,0),(0,0,0,0,1,0,0,0,1),(0,0,0,0,1,0,0,0,2),(0,0,0,0,1,0,0,0,3)}
    for i in range(time):
        remaining_time = time-i
        next_layer = set()
        for node in current_layer:
            if can_build(node):
                next_layer.update(next_builds(node))
            else:
                next_layer.add(tuple(next_node_list(node)))
        current_layer = next_layer
    return find_max(current_layer, 3)

def parse_blueprint(line):
    nums = [int(x) for x in re.findall(r'-?\d+', line)]
    return ((nums[1],0,0),(nums[2],0,0),(nums[3],nums[4],0),(nums[5],0,nums[6]))

def part1(filename):
    quality_level = 0
    with open(filename) as file:
        lines = file.readlines()
        for i in range(len(lines)):
            bp = parse_blueprint(lines[i])
            max_geodes = find_maximum_geodes(bp, 24)
            # print(i+1, max_geodes)
            quality_level += (max_geodes*(i+1))
    return quality_level

def part2(filename):
    prod = 1
    with open(filename) as file:
        lines = file.readlines()
        for i in range(3):
            bp = parse_blueprint(lines[i])
            max_geodes = find_maximum_geodes(bp, 32)
            print(i+1, max_geodes)
            prod = prod*max_geodes
    return prod

if __name__ == '__main__':
    # test_bp = ((2,0,0),(3,0,0),(3,8,0),(3,0,12))
    # print(find_maximum_geodes(test_bp,24))
    print(part1(input_file))

    