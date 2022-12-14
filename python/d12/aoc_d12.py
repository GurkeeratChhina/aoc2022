input_file = 'python/d12/input.txt'

class Node:
    def __init__(self, height, distance = None):
        self.neighbours = []
        self.height = height
        self.distance = distance

def min_distance(list_of_nodes):
    min_so_far = list_of_nodes[0]
    for node in list_of_nodes:
        if node.distance is not None and (min_so_far.distance is None or node.distance < min_so_far.distance):
            min_so_far = node
    return min_so_far

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def dijkstras(self, start, end_condition, node_condition):
        unvisited = self.nodes
        current = start
        while True:
            if end_condition(current):
                return current.distance
            for neighbour in current.neighbours:
                if node_condition(current, neighbour):
                    if neighbour.distance is None:
                        neighbour.distance = current.distance + 1
                    else:
                        neighbour.distance = min(neighbour.distance, current.distance+1)
            unvisited.remove(current)
            current = min_distance(unvisited)

def build_graph(filename):
    list_of_nodes = []
    start_node = None
    end_node = None
    with open(filename) as file:
        for line in file:
            row = []
            for letter in line.strip():
                if letter == "S":
                    start_node = Node(0)
                    row.append(start_node)
                elif letter == "E":
                    end_node = Node(25)
                    row.append(end_node)
                else:
                    row.append(Node(ord(letter)-ord("a")))
            list_of_nodes.append(row)
        height = len(list_of_nodes)
        width = len(list_of_nodes[0])
        for x in range(width):
            for y in range(height):
                if x == 0:
                    list_of_nodes[y][x].neighbours.append(list_of_nodes[y][x+1])
                elif x == width-1:
                    list_of_nodes[y][x].neighbours.append(list_of_nodes[y][x-1])
                else:
                    list_of_nodes[y][x].neighbours.append(list_of_nodes[y][x+1])
                    list_of_nodes[y][x].neighbours.append(list_of_nodes[y][x-1])
                if y == 0:
                    list_of_nodes[y][x].neighbours.append(list_of_nodes[y+1][x])
                elif y == height-1:
                    list_of_nodes[y][x].neighbours.append(list_of_nodes[y-1][x])
                else:
                    list_of_nodes[y][x].neighbours.append(list_of_nodes[y+1][x])
                    list_of_nodes[y][x].neighbours.append(list_of_nodes[y-1][x])
    return [Graph([x for row in list_of_nodes for x in row]), start_node, end_node]

if __name__ == '__main__':
    myGraph, starting_node, ending_node = build_graph(input_file)
    # starting_node.distance = 0
    # print(myGraph.dijkstras(starting_node,lambda x: x == ending_node, lambda x,y: y.height <= x.height +1))
    ending_node.distance = 0
    print(myGraph.dijkstras(ending_node, lambda x: x.height == 0, lambda x,y: y.height >= x.height -1))

