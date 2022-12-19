import re
import scipy
import timeit

input_file = 'python/d15/input.txt'
test_file = 'python/d15/test.txt'
second_test = 'python/d15/basic.txt'

myrow = 2000000
myrange = (0,4000000)
M = 100000000

def l1(a, b, c, d):
    return abs(a-c)+abs(b-d)

def ball(a, b, c, d, row):
    return max(-1, l1(a,b,c,d) - abs(b - row))

def union(pair):
    return (min(pair[0][0], pair[1][0]), max(pair[0][1], pair[1][1]))

def union_all(list_of_intervals):
    list_of_intervals[:] = sort_intervals(list_of_intervals)
    i = 0
    while(i< len(list_of_intervals)-2):
        if list_of_intervals[i][1] >= list_of_intervals[i+1][0]-1:
            list_of_intervals[:] = list_of_intervals[0:i] + [union([list_of_intervals[i], list_of_intervals[i+1]])] + list_of_intervals[i+2:]
        else:
            i += 1
    if list_of_intervals[-2][1] >= list_of_intervals[-1][0]-1:
        list_of_intervals[:] = list_of_intervals[0:-2] + [union([list_of_intervals[-2], list_of_intervals[-1]])]

def sort_intervals(list_of_intervals):
    return sorted(list_of_intervals, key=lambda x: x[0])

def build_intervals(filename, rownumber):
    list = []
    beacons = set()
    with open(filename) as file:
        for line in file:
            a,b,c,d = [int(x) for x in re.findall(r'-?\d+', line)]
            r = ball(a, b, c, d, rownumber)
            if r >= 0:
                list.append((a-r, a+r))
            if d == rownumber:
                beacons.add((c,d))
    return [list, beacons]

def intersect_intervals(list_of_intervals, target_range):
    for interval in list_of_intervals:
        if interval[1] < target_range[0] or interval[0] > target_range[1]:
            list_of_intervals.remove(interval)
        elif interval[0] < target_range[0] or interval[1] > target_range[1]:
            new_interval = (max(target_range[0],interval[0]), min(interval[1],target_range[1]))
            list_of_intervals.append(new_interval)
            list_of_intervals.remove(interval)

def find_gaps(filename, target_range):
    for row in range(target_range[0], target_range[1]):
        if row%(target_range[1]//100) == 0:
            print(100*row//target_range[1],"%")
        intervals = build_intervals(filename, row)[0]
        intersect_intervals(intervals, target_range)
        intervals += [(target_range[0]-1, target_range[0]-1), (target_range[1]+1, target_range[1]+1)]
        union_all(intervals)
        if len(intervals)> 1:
            return [intervals[0][1]+1, row]

def linear_program(filename, x_range, y_range, objective):
    with open(filename) as file:
        lines = file.readlines()
        n = len(lines)
        a_ub = [[0 for x in range(2*n+2)] for y in range(4*n)]
        b_ub = []
        for i in range(n):
            line = lines[i]
            a,b,c,d = [int(x) for x in re.findall(r'-?\d+', line)]
            r = l1(a, b, c, d)+1
            a_ub[4*i][0:2] = [-1,-1]
            a_ub[4*i][2*i+2:2*i+4] = [-M, -M]
            a_ub[4*i+1][0:2] = [-1,1]
            a_ub[4*i+1][2*i+2:2*i+4] = [-M, M]
            a_ub[4*i+2][0:2] = [1,-1]
            a_ub[4*i+2][2*i+2:2*i+4] = [M, -M]
            a_ub[4*i+3][0:2] = [1,1]
            a_ub[4*i+3][2*i+2:2*i+4] = [M, M]
            b_ub.append(-a-b-r)
            b_ub.append(-a+b+M-r)
            b_ub.append(a-b+M-r)
            b_ub.append(a+b+2*M-r)
        c = objective + [0 for x in range(2*n)]
        bounds = [x_range, y_range] + [(0,1) for x in range(2*n)]
        integral = [1 for x in range(2*n + 2)]
    result = scipy.optimize.linprog(c=c, A_ub = a_ub, b_ub = b_ub, bounds = bounds, integrality = integral)
    return result.fun

if __name__ == '__main__':
    intervals, beacons = build_intervals(input_file, myrow)
    union_all(intervals)
    sum = sum([x[1] - x[0] +1 for x in intervals]) - len(beacons)
    print(sum)
    print(linear_program(input_file,myrange,myrange,[4000000,1]))
    # find_gaps(input_file, myrange)
    # print(2628223+2939043*4000000)
    # time = timeit.timeit('linear_program("python/d15/input.txt", (0,4000000), (0,4000000), [4000000, 1])', "from __main__ import linear_program", number = 10)
    # print(time)