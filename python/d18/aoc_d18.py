input_file = 'python/d18/input.txt'
test_file = 'python/d18/test.txt'

def distance(tuple1, tuple2):
    return sum([abs(tuple1[i] - tuple2[i]) for i in range(len(tuple1))])

def adjacent(tuple1, tuple2):
    return distance(tuple1, tuple2) == 1

def surface_area(filename):
    vertices = set()
    adjacencies = 0
    with open(filename) as file:
        for line in file:
            point = tuple(int(x) for x in line.strip().split(","))
            for location in vertices:
                if adjacent(location, point):
                    adjacencies+=1
            vertices.add(point)
    return 6*len(vertices) - 2*adjacencies

def neighbours(point, minimum, maximum):
    output = set()
    if point[0] -1 >= minimum:
        output.add((point[0]-1, point[1], point[2]))
    if point[0] +1 <= maximum:
        output.add((point[0]+1, point[1], point[2]))
    if point[1] -1 >= minimum:
        output.add((point[0], point[1]-1, point[2]))
    if point[1] +1 <= maximum:
        output.add((point[0], point[1]+1, point[2]))
    if point[2] -1 >= minimum:
        output.add((point[0], point[1], point[2]-1))
    if point[2] +1 <= maximum:
        output.add((point[0], point[1], point[2]+1))
    return output

def exterior_area(filename):
    vertices = set()
    minimum = 1
    maximum = 1
    with open(filename) as file:
        for line in file:
            point = tuple(int(x) for x in line.strip().split(","))
            minimum = min(minimum, *point)
            maximum = max(maximum, *point)
            vertices.add(point)
    minimum -= 1
    maximum += 1
    outside_set_unvisited = set()
    outside_set_visited = set()
    area = 0
    outside_set_unvisited.add((minimum,minimum,minimum))
    while len(outside_set_unvisited) > 0:
        current = outside_set_unvisited.pop()
        outside_set_visited.add(current)
        adjacenies = neighbours(current,minimum,maximum)
        area += len(adjacenies.intersection(vertices))
        adjacenies.difference_update(vertices)
        adjacenies.difference_update(outside_set_visited)
        outside_set_unvisited.update(adjacenies)
    return area

def exterior_area2(vertices):
    minimum = 1
    maximum = 1
    minimum -= 1
    maximum += 1
    outside_set_unvisited = set()
    outside_set_visited = set()
    area = 0
    outside_set_unvisited.add((minimum,minimum,minimum))
    while len(outside_set_unvisited) > 0:
        current = outside_set_unvisited.pop()
        outside_set_visited.add(current)
        adjacenies = neighbours(current,minimum,maximum)
        area += len(adjacenies.intersection(vertices))
        adjacenies.difference_update(vertices)
        adjacenies.difference_update(outside_set_visited)
        outside_set_unvisited.update(adjacenies)
    return area


if __name__ == '__main__':
    print(surface_area(input_file))
    print(exterior_area(input_file))
    # print(exterior_area2({(1,1,1)}))
