import re

input_file = 'python/d16/input.txt'
test_file = 'python/d16/test.txt'

class Node:
    def __init__(self, id, distance = None, flowrate = 0):
        self.neighbours = []
        self.id = id
        self.distance = distance
        self.flowrate = flowrate

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.id

def min_distance(list_of_nodes):
    if len(list_of_nodes) == 0:
        return None
    min_so_far = list_of_nodes[0]
    for node in list_of_nodes:
        if node.distance is not None and (min_so_far.distance is None or node.distance < min_so_far.distance):
            min_so_far = node
    return min_so_far

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.min_distance = {}

    def dijkstras(self, start, end_condition):
        unvisited = self.nodes.copy()
        current = start
        while len(unvisited) > 0:
            if end_condition(current):
                return current.distance
            for neighbour in current.neighbours:
                if neighbour.distance is None:
                    neighbour.distance = current.distance + 1
                else:
                    neighbour.distance = min(neighbour.distance, current.distance+1)
            unvisited.remove(current)
            current = min_distance(unvisited)

    def build_min_distances(self):
        for start_node in self.nodes:
            set_distances(self.nodes, None)
            start_node.distance = 0
            self.dijkstras(start_node, lambda x: False)
            self.min_distance[start_node.id] = dict([(node.id, node.distance+1) for node in self.nodes])

    def max_flow_rate(self, start_node, target_nodes, time):
        if time <= 0:
            return 0
        first_step = start_node.flowrate*time
        second_step = max([self.max_flow_rate(node, [target for target in target_nodes if target != node], time-self.min_distance[start_node.id][node.id]) for node in target_nodes]+[0])
        return first_step + second_step

    def multi_headed_flow(self, start, targets, time, num_heads):
        max_attempt = 0
        if num_heads == 1:
            return self.max_flow_rate(start,targets,time)
        for path in self.make_paths(start, targets, time):
            current = start
            current_time = time
            path_sum = 0
            for node in path[1:]:
                current_time -= self.min_distance[current.id][node.id]
                path_sum += current_time*node.flowrate
                current = node
            rest = self.multi_headed_flow(start, [x for x in targets if x not in path], time, num_heads-1)
            max_attempt = max(max_attempt, path_sum + rest)
        return max_attempt
    
    def make_paths(self, start, targets, time):
        total_paths = [[]]
        for node in targets:
            time_remaining = time - self.min_distance[start.id][node.id]
            if time_remaining > 0:
                path_from_node = self.make_paths(node, [x for x in targets if x != node], time_remaining)
                total_paths += path_from_node
        total_paths = [[start] + path for path in total_paths]
        return total_paths


def build_nodes(filename):
    dict_of_nodes = {}
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            flow = [int(x) for x in re.findall(r'-?\d+', line)][0]
            id = re.findall(r'[A-Z]{2}', line)[0]
            dict_of_nodes[id] = Node(id = id, flowrate=flow)
        for line in lines:
            list_of_ids = re.findall(r'[A-Z]{2}', line)
            myNode = dict_of_nodes[list_of_ids[0]]
            for id in list_of_ids[1:]:
                myNode.neighbours.append(dict_of_nodes[id])
    return dict_of_nodes

def set_distances(list_of_nodes, value):
    for node in list_of_nodes:
        node.distance = value

if __name__ == '__main__':
    myNodes = build_nodes(input_file)
    myGraph = Graph(list(myNodes.values()))
    myGraph.build_min_distances()
    non_zero_nodes = [node for node in list(myNodes.values()) if node.flowrate > 0]
    max_flow = myGraph.max_flow_rate(myNodes['AA'], non_zero_nodes, 30)
    print(max_flow)
    print(myGraph.multi_headed_flow(myNodes['AA'],non_zero_nodes,26,2))
