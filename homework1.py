import sys
import random
import heapq

import graph
import prims


def difference((weight, length)):
    return (-weight + length, -weight, -length)

def quota((weight, length)):
    return (-float(weight) / length, -weight, -length)

def get_entry(f):
    line = f.readline().strip()
    left, right = line.split(' ')
    weight, length = (int(left), int(right))
    return weight, length

def weighted_sum(filename, objective):
    f = open(filename, 'r')
    num_lines = int(f.readline())
    x = [objective(get_entry(f)) for _ in range(num_lines)]

    heapq.heapify(x)
    t = 0
    S = 0
    for _ in range(num_lines):
        entry = heapq.heappop(x)
        print entry
        diff,weight,length = entry
        weight = -weight
        length = -length
        t = t + length
        S = S + weight * t
    print S


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "usage: ./homework1.py [1|2|3] <inputfile>"
        sys.exit(0)
    question = sys.argv[1]
    filename = sys.argv[2]
    if question == '1':

        weighted_sum(filename, difference)
    elif question == '2':
        weighted_sum(filename, quota)
    elif question == '3':
        _graph = graph.parse(filename, undirected=True)
        _start_node = _graph[random.sample(_graph, 1)[0]]
        mst = prims.spanning_tree(set(_graph.values()), _start_node)

        edges = set()
        for node in mst:
            [edges.add(e) for e in node.edges]
        edge_sum = 0
        for e in edges:
            if e.spanning:
                edge_sum += e.cost

        graph.graphviz(filename.replace('.txt', '.neato'), edges)
        print edge_sum
    else:
        print 'Unknown assignment: ' + question
