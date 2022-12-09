input_file = 'd8/input.txt'

def to_array(filename):
    array = []
    with open(filename) as file:
        for line in file:
            array.append([int(digit) for digit in line.strip()])
    return array

def visibility_up(tree_x, tree_y, tree_array):
    sum = 0
    for y in range(tree_y):
        sum += 1
        if tree_array[tree_y-y-1][tree_x] >= tree_array[tree_y][tree_x]:
            break
    return sum

def visibility_down(tree_x, tree_y, tree_array):
    sum = 0
    for y in range(tree_y+1, len(tree_array)):
        sum += 1
        if tree_array[y][tree_x] >= tree_array[tree_y][tree_x]:
            break
    return sum

def visibility_left(tree_x, tree_y, tree_array):
    sum = 0
    for x in range(tree_x):
        sum += 1
        if tree_array[tree_y][tree_x-x-1] >= tree_array[tree_y][tree_x]:
            break
    return sum

def visibility_right(tree_x, tree_y, tree_array):
    sum = 0
    for x in range(tree_x+1, len(tree_array[0])):
        sum += 1
        if tree_array[tree_y][x] >= tree_array[tree_y][tree_x]:
            break
    return sum

def tree_visibility(tree_x, tree_y, tree_array):
    a = visibility_up(tree_x, tree_y, tree_array)
    b = visibility_down(tree_x, tree_y, tree_array)
    c = visibility_left(tree_x, tree_y, tree_array)
    d = visibility_right(tree_x, tree_y, tree_array)
    return a*b*c*d

def find_max_tree(tree_array):
    max = 0
    for y in range(len(tree_array)):
        for x in range(len(tree_array[0])):
            if tree_visibility(x,y,tree_array) > max:
                max = tree_visibility(x,y,tree_array)
    return max

def visibility_from_edge(tree_array):
    height = len(tree_array)
    width = len(tree_array[0])
    visibility_array = [[0 for x in range(width)] for y in range(height)]
    for y in range(height):
        max_so_far_left = -1
        max_so_far_right = -1
        for x in range((width+1)//2):
            if max_so_far_left < 9 and tree_array[y][x] > max_so_far_left:
                visibility_array[y][x] = 1
                max_so_far_left = tree_array[y][x]
            if max_so_far_right < 9 and tree_array[y][-x-1] > max_so_far_right:
                visibility_array[y][-x-1] = 1
                max_so_far_right = tree_array[y][-x-1]
        if max_so_far_left < max_so_far_right:
            for x in range((width+1)//2, width):
                if max_so_far_left < max_so_far_right and tree_array[y][x] > max_so_far_left:
                    visibility_array[y][x] = 1
                    max_so_far_left = tree_array[y][x]
        elif max_so_far_right < max_so_far_left:
            for x in range((width+1)//2, width):
                if max_so_far_right < max_so_far_left and tree_array[y][-x-1] > max_so_far_right:
                    visibility_array[y][-x-1] = 1
                    max_so_far_right = tree_array[y][-x-1]
    for x in range(width):
        max_so_far_top = -1
        max_so_far_bottom = -1
        for y in range((height+1)//2):
            if max_so_far_top < 9 and tree_array[y][x] > max_so_far_top:
                visibility_array[y][x] = 1
                max_so_far_top = tree_array[y][x]
            if max_so_far_bottom < 9 and tree_array[-y-1][x] > max_so_far_bottom:
                visibility_array[-y-1][x] = 1
                max_so_far_bottom = tree_array[-y-1][x]
        if max_so_far_top < max_so_far_bottom:
            for y in range((height+1)//2, height):
                if max_so_far_top < max_so_far_bottom and tree_array[y][x] > max_so_far_top:
                    visibility_array[y][x] = 1
                    max_so_far_top = tree_array[y][x]
        elif max_so_far_bottom < max_so_far_top:
            for y in range((height+1)//2, height):
                if max_so_far_bottom < max_so_far_top and tree_array[-y-1][x] > max_so_far_bottom:
                    visibility_array[-y-1][x] = 1
                    max_so_far_bottom = tree_array[-y-1][x]
    return visibility_array

if __name__ == '__main__':
    tree_array = to_array(input_file)
    print(sum([sum(row) for row in (visibility_from_edge(tree_array))]))
    print(find_max_tree(tree_array))
    #print(find_max_tree(to_array('d8/test.txt')))

