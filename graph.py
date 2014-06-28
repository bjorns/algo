 # coding=utf-8

class Node(object):
    def __init__(self, name, edges=None):
        self.name = name
        self.edges = edges if edges else set()
        self.cost = -1

    def __str__(self):
        return str(self.name)

class Edge(object):
    def __init__(self, src, cost, dst):
        self.src = src
        assert cost >= 0
        self.cost = cost
        self.dst = dst

    def __str__(self):
        return "{} -> {} {}".format(self.src, self.cost, self.dst)


def parse_edge(nodes, line):
    relation = line.split(' ')
    assert len(relation) == 4

    src = nodes.setdefault(relation[0], Node(relation[0]))
    nodes
    assert relation[1] == '->'
    cost = int(relation[2])
    dst = nodes.setdefault(relation[3], Node(relation[3]))
    edge = Edge(src, cost, dst)
    src.edges.add(edge)
    return edge


def parse(filename):
    nodes = {}
    for line in file(filename):
        edge = parse_edge(nodes, line.strip())
        #print edge
    return nodes
